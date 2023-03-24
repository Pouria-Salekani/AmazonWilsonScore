from django.http import HttpResponse
from django.shortcuts import render
import asyncio
from requests_html import AsyncHTMLSession
import subprocess
from scrape.spiders.spder import QuotesSpider

# Create your views here.

#fixes the url; makes it go to review page at amazon
def fix_url(urls):
    fixed_urls = []

    for u in urls:
        dp = u.find('dp')
        fixed_urls.append(u[:dp] + 'product-reviews' + u[dp+2:])

    return fixed_urls



def home(request):
    is_true = False

    if request.method == 'POST':
        post = request.POST
        print(request.POST)
       
        #TODO: I need to make sure that the 'urls' is a LIST or something or create an if-else statement to see if its a list or not
        #MORE: I need the TEXTBOX in the HTML to GET BIGGER as the texts get inputted in

        urls = post['urls']
        url = urls.split(',')
        url = [i.strip() for i in url]
        
        #fix the url
        fixed_urls = fix_url(url)
        print("DJANGO URL", urls, url)
        #url = ','.join(url)
        url_domains = ','.join(fixed_urls)
        print('DJANGO POST', post, url_domains)
        print('FIXED URL', fixed_urls)
        is_true = True
        # if is_true:
        #     subprocess.call(['scrapy', 'crawl', 'amz', '-a', f'domain={url_domains}'])

        #this gets called quick, just make sure this gets called after an if statement and itll work out
        #subprocess.call(['scrapy', 'crawl', 'amz'])

    return render(request, 'search/page.html')
 