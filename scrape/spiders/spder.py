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
        'Accept-Language': 'en-US, en;q=0.5'
        }

        for url in self.urlx:
            yield scrapy.Request(url=url, headers=HEADERS, callback=self.parse)

    def parse(self, response):
        total_ratings = response.css('div[data-hook]::text').get().strip()
        review = response.css('span[data-hook]::text').get()

        yield {
            'total_rating' : total_ratings[:total_ratings.find(' ')],
            'review' : review[:review.find(' ')]
        }

  