# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiHocItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    unit = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    dschuhan = scrapy.Field()
    dstughep = scrapy.Field()
    pass

class ChuHanItem(scrapy.Item):
	hantu = scrapy.Field()
	amhan = scrapy.Field()
	ynghia = scrapy.Field()
	pass

class TuGhepItem(scrapy.Item):
	tughep = scrapy.Field()
	amhan = scrapy.Field()
	hiragana = scrapy.Field()
	ynghia = scrapy.Field()
	pass
		
		
