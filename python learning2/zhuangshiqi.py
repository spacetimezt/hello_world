#coding=utf-8

#装饰器：在函数运行时增加功能且不影响这个函数原有内容，还可以进行函数执行后的清理工作
#语法
'''
@func1
def func2():
    pass
装饰器做的事情就是func1(func2)，我们传递了一个函数对象到我们的装饰器里面然后先执行装饰器func1中的内容，然后再执行func2
'''

#普通装饰器

def func1(func):
    def add_func():
        print '这是我添加的功能'
        return func()
        # func 函数名
        # func（） 函数调用

    return add_func


@func1
def func2():
    print 'hello,angel!'

#func1装饰器函数
#func2被装饰的

func2()
#func1(func2)

var=func2()
print type(var)


#被装饰的函数带参数
def func1(func):
    def func2(a,b):
        a=10
        b=15
        return func(a,b)
    return func2


@func1
def func(x,y):
    print('this is a add func')
    print (x+y)

func(10,20)

#装饰器函数带参数
def __func(arg):
    '''
    __func装饰器函数的参数接收函数
    __func -> _func 接收我们装饰器函数的参数
    _func -> _func1 闭包函数 添加功能
    _func1
    '''

    def _func(func):

        def _func1():
            if arg=='good':
                print '出去玩'
            if arg=='bad':
                print '不出去玩'

            return func()
        return _func1
    return _func

@__func('bad')
def func():
    print ('bad day')

@__func('good')
def func1():
    print 'good day'

func()
func1()