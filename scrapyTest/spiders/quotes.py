# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'   #项目唯一标识，用于初始化项目
    allowed_domains = ['quotes.toscrape.com']   #定义要爬取得域名，不是该域名下的网址不处理
    start_urls = ['http://quotes.toscrape.com/']   #要爬取得url列表，可以多个

    def parse(self, response):
        #print(response)
        #pass
        for qu in response.css('.quotes'):
            text = qu.css('.text::text').extract_first()  #::text 代表.text()
            author = qu.css('.author::text').extract_first()
            tags = qu.css('.tags .tag::text').extract()
            print(text)
            item = ScrapytestItem()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item
