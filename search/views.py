from django.http import HttpResponse
from django.shortcuts import render
import asyncio
from requests_html import AsyncHTMLSession
import subprocess
from scrape.spiders.spder import QuotesSpider

# Create your views here.


# def wo(url):
#     s = HTMLSession()
#     r = s.get(url)
#     r.html.render(sleep=1)


#     #This is our simple scraper, just copy xPath from inspect then paste it and follow this format
#     data = {
#         'total-ratings' : r.html.xpath('//*[@id="cm_cr-product_info"]/div/div[1]/div[3]/span', first=True).text,
#         'outof5' : r.html.xpath('//*[@id="cm_cr-product_info"]/div/div[1]/div[2]/div/div/div[2]/div/span', first=True).text
#     }

#     print(data)

# loop = asyncio.get_event_loop()

def home(request):
    is_true = False

    # if request.method == 'POST':
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)
        # rate_data = loop.run_until_complete(getRate('https://www.amazon.com/Jackson-Safety-Nemesis-22475-Anti-Fog/product-reviews/B008D81A0A/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'))
        # loop.close()
        # print(rate_data)

    if request.method == 'POST':
        post = request.POST
        print(request.POST)
        # print('type', type(jj))
        # url = {'urls' : 'hi'}
        # print('AFTER', QuotesSpider(url))

        #TODO: I need to make sure that the 'urls' is a LIST or something or create an if-else statement to see if its a list or not
        #MORE: I need the TEXTBOX in the HTML to GET BIGGER as the texts get inputted in

        urls = post['urls']
        url = urls.split(',')
        url = [i.strip() for i in url]
        print("DJANGO URL", urls, url)
        #url = ','.join(url)
        url_domains = ','.join(url)
        print('DJANGO POST', post, url_domains)
        is_true = True
        # if is_true:
        #     subprocess.call(['scrapy', 'crawl', 'amz', '-a', f'domain={url_domains}'])

        #this gets called quick, just make sure this gets called after an if statement and itll work out
        #subprocess.call(['scrapy', 'crawl', 'amz'])

    return render(request, 'search/page.html')
    # Use requests_html to scrape data from the response

    # Replace this with your actual scraping code
    # await main('https://www.amazon.com/Jackson-Safety-Nemesis-22475-Anti-Fog/product-reviews/B008D81A0A/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews')
  
    # return HttpResponse(f'Scraped data: hi')


# async def close_session():
#     await asyncio.sleep(0.25)  # Give asyncio tasks time to complete
#     await loop.shutdown_asyncgens()
#     loop.stop()

# # Register the close_session function to be called when the Django application exits
# loop.run_until_complete(loop.create_task(close_session()))