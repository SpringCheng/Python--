"""
字典的使用
key()方法的使用

 -*- coding: UTF-8 -*-
@date: 2019/9/4 22:23 
@name: 字典的使用.py
@author：Spring
"""
import copy
"""
# 创建字典的四种方式
a = {'name': 'spring', 'age': 26, 'gender': '男'}
b = dict(name='chun', age=20, gender='男')
c = dict({'name': 'cheng', 'age': 22, 'gender': '男'})
d = dict([('name', 'spring'), ('age', 30)])

# 查找项
# 方式1
a1 = a['name']
print(a1)
print(a['age'], a['gender'])

# 方式2
a2 = a.get('age')
print(a2)
print(a.get('se', 'NO'))  # get(key,[default])

# 插入
# 方法1   a[key]=value
a['job'] = 'engineer'

# 方法2   setdefault(key,[default])若key存在则获取对应的value值，若不存在，则添加value值并
# 返回默认值
# print(a.setdefault('name'))
# print(a.setdefault('key','不存在的key'))
# print(a)

# 方法3 update({其他的字典})
a.update({'love': 'None'})
print(a)

# 删除
# 方式1
del d['name']
print(d)

# 方式2
print(b)
b.popitem()
print(b)

# 方式3
print(c)
c.pop('name', '不存在')
print(c)

# 方式4
c.clear()
print(c)

# 修改
c['name'] = '平'
print(c)

# 浅复制copy() （浅复制会简单复制对象内部的值）
# 深复制deepcopy()

# 直接复制  原始值改变，被赋值的对象也会改变，都是指向同一个地址，id不变
a = [1, 2, 3, 4, [5, 6]]
aa = a
a.append(7)
a[4].append(9)
print(a)
print(aa)
print(id(a))
print(id(aa))

# 浅复制copy（）
b = [1, 2, 3, 4, [5, 6]]
bb = copy.copy(b)
b.append(7)
b[4].append(8)
print(b)
print(bb)
print(id(b))
print(id(bb))

# 深拷贝
b = [1, 2, 3, 4, [5, 6]]
bbb = copy.deepcopy(b)
b.append(7)
b[4].append(88)
print(b)
print(bbb)
print(id(b))
print(id(bbb))
"""
# 通用操作 ： len(),+,*,in/not in , max(),min(),index(),count()
# 遍历字典  (字典转换为列表)
a = {'name': 'spring', 'age': 26, 'gender': '男'}
print(a)
aa = a.keys()
for i in aa:
    print(i, a[i])
print(a.keys())
print(a.values())
print(a.items())
for a, b in a.items():  # 打印字典内容（key,value,key:value）
    print(a, ':', b)
