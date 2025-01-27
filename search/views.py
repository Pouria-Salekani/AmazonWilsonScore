from django.shortcuts import render
import subprocess
from matplotlib.figure import Figure
import io
import base64
import numpy as np
from .models import Global_Rating, Bounds
import json
from django.views.decorators.csrf import csrf_exempt
from urllib.parse import urlparse, urlunparse



#def getdataset() from calc.py
def get_dataset():
    #this will determine how many 'Datasets' should be printed out based off of the 'dataset' length
    loaded = Bounds.objects.values('bounds')
    for d in loaded:
        if d['bounds']:
            data_set = json.loads(d['bounds'])

    legend = []

    for i in range(len(data_set)):
        legend.append('Dataset ' + str(i+1))

    return data_set, legend

#fixes the url; makes it go to review page at amazon
#THIS IS OUTDATED: 2025
# def fix_url(urls):
#     fixed_urls = []

#     for u in urls:
#         dp = u.find('dp')
#         fixed_urls.append(u[:dp] + 'product-reviews' + u[dp+2:])

#     return fixed_urls

#new method
def new_fix(url):
    parsed_url = urlparse(url)
    clean_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
    return clean_url.rstrip('/')


@csrf_exempt
def home(request):
    if request.method == 'POST':
        import calculate

        print('POSTY CALLED')

        #make sure to delete all models here previously so new ones get made
        Global_Rating.objects.all().delete()
        post = request.POST

        urls = post['urls']
        url = urls.split(',')
        url = [i.strip() for i in url]
        
        #fix the url --- OUTDATED
        # fixed_urls = fix_url(url)
        # url = ','.join(url)
        # url_domains = ','.join(fixed_urls)
        #print('URL DOMAIN ', url_domains)

        #new fix url
        urlc = [new_fix(u) for u in url]
        url_dom = ','.join(urlc)

        
        
        #makes it so certain stuff render out
        is_true = True

        if is_true:
            subprocess.call(['scrapy', 'crawl', 'amz', '-a', f'domain={url_dom}'])

        
        # #this does all the calculations
        calculate.make_data()


        #most of below is using Matplotlib to display datasets
        x = np.linspace(0, 10, 50)

        dataset, legend = get_dataset()
        

        #create a plot with one axis object
        fig = Figure()
        ax = fig.subplots()

        
        for lb, ub in dataset:
            ax.fill_between(x, lb, ub, alpha=0.2)
 
        #add labels and a legend
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Multiple Confidence Intervals')

        #below automatically updates as we increase the upper and lower-bound, pretty cool
        ax.legend(legend)


        #save the plot to a buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        buffer.seek(0)
        img = buffer.getvalue()
        graph = base64.b64encode(img)
        graph = graph.decode('utf-8')
        buffer.close()

        #clear the plot
        fig.clf()

       
        return render(request, 'search/page.html', {'is_true': is_true, 'graph':graph})
    else:
        is_true = False
        return render(request, 'search/page.html', {'is_true': is_true})
 

def more_info(request):
    data = Global_Rating.objects.values('whole_item')
    return render(request, 'search/info.html', {'data':data})