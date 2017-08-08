#encoding=utf8
import urllib2
from bs4 import BeautifulSoup
import urllib
import socket

#User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
User_Agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
header = {}
header['User-Agent'] = User_Agent

'''
获取所有代理IP地址
'''


def getProxy(url):
    proxys = []
    req = urllib2.Request(url,headers=header)
    res = urllib2.urlopen(req).read()
    print res
    soup = BeautifulSoup(res)
    ips = soup.findAll('tr')
    print ips
    for x in range(1,len(ips)):
        ip = ips[x]
        tds = ip.findAll("td")
        ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]
        proxys.append(ip_temp)
    return proxys


def getProxyIp():
    proxy = []
    for i in range(1,2):
        url = 'http://www.kuaidaili.com/free/inha/'+str(i)
        print url
        page_ips = getProxy(url)
        proxy.append(page_ips)
    return proxy

'''
验证获得的代理IP地址是否可用
'''
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
            print 'errip  ' + proxy[i]
            continue
    f.close()


if __name__ == '__main__':
    proxy = getProxyIp()
    #validateIp(proxy)
