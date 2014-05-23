#coding: utf-8
import bs4
import logging
import os
import re
import urlparse

from models.theplace import Celeb
from utils import *



# logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

base_url = 'http://www.theplace.ru'
settings_dir = 'settings'
photos = 'photos'

utls = UrlUtils()
utls.encoding = 'cp1251'


def get_alphas():
    global photos, base_url
    url = os.path.join(base_url, photos)
    html_text = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html_text)
    links = soup.find_all('a')
    return filter(lambda l: re.match("/photos/celebs.*", l.get("href")), links)


def get_alphas_local():
    global base_url
    with open(os.path.join(settings_dir, 'alphas_list.txt')) as f:
        for line in f:
            yield urlparse.urljoin(base_url, line.strip())


def get_pages(celeb):
    assert isinstance(celeb, Celeb)
    page = utls.getPage(celeb.url)
    soup = bs4.BeautifulSoup(page)
    tags = soup.select(".listalka.ltop a")
    max_page = 1
    for t in tags:
        if t.text.isnumeric():
            v = int(t.text)
            max_page = v if v > max_page else max_page
    out = []
    for i in xrange(1, max_page+1):
        v = "/photos/gallery.php?id={id}&page={page_id}".format(
            id=celeb.id,
            page_id=i,
        )
        out.append(urlparse.urljoin(base_url, v))
    return out


def get_celebs(save_to_file=False, save_to_db=False):
    '''
    возвращает список ссылок на всех знаменитостей
    '''
    alphas = list(get_alphas_local())
    links_list = []
    for a in alphas:
        page = utls.getPage(a)
        soup = bs4.BeautifulSoup(page)
        tags = soup.select(".m-box a.t")
        log.info("считываю :{0}".format(a))
        for x in tags:
            href = x.get('href').strip()
            href = urlparse.urljoin(base_url, os.path.join(photos, href))
            name = x.select(".name")[0].text.strip()
            if not name:
                print x

            try:
                links_list.append(u"{0}@{1}".format(href, name))
            except:
                log.error(u"ошибка: {0}".format(href))

    links_list = set(links_list)
    links_list = list(links_list)

    if save_to_db:
        Celeb.save_celebs_links_list_to_db(links_list)

    if save_to_file:
        f = open(os.path.join(settings_dir, 'celebs_list.txt'), 'w')
        # for line in links_list:
        # l = u"{0}\n".format(line)
        f.write(u'\n'.join(links_list).encode('utf8'))
        f.close()
    return links_list


def get_celebs_local():
    with open(os.path.join(settings_dir, 'celebs_list.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            c = line.decode('utf8')
            if c:
                yield c


pages = get_pages(Celeb.from_url(
    'http://www.theplace.ru/photos/Monica_Bellucci-mid213.html@Monica Bellucci'))
# get_celebs(save_to_file=True)
# Celeb.save_celebs_links_list_to_db(list(get_celebs_local()))