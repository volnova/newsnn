# -*- coding: utf-8 -*-
import requests
from datetime import datetime
from lxml import html


class News:
    def __init__(self, subject, img, date):
        self.subject = subject
        self.img = img
        self.date = datetime.strptime(date, '%Y/%m/%d %H:%M')


def request_to_site():
    date_now = datetime.strftime(datetime.now(), "%Y/%m/%d")
    r = requests.get('http://newsnn.ru/news/{}/'.format(date_now))
    print 'http://newsnn.ru/news/{}/'.format(date_now)
    root = html.fromstring(r.text)
    xpath_dict = {
        'news': './/div[@class="news-list"]/*/div[@class="news-item"]',
        'subject': './/img[@class="preview_picture"]/@title',
        'img': './/img[@class="preview_picture"]/@src',
        'date': './/span[@class="news-date-time"]/span/text()'
    }
    news_list = root.xpath(xpath_dict['news'])
    del root

    for item in news_list:
        obj = News(subject=item.xpath(xpath_dict["subject"])[0],
                   img='http://newsnn.ru/{}'.format(item.xpath(xpath_dict['img'])[0]),
                   date='{} {}'.format(date_now, item.xpath(xpath_dict['date'])[0]))
        print obj.__dict__

request_to_site()
