"""


 -*- coding: UTF-8 -*-
@date: 2019/9/3 13:51 
@name: demo.py
@author：Spring
"""

from bs4 import BeautifulSoup

bs = BeautifulSoup('<p><a>我是标签一</a><a>我是标签二</a></p>','html.parser')
tag = bs.find('p')
print(tag.text)
