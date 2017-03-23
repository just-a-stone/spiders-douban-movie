# -*- coding: utf-8 -*-
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
        html = response.body
        soup = BeautifulSoup(html, 'lxml')
        item = DoubanMovieItem()
        item['name'] = soup.find('span', attrs={'property': 'v:itemreviewed'}).string
        item['frontCover'] = soup.find('img', attrs={'rel': 'v:image'})['src']
        item['director'] = soup.find('a', attrs={'rel': 'v:directedBy'}).string
        item['screenWriter'] = soup.find('span', text='编剧').next_sibling.next_sibling.string
        item['stars'] = []
        for actor in soup.find_all('a', {'rel': 'v:starring'}):
            item['stars'].append(actor.string)

        item['styleTag'] = []
        for style in soup.find_all('span',attrs={'property':'v:genre'}):
            item['styleTag'].append(style.string)

        item['summary'] = tuple(soup.find('span',attrs={'property':'v:summary'}).stripped_strings)
        item['associate'] = {}
        for associate in soup.find('div','recommendations-bd').children:
            # tags = associate.descendants
            if isinstance(associate,Tag):
                name = associate.dd.a.string
                href = associate.dt.a['href']
                item['associate'][name] = href
                # print(tags)
            # item['association'][tags[]]
        yield item

        for movie in item['associate'].values():
            yield scrapy.Request(url=movie,callback=self.parse)

        print(item)
        pass
