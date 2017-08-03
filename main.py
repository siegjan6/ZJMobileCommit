#!usr/bin/env python
#coding=utf8

import sys
import requests
import urllib2,urllib
import cookielib
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = 'https://ccclub.cmbchina.com/mca/MPreContract.aspx'
u_name = '口天吴'
u_id = '310115198712035132'
u_smscode = '12345' #验证码
u_selpro = '' #选择框 直辖市
u_selcity = '' #城市 sel
u_selqu = '' #区
u_address = '' #单位地址
u_unitname = '' #单位名称

dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置userAgent
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true','--load-images=false','--disk-cache=true'],desired_capabilities=dcap)
#driver.maxmize_window() #设置全屏
driver.set_window_size(320,568)

def main(cur_url):
    try:
        driver.get(cur_url)
        content = driver.page_source
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbName').send_keys(u_name)
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbCardId').send_keys(u_id)
        driver.find_element_by_id('tbxMobile').send_keys(u_mobile)
        driver.find_element_by_id('tbxSMSCode').send_keys(u_smscode)
        #driver.find_element_by_id('selpro').options[1].selected = true
        #driver.find_element_by_id('selcity')
        #driver.find_element_by_id('selqu')
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxAddrOther').send_keys(u_address)
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxUnitName').send_keys(u_unitname)
        #driver.find_element_by_id('ctl00_ContentPlaceHolder1_seledu')
        #driver.find_element_by_id('ctl00_ContentPlaceHolder1_selDuty')
        driver.close()
    except Exception as e:
        print e

if __name__ == '__main__':
        main(url)
