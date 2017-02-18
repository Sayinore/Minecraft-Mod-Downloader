import random
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup as bs

import module.log as log

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14"
]


# Basic search
def bing(keyword, page):
    keyword = urllib.parse.quote(keyword)
    raw_url = "https://cn.bing.com/search?q=" + keyword
    headers = {'User-Agent': random.choice(ua)}
    result_count = page * 10 - 9

    url = raw_url + "&first=" + str(result_count)
    log.info("Searching with bing")
    html = bs(urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read(), "html.parser")
    raw_result = html.find_all("h2")

    text = []
    link = []
    for i in raw_result:
        result = i.find_all("a")

        for i in result:
            text.append(i.get_text())
            link.append(urllib.parse.unquote(i.get("href")))

    return text, link


def mcbbs(mod_name, game_version, page):
    result_text = []
    result_link = []
    keyword = mod_name + " site:www.mcbbs.net"
    headers = {'User-Agent': random.choice(ua)}

    log.info("Searching with mcbbs")
    text, link = bing(keyword, page)

    for i in link:
        num = link.index(i) + 1
        log.pro("Checking the search results of bing, " + str(num) + "/" + str(len(link)))
        log.info("Testing if they are from MCBBS")
        if i[0:20] == "http://www.mcbbs.net":
            html = bs(urllib.request.urlopen(urllib.request.Request(i, headers=headers)).read(), "html.parser")

            div = html.find_all("div", "typeoption")
            if div:
                for j in div:
                    td = j.find_all("td")
                    log.info("Testing if the MCBBS thread for the needed game version")
                    if td[5].get_text().find(game_version) > -1:
                        result_link.append(i)
                        result_text.append(text[result_link.index(i)])
                        log.info("Found " + str(len(result_link)) + " result(s)")

    return result_text, result_link
