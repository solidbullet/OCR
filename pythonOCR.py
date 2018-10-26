# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 20:52:37 2018

@author: Administrator
"""
import requests 
import base64 
import json
    
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=xxxxxx&client_secret=yyyyyyyy'#替换掉xxxx&yyyyyyyy
headers = {'Content-Type': 'application/json; charset=UTF-8'}

r = requests.get(url, headers=headers)
r=json.loads(r.text)



with open(r'C:\20181026220921.jpg','rb') as f:
    base64_data = base64.b64encode(f.read())
#    print(base64_data)


url_post = 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers?access_token=' + r['access_token']
headers_post = {'Content-Type': 'application/x-www-form-urlencoded'}
body_post = {"image_type": "BASE64", "image": base64_data, "group_id": "gropu001","user_id": "0001"}
response = requests.post(url_post, body_post, headers = headers_post)
print(response.text)