import bs4
import bs4.element
import socket
import urllib2
import  logging

log = logging.getLogger(__name__)


def get_file_text(path):
    with open(path, 'rt') as f:
        return f.read()


class UrlUtils:
    timeout = 30
    userAgent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:29.0) Gecko/20100101 Firefox/29.0"
    debugLevel = 0
    encoding = "utf-8"
    referer = ''

    # @staticmethod
    def save_attributes(self, file_path, tags_list, attr):
        assert isinstance(tags_list, list)
        if len(tags_list) == 0:
            return
        assert isinstance(tags_list[0], bs4.element.Tag)
        f = open(file_path, 'w')
        f.write("\n".join((l.get(attr) for l in tags_list)))
        f.close()

    # @staticmethod
    def save_hrefs(self, file_path, tags_list):
        return self.save_attributes(file_path, tags_list, 'href')

    def getPageBytes(self, url):
        h = urllib2.HTTPHandler(debuglevel=self.debugLevel)
        opener = urllib2.build_opener(h)

        # escape not safe symbols
        url = urllib2.quote(url, safe="%/:=&?~#+!$,;'@()*[]")
        print(url)

        request = urllib2.Request(url)
        request.add_header('User-Agent', self.userAgent)

        if self.referer:
            request.add_header("Referer", self.referer) # should add, as some sites check for referer to exists
        if self.debugLevel == 1:
            print u'trying to connect to "%s"' % url

        response = None
        try:
            response = opener.open(request, timeout=self.timeout)
        except urllib2.URLError, e:
            log.error("There was an error: %r" % e)
        except socket.timeout, e:
            log.error("Socket timeout: %r" % e)

        out = None
        if response:
            out = response.read()
            response.close()
        return out

    # return page in the specific encoding of self.encoding
    # @staticmethod
    def getPage(self, url, as_image=False):
        response = self.getPageBytes(url)
        return response.decode(self.encoding, 'ignore')
