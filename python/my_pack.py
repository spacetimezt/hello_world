#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
Author:Dark_ALex
Time:2018/01/30
Description:用来学习如何用struck来解包

'''

import struct

a=12.34

bytes=struct.pack('f',a)

print(bytes)

a,=struct.unpack('f',bytes)
print(a)

a=12
print(struct.pack('i',a))

a='hello'

b='world!'

c=2

d=45.123

bytes=struct.pack('5s6sif',a,b,c,d)
print(a,b,c,d)

'''
struct中支持的格式如下表：

  Format	C Type            	Python            	字节数
  x     	pad byte          	no value          	1
  c     	char              	string of length 1	1
  b     	signed char       	integer           	1
  B     	unsigned char     	integer           	1
  ?     	_Bool             	bool              	1
  h     	short             	integer           	2
  H     	unsigned short    	integer           	2
  i     	int               	integer           	4
  I     	unsigned int      	integer or long   	4
  l     	long              	integer           	4
  L     	unsigned long     	long              	4
  q     	long long         	long              	8
  Q     	unsigned long long	long              	8
  f     	float             	float             	4
  d     	double            	float             	8
  s     	char[]            	string            	1
  p     	char[]            	string            	1
  P     	void *            	long

注1.q和Q只在机器支持64位操作时有意义

注2.每个格式前可以有一个数字，表示个数

注3.s格式表示一定长度的字符串，4s表示长度为4的字符串，但是p表示的是pascal字符串

注4.P用来转换一个指针，其长度和机器字长相关

注5.最后一个可以用来表示指针类型的，占4个字节



为了同c中的结构体交换数据，还要考虑有的c或c++编译器使用了字节对齐，通常是以4个字节为单位的32位系统，故而struct根据本地机器字节顺序转换.可以用格式中的第一个字符来改变对齐方式.定义如下：

  Character	Byte order            	Size and alignment
  @        	native                	native            凑够4个字节
  =        	native                	standard        按原字节数
  <        	little-endian         	standard        按原字节数
  >        	big-endian            	standard       按原字节数
  !        	network (= big-endian)	standard       按原字节数

使用方法是放在fmt的第一个位置，就像'@5s6sif'

'''