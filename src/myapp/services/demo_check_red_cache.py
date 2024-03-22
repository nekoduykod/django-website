'''
D:\Redis>redis-cli
ping   #PONG returned   -> Redis works (polling)
127.0.0.1:6379> keys *  -> returns cache
'''
import os
from django.core.cache import cache
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

settings.configure()

cache_key = ":0:views.decorators.cache.cache_header..cb1bd629b76dfafa7fca50901c60d267.en-us.UTC"
cached_data = cache.get(cache_key)
print(cached_data)