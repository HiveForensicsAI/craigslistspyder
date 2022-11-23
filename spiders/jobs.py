# -*- coding: utf-8 -*-
from scrapy import Request
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://miami.craigslist.org/search/apa?sort=dateoldest&min_price=&max_price=&availabilityMode=0&is_furnished=1&sale_date=all+dates']

    
    def parse(self, response):
        
        # titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        # jobs = response.xpath('//div[@class="result-info"]')
        jobs = response.xpath('//h3[@class="result-heading"]')

        for job in jobs:
            title = job.xpath('a/text()').extract()
            address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            relative_url = job.xpath('a/@href').extract_first()
            # absolute_url = "https://newyork.craigslist.org" + relative_url
            absolute_url = response.urljoin(relative_url)


            yield{'URL':absolute_url, 'Title':title, 'Address':address}