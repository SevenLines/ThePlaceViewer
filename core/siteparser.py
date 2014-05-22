#coding: utf-8
import bs4
import os
import re
from sqlalchemy.orm.session import _SessionClassMethods, sessionmaker, Session
import urlparse

from config import *
from core.image import Image
from models.theplace import Celeb, engine
from utils import *


def get_photos_url(url_without_photos):
    return urlparse.urljoin(base_url, os.path.join(photos, url_without_photos))


def get_alphas_urls():
    global photos, base_url
    url = os.path.join(base_url, photos)
    html_text = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(html_text)
    links = soup.find_all('a')
    links = filter(lambda l: re.match("/photos/celebs.*", l.get("href")), links)
    return list(map(lambda l: urlparse.urljoin(base_url, l.get("href")), links))


def get_alphas_local():
    global base_url
    with open(os.path.join(settings_dir, 'alphas_list.txt')) as f:
        for line in f:
            yield urlparse.urljoin(base_url, line.strip())

def get_page_url(the_place_id, page_num):
    url = u"/photos/gallery.php?id={id}&page={page_id}".format(
            id=the_place_id,
            page_id=page_num,
        )
    return urlparse.urljoin(base_url, url)

def get_pages_count(celeb):
    '''
    return pages count for celeb
    '''
    # assert isinstance(celeb, Celeb)
    page = utls.getPage(celeb.url)
    soup = bs4.BeautifulSoup(page)
    # get paginator tags
    tags = soup.select(".listalka.ltop a")
    max_page = 1 # at leas one page should be
    for t in tags:
        if t.text.isnumeric():
            v = int(t.text)
            max_page = v if v > max_page else max_page
    return max_page


def get_icons(celebs_page):
    assert isinstance(celebs_page, unicode)
    page = utls.getPage(celebs_page)
    soup = bs4.BeautifulSoup(page)
    tags = soup.select('.pic_box img.pic')
    for t in tags:
        t = get_photos_url(t.get('src'))
        icon = Image(t)
        yield icon, len(tags)


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
            href = get_photos_url(href)
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


def get_celebs_for_alpha(alpha_page_url):
    page = utls.getPage(alpha_page_url)
    soup = bs4.BeautifulSoup(page)
    tags = soup.select(".m-box a.t")
    log.info("считываю :{0}".format(alpha_page_url))
    for x in tags:
        href = x.get('href').strip()
        href = get_photos_url(href)
        name = x.select(".name")[0].text.strip()
        if not name:
            print x
        yield u"{0}@{1}".format(href, name)



def get_celebs_local():
    with open(os.path.join(settings_dir, 'celebs_list.txt'), 'r') as f:
        for line in f:
            line = line.strip()
            c = line.decode('utf8')
            if c:
                yield c

