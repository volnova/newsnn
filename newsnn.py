# -*- coding: utf-8 -*-

import requests

from lxml import html


def request_to_site():
    r = requests.get('http://newsnn.ru/news/2016/9/10/')
    root = html.fromstring(r.text)
    titles = root.xpath('.//img[@class="preview_picture"]/@title')
    links = root.xpath('.//img[@class="preview_picture"]/@src')

    for i in range(len(titles)):
        news = {'subject': titles[i], 'img': 'http://newsnn.ru/' + links[i]}
        print news

request_to_site()
