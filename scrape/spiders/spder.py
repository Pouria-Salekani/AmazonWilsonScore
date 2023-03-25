import random
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "amz"

    def __init__(self, domain = None, *args, **kwargs):
        super(QuotesSpider, self).__init__(*args, **kwargs)
        self.urlx = domain.split(',')
        #print("THE URL", self.urlx)
        #self.urlx = ['https://www.amazon.com/Jackson-Safety-Nemesis-22475-Anti-Fog/product-reviews/B008D81A0A/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews']

    
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

        # urls = ['https://www.amazon.com/Jackson-Safety-Nemesis-22475-Anti-Fog/product-reviews/B008D81A0A/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews',
        #         'https://www.amazon.com/Daisy-Jones-Taylor-Jenkins-Reid/product-reviews/1524798649/?_encoding=UTF8&pd_rd_w=NCCGT&content-id=amzn1.sym.64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_p=64be5821-f651-4b0b-8dd3-4f9b884f10e5&pf_rd_r=P0CSWMGQD4WBNFV20N16&pd_rd_wg=gfa1J&pd_rd_r=db04e1dc-4f1e-485a-9c91-cd7d3090de03&ref_=pd_gw_crs_zg_bs_283155'
        # ]

        for url in self.urlx:
            yield scrapy.Request(url=url, headers=HEADERS, callback=self.parse)

    def parse(self, response):
        total_ratings = response.css('div[data-hook]::text').get().strip()
        review = response.css('span[data-hook]::text').get()

        yield {
            'total_rating' : review[:review.find(' ')],
            'review' : total_ratings[:total_ratings.find(' ')]
        }

  