"""

 -*- coding: UTF-8 -*-
@date: 2019/9/9 13:29 
@author：Spring
"""


class Person:
    name = 'swk'

    def say_hell0(self):
        print(self.name)


p1 = Person()
p2 = Person()
p1.name = 'zbj'
p2.name = 'shs'
p1.say_hell0()
p2.say_hell0()

# Person.say_hell0()
