# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from weather_history.custom_settings import mongodbSetting

class WeatherHistoryPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient()
        db = client[mongodbSetting['db']]
        self.collect = db[mongodbSetting['collect']]
        # print(mongodbSetting['collect'])

    def process_item(self, item, spider):
        # self.collect.insert_one(dict(item), True)
        self.collect.update({'date': item['date']}, {'$set': dict(item)}, True)

        # valid = True
        # for data in item:
        #     if not data:
        #         valid = False
        #         raise DropItem("Missing {0}!".format(data))
        # if valid:
        #     self.collect.insert_one(dict(item),True)
        #     # self.collect.update({'date': item['date']}, {'$set': dict(item)})
        #     log.msg("Question added to MongoDB database!",
        #             level=log.DEBUG, spider=spider)

        return item
