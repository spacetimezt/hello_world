#coding=utf-8
#time:1/22
#用来学习如何将数据二进制的形式保存在 电脑中，包括变量的类型等信息
import pickle
print dir(pickle)
mylist=[1,2,3,4]
obj=pickle.dumps(mylist)
print obj

var=pickle.loads(obj)
print var

#dump存到文件
myfile=open('tmp','wb+')
pickle.dump(mylist,myfile)

myfile.close()
#load读取
myfp=open('./tmp','rb')
var=pickle.load(myfp)
print var