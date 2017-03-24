# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from elasticsearch import Elasticsearch


class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        self.process_es(item)

        return item

    def process_es(self, item):
        es = Elasticsearch(hosts='127.0.0.1:9200')
        # es.index(index='douban', doc_type='movie', body=json.dumps(item.__dict__['_values']), id=item['id'])
        es.index(index='douban', doc_type='movie', body=json.dumps(item.__dict__['_values']), id=item['id'])
