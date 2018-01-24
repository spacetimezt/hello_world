#coding=utf-8


def myLog(func):
    def fun(*args):
        print '*'*50
        func(*args)
        print '*' * 50
    return fun

def myFunc(fun):
    print '*' * 50
    fun()
    print '*' * 50



#myFunc(myPr)

def my_func2(func):
    def inner():
        print '*' * 50
        func()
        print '*' * 50
    return inner

@my_func2
def myPr():
    print 'angel!'


myPr()