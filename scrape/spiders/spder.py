import random
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "amz"

    def __init__(self, domain = None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.urlx = domain.split(',')
        
    
    def start_requests(self):

    #     UA_STRINGS = [
    # "Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36\
    #     (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
    # "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36\
    #     (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
    # "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15\
    #     (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1"
    #     ]

        # HEADERS = {
        # 'User-Agent': random.choice(UA_STRINGS),
        # 'Accept-Language': 'en-US, en;q=0.5'
        # }

        meta = {
        'proxy': 'http://scraperapi:d41cdd3624ece20b9eaa69dd11776ae3@proxy-server.scraperapi.com:8001'
    }


        for url in self.urlx:
            yield scrapy.Request(url=url, callback=self.parse, meta=meta)

    def parse(self, response):
        total_ratings = response.css('div[data-hook]::text').get().strip()
        #total_ratings = response.css('div[data-hook]::text').get()
        review = response.css('span[data-hook]::text').get()
        test = response.css('div[data-hook="total-review-count"]::text').get().strip()

        print('SCRAPE CALL', test)

        yield {
            #'total_rating' : total_ratings[:total_ratings.find(' ')],
            'total_rating' : total_ratings,
            'review' : review[:review.find(' ')],
        }

  