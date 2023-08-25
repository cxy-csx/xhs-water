import re

from flask import Flask, request
import spider

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = request.args.get('url')

    if url:
        url = re.search('(http.*)(&?)', url)
        print(url)
        url = url.group(1).split('，')[0]
        print(url)
        img = spider.get_pic(spider.get_real_url(url))
        print(img)
        return img

    return []


if __name__ == '__main__':
    app.run()
