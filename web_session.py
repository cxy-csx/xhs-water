import requests
import execjs
import random

def register_Id(c=32):
    s = "abcdef0123456789"
    webId = ''
    for i in range(c):
        webId += random.choice(s)
    return webId

def get_web_session():
    url = 'https://edith.xiaohongshu.com/api/sns/web/v1/login/activate'  # 请求接口
    headers = {
        'authority': 'edith.xiaohongshu.com',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json;charset=UTF-8',
        'cookie': 'abRequestId=7b41aa2f-2697-5d9b-876a-ea36f33c24e8; webBuild=3.5.1; xsecappid=xhs-pc-web; a1=18a11a81a61qglsx42mq3m9cja9d9e4q5owz2kvx950000293680; webId=0ad4917f75dfc85b8ae22d05bb9f4fa3; websectiga=8886be45f388a1ee7bf611a69f3e174cae48f1ea02c0f8ec3256031b8be9c7ee; sec_poison_id=cd7637f9-6695-4af9-b769-a924b3ec9c01',
        'origin': 'https://www.xiaohongshu.com',
        'pragma': 'no-cache',
        'referer': 'https://www.xiaohongshu.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'x-b3-traceid': '59fade6c65d0f3ca',
        'x-s': 'XYW_eyJzaWduU3ZuIjoiNTEiLCJzaWduVHlwZSI6IngxIiwiYXBwSWQiOiJ4aHMtcGMtd2ViIiwic2lnblZlcnNpb24iOiIxIiwicGF5bG9hZCI6IjM0ODc4M2Y2MzhiYmRiN2MxNDhiMDMxYTdkZjRhMGI0ZmRhNzZjMjQ0YTE0YmNiMmYzN2NlOTVmYWMxOTdhYTI2YzY1MGE1ZmQwNTg3MmVjNTBkODdkOWEzYzYxMWYwNGM5ZTNiZmRhMWZhYTFlYjkwZDc0YWEzMWI1NGM3MmNkMGQ3NGFhMzFiNTRjNzJjZGFjNDg5YjlkYThjZTVlNDhmNGFmYjlhY2ZjM2VhMjZmZTBiMjY2YTZiNGNjM2NiNTljMTI3ZWM0YTE1ZmM0NzY0NTgzMjljOGYzNzMzNzM5YTAxNTk2MzkwNGI4OGI2ZTFlODk2ZjQ3ZWFmZTQzZTgyZmE1M2MzNjM2ZGRlZGRhNThlMTkzMTA0YmFhZTRiZGU3Njg5NzUwMDVhOTIyMzRkMTdkYzI3MjIzNTNkNWNiMTg4YTVhNzBjY2RjMDU0ODRiOTBiYmI2NGE3MGJiNTYwYjA5MjFkNjQ1ZGIxYTdkMDE5ZTE4YTRiYzM0NzUyYyJ9',
        'x-s-common': '2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1+jhIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHAN0L1PaHVHdWMH0ijP/YYP/bYwebY+0bl89lA2ecUJgrAJ/S0yfrE8eSS+orMJ74CPfT92eDMPeZIPeHEPAGhPsHVHdW9H0il+0DU+/rAPAcMPeqUNsQh+UHCHSY8pMRS2LkCGp4D4pLAndpQyfRk/SzbyLleadkYp9zMpDYV4Mk/a/8QJf4hanS7ypSGcd4/pMbk/9St+BbH/gz0zFMF8eQnyLSk49S0Pfl1GflyJB+1/dmjP0zk/9SQ2rSk49S0zFGMGDqEybkea/8QyDFI/Fz0+rFUn/Q+2fYknnMayLhU/gYwzBYk/Lz+2bSL8BTyySQi/L4QPbkTLfYw2Skx/nkzPbSLz/m8JLEk/nM82DhU/flOpb8Tnp4+2rRL8BY8prDUngk8PLMoz/byJpb7/SzdPFMTpfkwprQ3/FzDyFRgzgk82SSh/p484FEo//pyprEknfMayrMgnfY8pr8Vnnk34MkrGAm8pFpC/p4QPLEo//++JLE3/L4zPFEozfY+2D8k/SzayDECafkyzF8x/Dzd+pSxJBT8pBYxnSznJrEryBMwzF8TnnkVybDUnfk+PS8i/nkyJpkLcfS+ySDUnpzyyLEo/fk+PDEk/SzVyDMLa/+ypFFInpzbPpkT//mw2SDI/Szd2DMxJBkOzMSC/dk+2DEC//p8prbh/Sz3PDMCy74wzFDF/F4QPSkLzflOzBVUnfkzPMkgzfMypbbCnSzd2pkTz/b+PDMC/fk+PSkoLflyzMQi/SziJrMLy7k+prrInnMBybkLLfSyzMLA/fkd+LECpg4+zb8i/MzQ2LMCLfT+pBz3ngkQPFMxagkwprE3/S4wyLML8Az8pb8i/dksySDULfk+zbLI/FzayLRLcfS8JLDU/D4bPFMoafSwpbS7nnkm+LMxzfTwySrlnD4Q2bSL8BT+zrLMnSzb+bSLLfS82DFI/dkp2pSEa0DjNsQhwsHCJdpVJsIj2eDjw0rEPeZ7PePA+0PVHdWlPsHC+gF=',
        'x-t': '1692513345072',
    }

    json_data = {}

    response = requests.post(
        url,
        headers=headers,
        json=json_data,
    )
    print(response.content)
    return response.json()['data']['session']


get_web_session()
