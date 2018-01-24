#coding=utf-8
'''
time:2018/01/24
author:dark_alex
推导式

[表达式 for value in 序列 if 过滤条件] 列表推导式   会产生一个新的列表
（）元祖同理


'''
mylist =[1,2,3,4,5]
myli2=(1,2,3,4)

newlist=[var*var for var in mylist if var!=3]
print newlist

mynew2=(var*var for var in mylist if var!=3)
print mynew2

print dir(mynew2)

print mynew2.next()


'''字典推导式'''

mydict={var:'a' for var in mylist}
print mydict
