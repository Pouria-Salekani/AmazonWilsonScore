

from itemadapter import ItemAdapter
from search.models import Global_Rating


class ScrapePipeline(object):
    def process_item(self, item, spider):
        global_rating = Global_Rating(total_rating=item.get('total_rating'), stars=item.get('review'), whole_item=item)
        global_rating.save()
        return item
