# hiru.py
import subprocess
import requests
import json



def get_video_url(url):
    headers = {
        'Host': 'www.y2mate.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.y2mate.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.y2mate.com/en403/convert-youtube',
        'Accept-Language': 'en,en-GB;q=0.9,en-US;q=0.8',
    }

    data = {
        'k_query': url,
        'k_page': 'Youtube Converter',
        'hl': 'en',
        'q_auto': '0',
    }
    try:
        response = requests.post('https://www.y2mate.com/mates/analyzeV2/ajax', headers=headers, data=data)
        data = json.loads(response.content)
        video_url = data['links']['video'][0]['url']
        return video_url
    except requests.exceptions.RequestException as e:
        # If an error occurs, return the error message
        return str(e)
       
