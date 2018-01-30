#coding=utf-8

class A:
    #类的变量，可以通过类访问
    num=1

a=A()
b=A()

print a.num

a.num=2
print a.num
print b.num

A.num=5
print a.num
print b.num

a.age=1
print a.age
print '*'*50
#构造函数

class A:
    def __init__(self):
        #这个num是实例化才有
        self.num=1


a=A()
print a.num

help(classmethod)