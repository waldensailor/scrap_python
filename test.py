#-*- coding:utf-8 -*-
#这是主项目
'''
author = churen Tyan
'''
import urllib.request, re

#定义url如果需要的话，更改
url = "http://movie.mtime.com/#"

'''
获取页面
'''
def getHtml(Url):
    #模拟成浏览器
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    headers = {"User-Agent": user_agent}
    #request请求
    req = urllib.request.Request(url = Url, headers = headers)
    #打开页面
    page = urllib.request.urlopen(req)
    html = page.read()
    #解码
    html = html.decode("utf-8")
    #print(html)
    return html

def getImage(html):
    #reg = r'(?<=src=")htt.*?\.jpg(?=" width)'
    reg = r'(?<=src=")htt.*?\.jpg(?=" size)'    #图片的url，匹配url1
    #用正则匹配到所有的图片url,写入列表
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    print(imglist)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

#第一步，获取页面
html = getHtml(url)
#第二部得到图片
getImage(html)

