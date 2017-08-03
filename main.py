#!usr/bin/env python
#coding=utf8

import sys
reload(sys)  
sys.setdefaultencoding('utf8')
import requests
import urllib2,urllib
import cookielib
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select

url = 'https://ccclub.cmbchina.com/mca/MPreContract.aspx'
u_name = '口天吴'
u_id = '310115198712035132'
u_mobile = '13524013266'
u_smscode = '12345' #验证码
u_selpro = '' #选择框 直辖市
u_selcity = '' #城市 sel
u_selqu = '' #区
u_address = 'address255room' #单位地址
u_unitname = 'caobi' #单位名称

dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置userAgent
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true','--load-images=false','--disk-cache=true'],desired_capabilities=dcap)
#driver.maxmize_window() #设置全屏
driver.set_window_size(320,568)

def main(cur_url):
    try:
        driver.get(cur_url)
        content = driver.page_source
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbName').send_keys(u_name.decode())
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbCardId').send_keys(u_id)
        driver.find_element_by_id('tbxMobile').send_keys(u_mobile)
        driver.find_element_by_id('tbxSMSCode').send_keys(u_smscode)
	Select(driver.find_element_by_id('selpro')).select_by_index(1)
        Select(driver.find_element_by_id('selcity')).select_by_index(1)
        Select(driver.find_element_by_id('selqu')).select_by_index(1)
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxAddrOther').send_keys(u_address)
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxUnitName').send_keys(u_unitname)
        Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_seledu')).select_by_index(1)
        Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_selDuty')).select_by_index(1)
	driver.save_screenshot('123.png')
        driver.close()
	print 'done'
    except Exception as e:
        print e

if __name__ == '__main__':
        main(url)
