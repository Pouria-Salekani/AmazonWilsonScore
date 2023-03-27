

from itemadapter import ItemAdapter
from search.models import Global_Rating

#This pipeline gets called automatically when we change the settings...
#this will save the items from the 'spder.py' *yield* into the DJANGO MODELS
#TODO: Since we want new data everytime, make sure to DELETE ALL before saving it


class ScrapePipeline(object):
    def process_item(self, item, spider):
        global_rating = Global_Rating(total_rating=item.get('total_rating'), stars=item.get('review'), whole_item=item)
        global_rating.save()
        return item
