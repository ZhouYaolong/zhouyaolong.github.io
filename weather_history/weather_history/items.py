# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from weather_history.custom_settings import listDictKeys


class WeatherHistoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    for index in range(len(listDictKeys)):
        locals()[listDictKeys[index]] = Field()
    pass
