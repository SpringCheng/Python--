"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 15:55 
@author：Spring
"""


# class Rectangle:
#
#     def __init__(self, width, height):
#         self.__width = width
#         self.__height = height
#
#     def get_width(self):
#         return self.__width
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_height(self):
#         return self.__height
#
#     def set_height(self, height):
#         self.__height = height
#
#     # 面积
#     def get_area(self):
#         return self.__height * self.__width
#
#
# r = Rectangle(2, 12)
#
# r.set_height(4)
# r._Rectangle__width = 8
# print(r.get_width())
# print(r.get_area())


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    # 面积
    def get_area(self):
        return self.__height * self.__width


r = Rectangle(2, 12)

r.set_height(4)
r._Rectangle__width = 8
print(r.get_width())
print(r.get_area())
