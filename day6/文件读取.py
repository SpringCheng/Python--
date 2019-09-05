"""
文件的读写
1、  a:追加模式
    r：read读取
    w：write写入
    wb：二进制方式打开一个文件用于写入
2、 with关键词的用法  避免打开文件后忘记关闭
    with open() as 变量名
3、readlines()  按行读取
4、writelines() 按行写入



 -*- coding: UTF-8 -*-
@date: 2019/9/5 8:03 
@name: 文件读取.py
@author：Spring
"""
# 读取文件内容（打开，读取，关闭）
file1 = open(r'C:\Users\Mloong\Desktop\c.txt', 'r', encoding='utf-8')  # file1变量是存放读取到的文件数据的
file_content = file1.read()  # 读取file1的内容放到变量filecontent里
# print(file_content)
file1.close()

# 写入文件
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
