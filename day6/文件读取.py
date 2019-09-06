"""
文件的读写
1、  a:追加模式
    r：read读取
    w：write写入
    wb：二进制方式打开一个文件用于写入
2、 with关键词的用法  避免打开文件后忘记关闭
    with open() as 变量名
3、readlines()  按行读取,但是会将一次性读取到的内容封装到一个列表中返回
    readline()  一次读一行
4、writelines() 按行写入



 -*- coding: UTF-8 -*-
@date: 2019/9/5 8:03 
@name: 文件读取.py
@author：Spring
"""


# 读取文件内容（打开，读取，关闭）
file1 = open(r'C:\Users\Mloong\Desktop\c.txt', 'r', encoding='utf-8')  # file1变量是存放读取到的文件数据的,file1对象代表这个文件
file_content = file1.read()  # 读取file1的内容返回到变量file_content里
print(file_content)
# file1.close()

# 写入文件   如果文件不存在，创建文件
file2 = open('a.txt', 'w', encoding='utf-8')
file2.write('张无忌\n')
file2.write('张翠山\n')
file2.close()

# 写入文件(追加模式)
file3 = open('a.txt', 'a', encoding='utf-8')
file3.write('赵敏')
file3.close()

# with关键词的使用
with open('a.txt', 'a', encoding='utf-8') as file4:
    file4.write('赵芷若\n')

#
with open('b.txt', 'r', encoding='utf-8') as file5:
    file5_content = file5.readlines()  # readlines()按行读取
    # print(file5_content)  # 得到的是一个列表['罗恩 23 35 44\n', '哈利 60 77 68 88 90\n', '赫敏 97 99 89 91 95 90\n', '马尔福 100 85 90']，每个元素都是字符串

    final_scores = []  # 新建一个空列表
    for i in file5_content:
        data = i.split()  # 把字符串切割成更细的字符串 ['罗恩', '23', '35', '44']...
        sum = 0
        # print(data)
        for score in data[1:]:
            sum = sum + int(score)
        result = data[0] + ' ' + str(sum) + '\n'
        # print(result)
        final_scores.append(result)
    print(final_scores)
with open('c.txt', 'w', encoding='utf-8') as file6:
    file6.writelines(final_scores)


# 读取大文件  (防止内存溢出)
file_name = ('d.txt')
try:
    with open(file_name, 'r', encoding='utf-8') as file_obj:
        # 定义一个变量保存文件的内容
        file_content = ''
        # 定义一个变量，来指定每次读取的大小
        chunk = 100
        # 创建一个循环来读取文件内容
        while True:
            content = file_obj.read(chunk)

            # 检查是否读到了内容
            if not content:
                print('文件读取完毕')
                break
            file_content += content
except FileNotFoundError:
    print(f'{file_name}这个文件不存在')
print(file_content)

# 读取二进制文件

file_name = (r'F:\音乐\暗杠 - 小桥.mp3')
with open(file_name,'rb') as file_obj:
    # print(file_obj.read(100))
    new_name='房东的猫.mp3'
    chunk = 1024 * 100

    with open(new_name,'ab') as new_obj:
        while True:

            # 从已有对象读取数据
            content=file_obj.read(chunk)
            if not content:
                break
            # 将读取到的数据写入到新对象中
            new_obj.write(content)
