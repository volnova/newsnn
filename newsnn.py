# -*- coding: utf-8 -*-

import requests

from datetime import datetime
from lxml import html


def request_to_site():
    date_now = datetime.strftime(datetime.now(), "%Y/%m/%d")
    r = requests.get('http://newsnn.ru/news/{}/'.format(date_now))
    root = html.fromstring(r.text)
    xpath_dict = {
        'titles': root.xpath('.//img[@class="preview_picture"]/@title'),
        'links': root.xpath('.//img[@class="preview_picture"]/@src'),
        'dates': root.xpath('.//div[@class="news-list"]/div/div/span[@class="news-date-time"]/span/text()')
    }

    for i in xrange(len(xpath_dict["titles"])):
        news = {
            'subject': xpath_dict["titles"][i],
            'img': 'http://newsnn.ru/{}'.format(xpath_dict["links"][i]),
            'date': '{} {}'.format(date_now, xpath_dict["dates"][i])
        }
        print news

request_to_site()
