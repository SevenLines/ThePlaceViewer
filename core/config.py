from collections import defaultdict
import os

from core.utils import UrlUtils


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


def save_config(d):
    assert isinstance(d, dict)
    d['config'] = {
        'save_dir': save_dir,
        'base_url': base_url,
        'encoding': utls.encoding,
    }


def load_config(d):
    global save_dir, base_url
    assert isinstance(d, dict)
    if not d.has_key('config'):
        return

    d['config'] = defaultdict(int, d['config'])
    save_dir = d['config']['save_dir']
    base_url = d['config']['base_url']
    utls.encoding = d['config']['encoding']