import requests


def getHtml():
    url = "https://movie.douban.com/subject/1292052/comments?start=0&limit=20&sort=time&status=P"
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

    rep = requests.get(url, headers=headers)
    print(rep.encoding)
    print(rep.apparent_encoding)
    html = rep.content
    doc = str(html, 'utf-8')
    with open('demo.html', 'w',encoding='gb18030') as f:
        f.write(doc)
        f.close()
    print(doc)

if __name__ == "__main__":
    getHtml()
