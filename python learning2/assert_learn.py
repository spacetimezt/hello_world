#coding=utf-8

try:
    assert 1==2
except:
    print 'hh'


#with ... as... 上下文管理语句
with open('1.txt','rb') as tmp_fp:
    data=tmp_fp.read()


