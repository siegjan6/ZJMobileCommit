#coding=utf-8
import execjs
import re
import requests
from bs4 import BeautifulSoup
import urllib,urllib2
import socket

url = "http://www.kuaidaili.com/proxylist/1/"

HERDERS = {
    "Host": "www.kuaidaili.com",
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
}


def executejs(html):
    # 提取其中的JS加密函数
    js_string = ''.join(re.findall(r'(function .*?)</script>',html))

    # 提取其中执行JS函数的参数
    js_func_arg = re.findall(r'setTimeout\(\"\D+\((\d+)\)\"', html)[0]
    js_func_name = re.findall(r'function (\w+)',js_string)[0]

    # 修改JS函数，使其返回Cookie内容
    js_string = js_string.replace('eval("qo=eval;qo(po);")', 'return po')

    func = execjs.compile(js_string)
    return func.call(js_func_name,js_func_arg)

def parse_cookie(string):
    string = string.replace("document.cookie='", "")
    clearance = string.split(';')[0]
    return {clearance.split('=')[0]: clearance.split('=')[1]}

def getUrlIps(url):
    proxys = []
    # 第一次访问获取动态加密的JS
    first_html = requests.get(url=url,headers=HERDERS).content.decode('utf-8')
    # 执行JS获取Cookie
    cookie_str = executejs(first_html)
    # 将Cookie转换为字典格式
    cookie = parse_cookie(cookie_str)
    # 带上cookies参数，再次请求
    response = requests.get(url=url,headers=HERDERS,cookies=cookie)
    res = response.text
    soup = BeautifulSoup(res)
    ips = soup.findAll('tr')
    for x in range(1,len(ips)):
        ip = ips[x]
        tds = ip.findAll("td")
        if len(tds) > 0 and tds[0]['data-title'] == 'IP':
            ip_temp = tds[0].contents[0]+"\t"+tds[1].contents[0]
            proxys.append(ip_temp)
    return proxys

def validateIp(proxy):
    url = "http://ip.chinaz.com/getip.aspx"
    f = open("./ip.txt","w")
    socket.setdefaulttimeout(3)
    for i in range(0,len(proxy)):
        try:
            ip = proxy[i].strip().split("\t")
            proxy_host = "http://"+ip[0]+":"+ip[1]
            proxy_temp = {"http":proxy_host}
            res = urllib.urlopen(url,proxies=proxy_temp).read()
            f.write(proxy[i]+'\n')
            print proxy[i]
        except Exception,e:
            continue
    f.close()

def getProxyIp():
    proxy = []
    for i in range(1,3):
        url = 'http://www.kuaidaili.com/free/inha/'+str(i)
        print url
        page_ips = getUrlIps(url)
        proxy = proxy + page_ips
    return proxy

proxys = getProxyIp()
validateIp(proxys)
