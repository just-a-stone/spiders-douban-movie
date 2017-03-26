# -*- coding: utf-8 -*-
import re
import scrapy
import time
from bs4 import BeautifulSoup
from bs4.element import Tag
from douban.items import DoubanMovieItem


class DMovieSpider(scrapy.Spider):
    name = "d-movie"
    allowed_domains = ["douban.com"]
    start_urls = ['https://movie.douban.com/subject/25934014/']

    def parse(self, response):
        print(response.request.url)
        html = response.body
        soup = BeautifulSoup(html, 'lxml')
        item = DoubanMovieItem()
        item['id'] = re.search('/(\d+)/',response.request.url).group(1)
        item['name'] = soup.find('span', attrs={'property': 'v:itemreviewed'}).string
        item['frontCover'] = soup.find('img', attrs={'rel': 'v:image'})['src']
        item['director'] = soup.find('a', attrs={'rel': 'v:directedBy'}).string
        item['screenWriter'] = soup.find('span', text='编剧').next_sibling.next_sibling.string
        item['stars'] = []
        for actor in soup.find_all('a', {'rel': 'v:starring'}):
            item['stars'].append(actor.string)
        item['stars'] = str(item['stars'])

        item['styleTag'] = []
        for style in soup.find_all('span',attrs={'property':'v:genre'}):
            item['styleTag'].append(style.string)
        item['styleTag'] = str(item['styleTag'])

        item['summary'] = str(tuple(soup.find('span',attrs={'property':'v:summary'}).stripped_strings))
        ass = {}
        item['associate'] = []
        for associate in soup.find('div','recommendations-bd').children:
            if isinstance(associate,Tag):
                name = associate.dd.a.string
                href = associate.dt.a['href']
                item['associate'].append(name)
                ass[name] = href
        item['associate'] = str(item['associate'])
        yield item

        for movie in ass.values():
            yield scrapy.Request(url=movie,callback=self.parse)

        print(item)
        pass
