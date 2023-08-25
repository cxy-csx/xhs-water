import ast
import random
import re
import urllib
import requests


def get_real_url(url):
    resp = requests.get(url, allow_redirects=False)
    if resp.headers.get('Location'):
        real_url = re.search('item/(.*?)\\?app_platform', resp.headers.get('Location'))
        if real_url:
            return "https://www.xiaohongshu.com/explore/" + urllib.parse.unquote(real_url.group(1))
        else:
            real_url = re.search('redirectPath=(.*?)&', resp.headers.get('Location'))
            if real_url:
                return urllib.parse.unquote(real_url.group(1))
    else:
        return url


def get_pic(link):
    with open('web_session.txt', 'r', encoding='utf-8') as fp:
        web_session_list = fp.readlines()
        num_items = len(web_session_list)
        random_index = random.randrange(num_items)
        web_session = web_session_list[random_index]
        print(web_session.replace('\n', ''))
    headers = {
        'cookie': f'web_session={web_session}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }

    response = requests.get(
        link,
        headers=headers,
    )

    # print(response.content)

    pattern = r'"imageList":(.*?}]),'

    imgList = re.findall(pattern, response.content.decode('utf-8'))
    print(imgList)
    newList = []
    if imgList:
        for i in ast.literal_eval(imgList[0]):
            fullUrl = re.sub(r"([0-9a-fA-F-]+)$", i['traceId'], i['url'])
            print(fullUrl)
            newList.append(fullUrl)
    return newList


if __name__ == '__main__':
    url = get_real_url('https://www.xiaohongshu.com/explore/64c5d938000000001201b98b')
    if url:
        print(url)
        print(get_pic(url))
