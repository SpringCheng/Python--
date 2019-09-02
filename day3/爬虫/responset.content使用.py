import requests

# 获取改地址的内容存放在变量res中，res也是一个对象
res = requests.get('https://res.pandateacher.com/2018-12-18-10-43-07.png')
# 将对象内容以二进制数据形式返回给pic
pic = res.content
# 新建一个文件ppt.jpg，图片内容以二进制wb格式读写
photo = open('ppt.jpg', 'wb')
# 获取pic的二进制内容
photo.write(pic)
photo.close()
