# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    frontCover = scrapy.Field()
    director = scrapy.Field()
    screenWriter = scrapy.Field()
    stars = scrapy.Field()
    styleTag = scrapy.Field()
    location = scrapy.Field()
    language = scrapy.Field()
    launchDate = scrapy.Field()
    duration = scrapy.Field()
    alias = scrapy.Field()
    summary = scrapy.Field()
    associate = scrapy.Field()

    pass
