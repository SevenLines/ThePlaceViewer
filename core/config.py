import logging
from core.utils import UrlUtils
import os



base_url = 'http://www.theplace.ru'
settings_dir = 'settings'
photos = 'photos'
cache_dir = os.path.join('.', 'cache')
save_dir = 'output'
icons_cache_dir = os.path.join(cache_dir, 'icons')

rows_count = 3
columns_count = 3

utls = UrlUtils()
utls.referer = base_url
utls.encoding = 'cp1251'
