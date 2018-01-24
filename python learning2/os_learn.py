#coding=utf-8
#试试
import os

#运行目录：执行程序的路径

#工作目录，可更改
path=os.getcwd()
print path

print os.name

#列出文件
lsdir=os.listdir(path)
print lsdir

#删除文件
#d=os.remove('./2')

#删除文件夹
#c=os.rmdir('./3')

print dir(os)

#递归创建
#os.makedirs('./a/c/d')

#调用系统命令
print os.system('tree')

#path
print os.path

print '*'*50
#绝对路径
print os.path.abspath('a/ss')
print '*'*50

#分割文件路径

print os.path.split('./a/1.txt')

#文件名
print os.path.basename('../a/f/e.txt')

#文件存在
print os.path.exists('./a')
print '*'*50

#文件名拼接
print os.path.join('../a/f','jj.txt')


#是否文件，文件夹
print os.path.isdir('./f')
print os.path.isfile('./1')

#文件大小
print os.path.getsize('./1')

#改变工作目录
os.chdir('../')
print os.getcwd()
fp=open('./myapp.log','r')
data=fp.read()
print data