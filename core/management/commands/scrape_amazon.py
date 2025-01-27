#THIS IS USELESS

from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrape.spiders.spder import QuotesSpider

class Command(BaseCommand):
    help = "Scrape Amazon (example)"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())
        process.crawl(QuotesSpider)
        process.start()
