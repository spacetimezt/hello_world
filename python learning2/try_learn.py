#coding=utf-8

try:
    a=1/0
except ZeroDivisionError:
    print '除数为零'

finally:
    print '一定做得'


try:
    fp=open('123.txt','wb')
except Exception,e:
    pass
    #捕获异常
else:
    print '创建文件'
    #没有错误
finally:
    print '读取错误'
    #最后一定执行

#字符串转列表

a=raw_input('list:')
a=eval(a)
tmp=list(a)
print tmp