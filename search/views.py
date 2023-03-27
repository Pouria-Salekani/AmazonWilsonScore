from django.shortcuts import render
import subprocess
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import io
import base64
import numpy as np
from .models import Global_Rating, Bounds
import json
# from calculate import make_data

# Create your views here.
#def getdataset() from calc.py
def get_dataset():
    #this will determine how many 'Datasets' should be printed out based off of the 'dataset' length
    loaded = Bounds.objects.values('bounds')
    for d in loaded:
        if d['bounds']:
            data_set = json.loads(d['bounds'])

    legend = []
    print('DATA SETTTTT', data_set)

    for i in range(len(data_set)):
        legend.append('Dataset ' + str(i+1))

    return data_set, legend

#fixes the url; makes it go to review page at amazon
def fix_url(urls):
    fixed_urls = []

    for u in urls:
        dp = u.find('dp')
        fixed_urls.append(u[:dp] + 'product-reviews' + u[dp+2:])

    return fixed_urls



def home(request):
    #is_true = False

    if request.method == 'POST':
        import calculate
        #make sure to delete all models here previously so new ones get made
        Global_Rating.objects.all().delete()
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

        #-----call the calc thing here-----
        calculate.make_data()



        #the perfect one
        x = np.linspace(0, 10, 50)

        dataset, legend = get_dataset()
        

        # Create a plot with one axis object
        fig = Figure()
        ax = fig.subplots()

        #UPDATED, since our dataset is UPDATED to a 2D LIST, remove zip
        # Plot each dataset's confidence interval
        for lb, ub in dataset:
            ax.fill_between(x, lb, ub, alpha=0.2)
 
        #I gotta make a loop that checks how many values of either of the bounds are then make the apprpirate datasets
        leg = ['Dataset 1', 'Dataset 2', 'Dataset 3']

        # Add labels and a legend
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Multiple Confidence Intervals')
        #below automatically updates as we increase the upper and lower-bound, pretty cool
        ax.legend(legend)

        #plt.show()

        # save the plot to a buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        buffer.seek(0)
        img = buffer.getvalue()
        graph = base64.b64encode(img)
        graph = graph.decode('utf-8')
        buffer.close()

        # clear the plot
        #plt.clf()
        fig.clf()

        # #pass the plot image to the template
        # plot_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        # 3context = {'plot_image': plot_image}
        # if is_true:
        #     subprocess.call(['scrapy', 'crawl', 'amz', '-a', f'domain={url_domains}'])

        #-----call the calc thing here-----

        #this gets called quick, just make sure this gets called after an if statement and itll work out
        #subprocess.call(['scrapy', 'crawl', 'amz'])

        #TODO: after calling Scrapy and it returning the stuff -done
        #we need to store it inside of the Model database -done
        #then use the calculate.py to calculate the stuff -done
        #then use matolib to plot the points -done
        #add a refresh/remove button that removes the previous stuff - done
        #make sure matplotlib can plot MULTIPLE points -done
        #show the points on the screen using the matplotlib -done 
        #then to recommend which is better
        return render(request, 'search/page.html', {'is_true': is_true, 'graph': graph})
    else:
        is_true = True
        x = np.linspace(0, 10, 50)
        fig = Figure()
        ax = fig.subplots()

        #UPDATED, since our dataset is UPDATED to a 2D LIST, remove zip
        # Plot each dataset's confidence interval
        dataset = [[88, 90], [92, 96]]

        for lb, ub in dataset:
            ax.fill_between(x, lb, ub, alpha=0.2)
 
        #I gotta make a loop that checks how many values of either of the bounds are then make the apprpirate datasets
        leg = ['Dataset 1', 'Dataset 2', 'Dataset 3']

        # Add labels and a legend
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Multiple Confidence Intervals')
        #below automatically updates as we increase the upper and lower-bound, pretty cool
        ax.legend(leg)

        #plt.show()

        # save the plot to a buffer
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png')
        buffer.seek(0)
        img = buffer.getvalue()
        graph = base64.b64encode(img)
        graph = graph.decode('utf-8')
        buffer.close()

        # clear the plot
        #plt.clf()
        fig.clf()

        return render(request, 'search/page.html', {'is_true': is_true, 'graph':graph})
 