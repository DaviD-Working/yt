from fastapi import FastAPI, Query
import requests
from fastapi import HTTPException
from hiru import get_video_url
import json
from fastapi.responses import HTMLResponse
app = FastAPI()

@app.get("/{hiru}")
async def root():
    return HTMLResponse(content="Please input a URL by adding it as a query parameter to the URL for Facebook video, like this: /?url=<your_input_url> <br><br> for youtube /yt/download?url=<url>", status_code=200)


   
@app.get("/")
async def process_input(url: str = Query(None)):
    if not url:
        return "Please input a URL by adding it as a query parameter to the URL for Facebook video, like this: /?url=<your_input_url>                       for youtube /yt/download?url=<url>"
    fb_url = url
    headers = {
        'Host': 'api.savefrom.biz',
        'user-agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'origin': 'https://savefrom.biz',
        'x-requested-with': 'idm.internet.download.manager.plus',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://savefrom.biz/',
        'accept-language': 'en,en-GB;q=0.9,en-US;q=0.8',
    }

    json_data = {
        'url': '{}'.format(fb_url),
    }

    try:
        response = requests.post('https://api.savefrom.biz/api/convert', headers=headers, json=json_data)
        data = json.loads(response.content)
        hd_url = data['hd']['url']
        sd_url = data['sd']['url']
        html_string= f"""
            <html>
                <body>
                    <h1>The HD video URL is:</h1>
                    <p>{hd_url}</p> <br> <br>
                    <h1>The SD video URL is:</h1> <br>
                    <p>{sd_url}</p>
                    Download link: <a href={hd_url}>HD video</a> <br>
                    Download link: <a href={sd_url}>SD video</a>
                </body>
            </html>
            """
    except:
        return "Something went wrong. Please try again later."
             
    return HTMLResponse(content=html_string, status_code=200)    


@app.get("/insta/download")
def get_video_url_html(url: str):
    video_url = get_video_url(url)
    if video_url is None:
        raise HTTPException(status_code=400, detail="Something went wrong. Please try again with a different URL.")    
    html_string= f"<html><body>{video_url} <br><a href='{video_url}'>Video URL</a></body></html>"
    return HTMLResponse(content=html_string, status_code=200)                
