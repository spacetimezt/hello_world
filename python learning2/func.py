#coding=utf-8
'''
author:dark_alex
time:2014/01/24
函数多参数
'''

def func(*a):
    print a

func(1,2,3,4,5,6)


def func2(**var):
    print var

func2(a=1,b=2,d=4)

def func3(*arg,**arg1):
    print arg
    print arg1

func3(1,2,3,4,a=1,b=3)
