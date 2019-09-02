"""


 -*- coding: UTF-8 -*-
@date: 2019/8/31 15:47 
@name: requests库.py
"""

import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
print(type(res))