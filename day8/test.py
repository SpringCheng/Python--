"""

@date: 2019/9/10 17:57 
@author：Spring
"""
import urllib
import urllib.parse
import urllib.request
import urllib.error
import urllib.robotparser

# 定义请求数据
url = "http://reg.haibian.com/login/ajax_login"
data = {}
data['loginname'] = 'student08@qq.com'
data['password'] = '111111'

# 对数据进行编码
data = urllib.parse.urlencode(data)
# 将数据和url进行连接
request = url + '?' + data
# 打开请求，获取对象
requestResponse = urllib.request.urlopen(request)
# 读取服务端返回数据
ResponseStr = requestResponse.read()
# 打印数据
print(ResponseStr)
