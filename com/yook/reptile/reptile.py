from __future__ import print_function

import requests
import json
import re #正则匹配
import time #时间处理模块
import jieba #中文分词
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
import urllib3
from PIL import Image
from wordcloud import WordCloud  #绘制词云模块
import paddlehub as hub
import urllib.request
import http.cookiejar
from requests.cookies import RequestsCookieJar
from bs4 import BeautifulSoup
import random


import jieba  # 中文分词
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud  # 绘制词云模块


def getHtml(url):
    """获取url页面"""
    headers = {
        'Host': 'movie.douban.com',
        'Connection': 'keep-alive',
        'Content-Type': 'text/html; charset=utf8',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Dest': 'document',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'bid=WD6_t6hVqgM'
    }

    # req = urllib.request.Request(url,None, headers)
    # response = urllib.request.urlopen(req)
    # content = response.read().decode('gbk').encode('utf-8')
    # file = open("../source.html", 'a', encoding='utf-8')
    # file.write(content)
    # # print(content.decode("utf-8", 'ignore'))

    # request = urllib.request.Request(url, headers=headers)
    # request.add_header( 'Accept-encoding' , 'gzip' )
    # response = urllib.request.urlopen(request).read()
    # gzipped = response.headers.get('Content-Encoding')
    # if gzipped:
    #  content = zlib.decompress(response, 16 + zlib.MAX_WBITS)

    # request = urllib.request.Request(url,headers=headers)
    #
    # response = urllib.request.urlopen(request)
    # # fh = open("../../source.html", "wb")    # 将文件写入到当前目录中
    # # fh.write(response)
    # # fh.close()
    # content = response.read().decode('utf-8', 'ignore')
    rep = requests.get(url, headers=headers)
    print(rep.encoding)
    print(rep.apparent_encoding)
    html = rep.content
    doc = str(html, 'utf-8')
    return doc


def getComment(urlStr):
    # """解析HTML页面"""
    html = getHtml(urlStr)
    soupComment = BeautifulSoup(html, 'lxml')
    comments = soupComment.findAll(class_='short')
    comment_arr = []
    for comment in comments:
        comment_arr.append(comment.getText() + '\n')
    return comment_arr


def wordAnalysis():
    f = open('../../xsk.txt', 'r', encoding='utf-8')
    content = f.read()
    f.close()
    ls = jieba.lcut(content)
    txt = ' '.join(ls)
    w = WordCloud(font_path='../../fonts/simhei.ttf', width=1000, height=1000, background_color='white')
    w.generate(txt)
    w.to_file('../../xsk.png')


if __name__ == "__main__":
    f = open('../../xsk.txt', 'a', encoding='utf-8')
    j = 0
    for page in range(15):  # 豆瓣爬取多页评论需要验证。
        url = 'https://movie.douban.com/subject/1292052/comments?start=' + str(
            1 * page) + '&limit=1000&sort=time&status=P'
        print('第%s页的评论:' % (page))
        print(url + '\n')
        for i in getComment(url):
            f.write(str(j))
            f.write(i)
            print(j, i)
            j += 1
        time.sleep(10)
        print('\n')
wordAnalysis()
