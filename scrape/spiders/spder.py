import random
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "amz"

    def __init__(self, domain = None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.urlx = domain.split(',')
        
    
    def start_requests(self):

        UA_STRINGS = [
    "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36\
        (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36\
        (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15\
        (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"
        ]

        HEADERS = {
        'User-Agent': random.choice(UA_STRINGS),
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5',
        'Accept-Encoding' : 'gzip', 
        'DNT' : '1', # Do Not Track Request Header 
        'Connection' : 'close'
        }

        meta = {
        'proxy': 'http://scraperapi.render=true:12a3151ea7f55828a0ce30dfc59895e8@proxy-server.scraperapi.com:8001'
    }


        for url in self.urlx:
            yield scrapy.Request(url=url, headers=HEADERS, callback=self.parse, meta=meta)

    def parse(self, response):
        total_ratings = response.css('div[data-hook]::text').get().strip()
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

