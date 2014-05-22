import os
import re

from config import *


class Image(object):
    url_to_icon = ''
    celeb = None

    def __init__(self, url_to_icon, celeb):
        self.url_to_icon = url_to_icon
        self.celeb = celeb

    @property
    def name(self):
        return self.url_to_icon.split('/')[-1]

    def update_cached(self):
        '''
        updates icon cache
        '''
        d = os.path.dirname(self.icon_cache_path)
        if not os.path.exists(d):
            os.makedirs(d)

        with open(self.icon_cache_path, 'w') as f:
            b = utls.getPageBytes(self.url_to_icon)
            f.write(b)
            f.close()

    @property
    def full_image_bytes(self):
        return utls.getPageBytes(self.full_image_url)

    @property
    def full_image_url(self):
        return re.sub("(.*)(_s)(\.\w{3,4})",
                      lambda m: "{0}{1}".format(m.group(1), m.group(3)),
                      self.url_to_icon)

    @property
    def icon(self):
        '''
        return cached version of icon image
        '''
        if not self.is_cached:
            self.update_cached()
        with open(self.icon_cache_path, mode='r') as f:
            return f.read()

    @property
    def is_cached(self):
        return os.path.exists(self.icon_cache_path)

    @property
    def icon_cache_path(self):
        return os.path.join(icons_cache_dir, str(self.celeb.id), self.name)

    def __repr__(self):
        # return urlparse.
        return "{0}: {1}".format(self.name, self.url_to_icon)