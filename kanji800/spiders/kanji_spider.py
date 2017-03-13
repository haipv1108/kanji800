# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy import Request

from kanji800.items import BaiHocItem
from kanji800.items import ChuHanItem
from kanji800.items import TuGhepItem

class Kanji800Spider(Spider):
	name = "kanji800"
	allowed_domains = ["tiengnhat24h.com"]
	start_urls = [
		"http://tiengnhat24h.com/vi/kanji/800-chu-han-thong-dung",
	]	

	def parse(self, response):
		res_lessons = response.css('div.kotoba ul.list li')
		for item in res_lessons:
			lesson = BaiHocItem()
			url = item.css('a::attr(href)').extract_first()
			lesson['url'] = url
			title = item.css('a::text').extract_first()
			lesson['title'] = title
			lesson['unit'] = int(title.split( )[1])
			details_lesson_request = Request(url, callback=self.parse_details_lesson)
			details_lesson_request.meta['lesson'] = lesson
			yield details_lesson_request
		yield lesson

	def parse_details_lesson(self, response):
		lesson = response.meta['lesson']
		lesson['dschuhan'] = []
		lesson['dstughep'] = []

		dschuhan = response.css('div#kanji1 table tbody tr')
		dschuhan.pop(0)

		for itemchuhan in dschuhan:
			chuhan = ChuHanItem()
			chuhan['hantu'] = itemchuhan.css('td::text').extract()[0]
			chuhan['amhan'] = itemchuhan.css('td::text').extract()[1]
			chuhan['ynghia'] = itemchuhan.css('td::text').extract()[2]

			lesson['dschuhan'].append(chuhan)

		dstughep = response.css('div#kanji2 table tbody tr')

		for itemtughep in dstughep:
			tughep = TuGhepItem()
			tughep['tughep'] = itemtughep.css('td::text').extract()[0]
			tughep['amhan'] = itemtughep.css('td.fontjp::text').extract_first()
			tughep['hiragana'] = itemtughep.css('td.fontjp::text').extract()[1]
			tughep['ynghia'] = itemtughep.css('td::text').extract()[3]

			lesson['dstughep'].append(tughep)

		return lesson
