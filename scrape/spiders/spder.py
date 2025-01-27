import random
import scrapy
import re

class QuotesSpider(scrapy.Spider):
    name = "amz"

    def __init__(self, domain = None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.urlx = domain.split(',')        
    
    def start_requests(self):

        for url in self.urlx:
            yield scrapy.Request(url=url, callback=self._parse)
        #yield scrapy.Request(url=self.urlx, callback=self._parse)

    def _parse(self, response):    
        total_ratings = response.css('span[data-hook="total-review-count"]::text').get(default='').strip()
        review = response.css('span[data-hook]::text').get()
        review_2 = response.css('i.a-icon-star')

        if not review:
            review = response.xpath(".//span[@class='a-icon-alt']/text()").get() or review_2.css('span.a-icon-alt::text').get()

        if not total_ratings:
            total_ratings = response.css('div[data-hook="cr-filter-info-review-rating-count"]::text').get().strip() or total_ratings
   

        yield {
            'total_rating' : total_ratings[:total_ratings.find(' ')],
            'review' : review[:review.find(' ')], #this works (also in production)
        }

