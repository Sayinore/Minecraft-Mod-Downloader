import random
import urllib.request

from bs4 import BeautifulSoup as bs

import module.log as log
import module.lang

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
]


def mcbbs(url):
    trash = "见楼下帖子后面请看完本文伸手党在正提供"

    headers = {'User-Agent': random.choice(ua)}
    log.pro(_("Loading the MCBBS thread"))
    html = bs(urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read(), "html.parser")

    log.pro(_("Checking the MCBBS thread"))
    div = html.find_all("div", "typeoption")
    log.pro(_("Testing if it is a mod-posting thread"))
    if div:
        td = div[0].find_all("td")

        for i in td.pop().find_all("a"):
            link = i.get_text()
            for j in link:
                if j in trash:
                    return False
            return link

    return False
