# Scrapy settings for scrape project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html


#12 -> 19 is necessary if we wanna use the Django.models
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath('.')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()

BOT_NAME = "scrape"

SPIDER_MODULES = ["scrape.spiders"]
NEWSPIDER_MODULE = "scrape.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "scrape (+https://web-production-7886.up.railway.app)"

# Obey robots.txt rules
# ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

#Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "scrape.middlewares.ScrapeSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html


# SCRAPEOPS_API_KEY = '886a5359-bdd2-4d62-a8be-82b9b4b6fcce'
SCRAPEOPS_API_KEY = '886a5359-bdd2-4d62-a8be-82b9b4b6fcce'
# SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
# SCRAPEOPS_NUM_RESULTS = 100
# SCRAPEOPS_FAKE_HEADERS_ENABLED = True

SCRAPEOPS_PROXY_ENABLED = True #maybe turn back on later
# SCRAPEOPS_PROXY_SETTINGS = {'country': 'us', 'optimize_request': True}
SCRAPEOPS_PROXY_SETTINGS = {'country': 'us'}


DOWNLOADER_MIDDLEWARES = {
   # "scrape.middlewares.ScrapeDownloaderMiddleware": 543,
   # 'scrape.middlewares.ScrapeOpsFakeBrowserHeadersMiddleware': 400
   'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   "scrapy.extensions.telnet.TelnetConsole": None,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "scrape.pipelines.ScrapePipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# #The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# #The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# #The average number of requests Scrapy should be sending in parallel to
# #each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# #Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

#-------IMPORTANT-------
#to PREVENT THE 'django sync->async' error you MUST REMOVE THIS LINE BELOW
# TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEED_EXPORT_ENCODING = "utf-8"
