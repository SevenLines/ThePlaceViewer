import logging
from core.utils import UrlUtils
import os

log = logging.getLogger(__name__)

base_url = 'http://www.theplace.ru'
settings_dir = 'settings'
photos = 'photos'
cache_dir = os.path.join('.', 'cache')
icons_cache_dir = os.path.join(cache_dir, 'icons')

utls = UrlUtils()
utls.referer = base_url
utls.encoding = 'cp1251'
