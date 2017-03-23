# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup


class DMovieSpider(scrapy.Spider):
    name = "d-movie"
    allowed_domains = ["douban.com"]
    start_urls = ['https://movie.douban.com/tag/']

    def parse(self, response):
        html = response.body
        soup = BeautifulSoup(html)
        print(soup.find_all('a'))
        pass
