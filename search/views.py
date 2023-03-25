from django.shortcuts import render
import subprocess

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
       #

        urls = post['urls']
        url = urls.split(',')
        url = [i.strip() for i in url]
        
        #fix the url
        fixed_urls = fix_url(url)
        print("DJANGO URL", urls, url)
        url = ','.join(url)
        url_domains = ','.join(fixed_urls)
        print('DJANGO POST', post, url_domains)
        print('FIXED URL', fixed_urls)
        is_true = True
        if is_true:
            subprocess.call(['scrapy', 'crawl', 'amz', '-a', f'domain={url_domains}'])

        #this gets called quick, just make sure this gets called after an if statement and itll work out
        #subprocess.call(['scrapy', 'crawl', 'amz'])

        #TODO: after calling Scrapy and it returning the stuff
        #we need to store it inside of the Model database
        #then use the calculate.py to calculate the stuff
        #then use matolib to plot the points
        #then to recommend which is better


    return render(request, 'search/page.html')
 