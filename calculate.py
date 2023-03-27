
import cmath
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()


from search.models import Global_Rating, Bounds
#we will eventually have MULTIPLE of these...
#first. have a LIST that have A HASHMAP ON EVERY INDEX
#have a function that goes thru the list and computes the results and returns it
#since it can have mulitple pts, it returns the value and res_list() will append it
#then go thru the res list and print to matlib

#need to return the data eventually so everything here needs to be in a django folder
#it would returns lower-bounds list and upper-bound list

jim = [{'whole_item': {}}, {'whole_item': {'review': '4.7', 'total_rating': '6,727'}}, {'whole_item': {'review': '4.1', 'total_rating': '1,212'}},
       {'whole_item': {'review': '3.1', 'total_rating': '12,212'}}]

data_set = []

def wilson_score(total_rating, review):
    #Amazon reviews are always out of 5
    constant = 5

    #sample size is total ratings
    n = int(total_rating.replace(',', ''))

    #p-hat or success is # of POSITIVE reviews; 
    x = float(review) / constant
    p = x

    print(n, x, p)


    z = 1.96 #uses a standard z-score of 95%
    deno = 1 + z**2/n
    nume = p + z**2/(2*n)

    deviation = cmath.sqrt((p*(1-p) / n) + (z**2 / (4*(n**2))))


    upper_bound = ((nume / deno) + ((z / deno) * deviation)) * 100
    lower_bound = ((nume / deno) - ((z / deno) * deviation)) * 100

    #rounding the numbers
    upper = round(upper_bound.real, 2)
    lower = round(lower_bound.real, 2)

    data_set.append([lower, upper])


def make_data():
    import search.views
    
    #when a new data is called, clear the old ones
    data_set.clear()
    Bounds.objects.all().delete()
    
    data = Global_Rating.objects.values('whole_item')
    print('data', data)
    for d in data:
        if d['whole_item']:
            print('rating',d['whole_item']['total_rating'])
            print('reveiw',d['whole_item']['review'])
            wilson_score(d['whole_item']['total_rating'], d['whole_item']['review'])

    data_set_json = json.dumps(data_set)
    model = Bounds(bounds=data_set_json) #saves lower and upper bound info in models
    model.save()

    #gets the dataset and uses matplotlib to show the results
    search.views.get_dataset()

    #MAKE A DATABASE SO WE CAN SEND THE LOWER AND UPPER BOUNDS
    #store it inside of the json database; then derserialize it (load it) back in 'views'
            
