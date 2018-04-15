# -*- coding: utf-8 -*-
import scrapy
from weather_history.items import WeatherHistoryItem
from weather_history.custom_settings import listDictKeys
import re


class CoreSpider(scrapy.Spider):
    name = 'core'
    # allowed_domains = ['http://www.tianqihoubao.com/lishi/ningbo/month/201709.html']
    start_urls = ['http://www.tianqihoubao.com/lishi/ningbo/month/201709.html']

    def parse(self, response):
        for href in response.css('.months a::attr(href)').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, self.parse_content)

    def parse_content(self, response):
        item = WeatherHistoryItem()
        for tr in response.css("#content table tr:not(:first-child)"):
            temp = re.findall('[\d\-\.]+', tr.css('td a::attr(title)').extract()[0])
            item['date'] = '-'.join(temp)
            temp = re.findall('[\u4E00-\u9FFF]+', tr.css('td:nth-child(2)::text').extract()[0])
            item['stateMorning'] = temp[0]
            item['stateNight'] = temp[1]
            temp = re.findall('[\d\-\.]+', tr.css('td:nth-child(3)::text').extract()[0])
            item['temperatureMorning'] = temp[0]
            item['temperatureNight'] = temp[1]
            temp = re.findall('([\u4E00-\u9FFF]+) ', tr.css('td:nth-child(4)::text').extract()[0])
            item['windDirectionMorning'] = temp[0]
            item['windDirectionNight'] = temp[1]
            temp = re.findall(' ([^\u4E00-\u9FFF]+)\u7ea7', tr.css('td:nth-child(4)::text').extract()[0])
            item['windForceMorning'] = temp[0]
            item['windForceNight'] = temp[1]
            yield item
