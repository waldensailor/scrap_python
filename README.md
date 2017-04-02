#-*- coding:utf-8 -*-
import urllib.request, re

url = "http://movie.mtime.com/#"

def getHtml(Url):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    headers = {"User-Agent": user_agent}
    req = urllib.request.Request(url = Url, headers = headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    html = html.decode("utf-8")
    #print(html)
    return html
    pass

def getImage(html):
    #reg = r'(?<=src=")htt.*?\.jpg(?=" width)'
    reg = r'(?<=src=")htt.*?\.jpg(?=" size)'#匹配url1
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    print(imglist)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

html = getHtml(url)
getImage(html)
