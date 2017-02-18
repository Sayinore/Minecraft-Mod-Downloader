import random
import urllib.request

from bs4 import BeautifulSoup as bs

import module.log as log

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
]

# trash = ["\u5728", "\u4e0b", "\u9762", "\u89c1", "\u4f38", "\u8bf7", "\u5e16"]
trash = ["见", "下", "后", "帖", "请", "面", "伸", "在"]


def mcbbs(url):
    headers = {'User-Agent': random.choice(ua)}
    log.pro("Loading the MCBBS thread")
    html = bs(urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read(), "html.parser")

    log.pro("Checking the MCBBS thread")
    div = html.find_all("div", "typeoption")
    log.pro("Testing if it is a mod-posting thread")
    if div:
        td = div[0].find_all("td")

        for i in td.pop().find_all("a"):
            for j, l in zip(i.get_text(), trash):
                if not j == i:
                    link = i.get_text()
                    return link

    return False
