from fastapi import FastAPI, Query
import requests
import json
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/")
async def process_input(url: str = Query(None)):
    if not url:
        return "Please input a URL by adding it as a query parameter to the URL, like this: /?url=<your_input_url>"
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
