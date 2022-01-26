
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import jieba
from bs4 import BeautifulSoup
from urllib.request import urlopen

from wordcloud import WordCloud

baseUrl = 'http://www.51bengou.com'


def getCover(articleUrl):
    global baseUrl
    html = urlopen(baseUrl+articleUrl).read().decode('utf-8', 'replace')
    bsObj = BeautifulSoup(html, 'lxml')
    try:
        # Find internal link of the cover.
        src = bsObj.find('span', {'class': 'cartoon-intro'}).find('img')['src']
        return src
    except AttributeError:
        return None


def getInfo(url):
    html = urlopen(url).read().decode('utf-8', 'replace')
    bsObj = BeautifulSoup(html, 'lxml')
    print(html)
    try:
        # Find all information.
        infos = bsObj.findAll('span', {'class': 'short'})
        items = {}
        # Store in a dict.
        for info in infos[:7]:
            items[info.span.text] = info.text
        return list(items)
    except AttributeError:
        return None

def wordAnalysis():
    f = open('../../../xsk.txt', 'r', encoding='utf-8')
    content = f.read()
    f.close()
    ls = jieba.lcut(content)
    txt = ' '.join(ls)
    w = WordCloud(font_path='../../fonts/simhei.ttf', width=1000, height=700, background_color='white')
    w.generate(txt)
    w.to_file('Movie.png')

if __name__ == "__main__":
    f = open('../../../xsk.txt', 'a', encoding='utf-8')
    j = 0
    for page in range(15):  # 豆瓣爬取多页评论需要验证。
        url = 'https://movie.douban.com/subject/1292052/comments?start=' + str(
            10 * page) + '&limit=20&sort=time&status=P'
        print('第%s页的评论:' % (page))
        print(url + '\n')
        for i in getInfo(url):
            f.write(str(j))
            f.write(i)
            print(j, i)
            j += 1
        time.sleep(10)
        print('\n')
wordAnalysis()
