"""

@date: 2019/9/10 10:16 
@author：Spring
"""


def fn():
    print("我是一个fn函数")


def add(a, b):
    r = a * b
    return r


# 用来对其他函数进行扩展，使其它函数可以在执行前打印开始执行，执行后打印执行结束
# 参数
#       old  要扩展的对象
def begin_end(old):
    # 创建一个新函数
    def new_function(*args, **kwargs):
        res = old(*args, **kwargs)
        print('函数结束')
        return res

    return new_function


f = begin_end(fn)
f2 = begin_end(add)
print(f2(12, 34))
print(f())


# 在定义函数时，可以通过@装饰器，来使用指定的装饰器，来装饰当前函数
# 可以同时为一个函数指定多个装饰器，这样函数将按照从内向外的顺序装饰
@begin_end
def say_hello():
    print('大家好')


say_hello()
