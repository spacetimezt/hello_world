#coding=utf-8

import os

#递归
dirpath=raw_input('input  dir')

def getdir(dirpath,level=0):
    level+=2
    if not dirpath:
        dirpath=os.getcwd()
    mylist=os.listdir(dirpath)

    for name in mylist:
        print ('-'*level+'|'+name)
        name =os.path.join(dirpath,name)
        if os.path.isdir(name):
            getdir(name,level)

if __name__=='__main__':
    getdir(dirpath)


