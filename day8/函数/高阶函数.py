l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def fn2(i):
    if i % 2 == 0:
        return True
    return False


def fn3(i):
    if i > 5:
        return True
    return False


def fn4(i):
    if i % 3 == 0:
        return True
    return False


# func参数可以为任意类型，故func为函数
def fn(func, lst):
    new_list = []
    for n in lst:
        if func(n):
            new_list.append(n)
    return new_list


print(fn(fn2, l))
print(list(filter(fn4,l)))

print(lambda a,b:a+b)

a=map(lambda i:i+1,l)
print(list(a))

l=['bb','ccc','dddddd','asdsdsdasdfa']
a='2343453453'
l=[1,'23','23234',23,456]
l.sort(key=int)
print(sorted(a,key=int))
print(l)