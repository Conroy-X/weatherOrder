# -*- coding:utf8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import time, localtime, strftime
import re
import string

resp=urlopen('http://www.weather.com.cn/weather/101280601.shtml')
soup=BeautifulSoup(resp,'html.parser')
tagDate=soup.find('ul', class_="t clearfix")
#dates=tagDate.h1.string

tagToday=soup.find('p', class_="tem")
try:
    temperatureHigh=tagToday.span.string
except AttributeError as e:
    temperatureHigh=tagToday.find_next('p', class_="tem").span.string

#temperatureHigh=tagToday.find_next('p', class_="tem").span.i.string
temperatureLow=tagToday.i.string
weather=soup.find('p', class_="wea").string
tagWind=soup.find('p',class_="win")
winL=tagWind.i.string

week = {'Monday':'周一','Tuesday':'周二','Wednesday':'周二','Thursday':'周四','Friday':'周五','Saturday':'周六','Sunday':'周日'}
time = strftime('%Y',localtime(time()))+ "年" + strftime('%m',localtime(time())) +'月'+ strftime('%d',localtime(time()))+'日'
temperature = temperatureHigh + '-' + temperatureLow.string

#赣州 101240701
#萍乡 101240901
#广州 101280101

# 短信应用SDK AppID
appid = 1400176631  # SDK AppID是1400开头
# 短信应用SDK AppKey
appkey = "9669fbeee70d8c94c6e89cd343cc5ce5"
# 需要发送短信的手机号码
phone_numbers = ["18370803126", "15579930901"]
# 短信模板ID，需要在短信应用中申请
template_id = 324912  # NOTE: 这里的模板ID`7839`只是一个示例，真实的模板ID需要在短信控制台中申请
# 签名
sms_sign = "张张张三"  # NOTE: 这里的签名"腾讯云"只是一个示例，真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`

from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError

result = ''
ssender = SmsSingleSender(appid, appkey)
#params = []
params = [weather,temperature]  # 当模板没有参数时，`params = []`
try:
    result = ssender.send_with_param(86, phone_numbers[0],
        template_id, params, sign=sms_sign, extend="", ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
except HTTPError as e:
    print(e)
except Exception as e:
    print(e)

print (strftime("%Y-%m-%d %H:%M:%S", localtime()))
print(result)
