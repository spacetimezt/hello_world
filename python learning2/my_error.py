#coding=utf-8

def func():
    raise Exception('this is an error')
    print 'go on'

try:
    func()
except Exception:
    print 'hello'

class MyError(Exception):
    pass

#自定义异常，就可以抛出Myerror了

def fuc2():
    raise MyError('error2')

fuc2()