#!usr/bin/env python
#coding=utf8

import sys,os
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import urllib2,urllib
import cookielib
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from excelio import *

dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置userAgent
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true','--load-images=false','--disk-cache=true'],desired_capabilities=dcap)
driver.set_window_size(320,568)
#driver.maxmize_window() #设置全屏

class MyPhantomJS:
    url = 'https://ccclub.cmbchina.com/mca/MPreContract.aspx'

    def __init__(self):
        self.u_name = '口吴B'
        self.u_id = '310115198712035132'
        self.u_mobile = '13795322945'
        self.u_smscode = '12345' #验证码
        self.u_selpro = u'A 安徽省' #选择框 直辖市
        self.u_selcity = u'合肥市' #城市 sel
        self.u_selqu = u'瑶海区' #区
        self.u_address = u'瑶海区胜利路88号' #单位地址
        self.u_unitname = u'年年红搬家公司' #单位名称
        self.u_seledu = '4' #xueli
        self.u_selduty = '04' #duty

    def set(self,name,id,mobile,selpro,selcity,selqu,address,unitname,seledu,selduty):
        self.u_name = name
        self.u_id = str(int(id))
        self.u_mobile = str(int(mobile))
        self.u_selpro = selpro
        self.u_selqu = selqu
        self.u_selcity = selcity
        self.u_address = address
        self.u_unitname = unitname
        self.u_seledu = seledu
        self.u_selduty = selduty

    def readExcel(self,fileName):
        data = open_excel(fileName)
        table = data.sheets()[0]
        rows = table.nrows
        for r in range(0,rows):
            row = table.row_values(r)
            if row:
                dic = {
                    'name' : row[0],
                    'id' : row[1],
                    'mobile' : row[2],
                    'selpro' : row[3],
                    'selcity' : row[4],
                    'selqu' : row[5],
                    'address' : row[6],
                    'unitname' : row[7],
                    'seledu' : row[8],
                    'selduty' : row[9]
                }
                self.set(**dic)
                self.run()
                path = 'img/img' + str(r) + '.png'
                driver.save_screenshot(path)

    def run(self):
        try:
            driver.get(self.url)
            driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbName').send_keys(self.u_name.decode())
            driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbCardId').send_keys(self.u_id)
            driver.find_element_by_id('tbxMobile').send_keys(self.u_mobile)
            driver.find_element_by_id('tbxSMSCode').send_keys(self.u_smscode)
            Select(driver.find_element_by_id('selpro')).select_by_value(self.u_selpro)
            Select(driver.find_element_by_id('selcity')).select_by_value(self.u_selcity)
            Select(driver.find_element_by_id('selqu')).select_by_value(self.u_selqu)
            driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxAddrOther').send_keys(self.u_address)
            driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxUnitName').send_keys(self.u_unitname)
            Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_seledu')).select_by_value(self.u_seledu)
            Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_selDuty')).select_by_value(self.u_selduty)
            #print 'done'
        except Exception as e:
            print e
            os.system('killall -9 phantomjs')

def main():
    myweb = MyPhantomJS()
    #myweb.run()
    myweb.readExcel('./info.xlsx')
    #driver.save_screenshot('123.png')

def test():
    myweb = MyPhantomJS()
    for i in range(10):
        m = int(myweb.u_mobile) + 1
        myweb.u_mobile = str(m)
        myweb.run()
        path = 'img/img' + str(i) + '.png'
        driver.save_screenshot(path)

if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        main()
