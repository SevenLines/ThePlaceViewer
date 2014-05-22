import logging
from core.utils import UrlUtils

log = logging.getLogger(__name__)

base_url = 'http://www.theplace.ru'
settings_dir = 'settings'
photos = 'photos'
icons_cache_dir = 'cache/icons'

utls = UrlUtils()
utls.referer = base_url
utls.encoding = 'cp1251'
