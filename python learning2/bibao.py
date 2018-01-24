#coding=utf-8
#闭包：内部函数对外部函数作用域里变量的引用（非全局变量），则内部函数为闭包，闭包就是你调用了外部函数，外部函数返回内部函数。此时的内部函数叫做闭包函数，闭包在运行时可以有多个实例，不同的引用环境和相同的函数组合可以产生不同的实例


def wai():
    a=1
    def nei():
        print a
    return nei


#返回值为内部函数
func=wai()
func()

def func(num):

    def func1(num1):
        print (num+num1)
    return func1
var=func(10)
var(11)




mylist=[1,2,3,4,5]
def func2(obj):
    def func3():
        obj[0]+=1
        print obj
    return func3

var=func2(mylist)
#var保存了一个状态在内存，没有消失，等程序完成后才会消失
var()
var()
var()

#闭包私有化了变量，原来需要类对象完成的工作，闭包也可以完成
#由于闭包引用了外部函数的局部变量，则外部函数的局部变量没有及时释放，消耗内存
#在python中，使用闭包的另一个场景就是装饰器，也叫语法糖@
