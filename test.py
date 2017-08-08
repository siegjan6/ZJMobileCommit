#!usr/bin/env python
#coding=utf8
import sys,os
import ConfigParser
reload(sys)
sys.setdefaultencoding('utf8')
import requests
import urllib2,urllib
import time
import cookielib
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from excelio import *

url = 'https://ccclub.cmbchina.com/mca/MPreContract.aspx'
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 ")
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true','--load-images=false','--disk-cache=true'],desired_capabilities=dcap)
driver.set_window_size(414,736)
driver.get(url)
driver.find_element_by_id("ckAgree").click()

driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbName').send_keys(u'iceking')
driver.find_element_by_id('ctl00_ContentPlaceHolder1_txbCardId').send_keys(u'310115198808162221')
driver.find_element_by_id('tbxMobile').send_keys(u'13524013266')
driver.find_element_by_id('tbxSMSCode').send_keys(u'123456')
Select(driver.find_element_by_id('selpro')).select_by_value(u'A 安徽省')
Select(driver.find_element_by_id('selcity')).select_by_value(u'合肥市')
Select(driver.find_element_by_id('selqu')).select_by_value(u'瑶海区')
driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxAddrOther').send_keys(u'深圳市南山区科技园南区R2-B')
driver.find_element_by_id('ctl00_ContentPlaceHolder1_tbxUnitName').send_keys(u'科技园')
Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_seledu')).select_by_value('4')
Select(driver.find_element_by_id('ctl00_ContentPlaceHolder1_selDuty')).select_by_value('04')



driver.find_element_by_id("ctl00_ContentPlaceHolder1_btnQuery").click()
time.sleep(3)  
print driver.find_element_by_xpath("//div[@id='errmsg']").text
driver.get(url)
driver.save_screenshot('123.png')
driver.quit()

'''
['',
'!请准确输入姓名，2-14个中文字符。',
'!请准确输入18位身份证号码。',
'!请准确输入11位手机号码。',
'!请准确输入短信验证码。',
'!请选择你所在城市',
'!请选择你所在城市的区',
'!请正确填写公司地址，5－24个字。',
'!请准确输入单位名称，2-24个字。',
'!请选择您的学历',
'!请选择您的职务'
]
'''
