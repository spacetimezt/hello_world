# 这是我的scapy学习笔记

## Scapy的安装

在Windows下安装Scapy是一件痛苦的事情，而且安装成功后，运行的时候也会显示乱码。而在Linux下，安装Scapy会非常的简单。在这里介绍一下在CentOS下的Scapy安装。

+ 安装Python
> yum install python
+ 安装unzip
> yum install unzip
+ 安装setuptools
```
wget https://pypi.python.org/packages/07/a0/11d3d76df54b9701c0f7bf23ea9b00c61c5e14eb7962bb29aed866a5844e/setuptools-36.2.7.zip#md5=b9e6c049617bac0f9e908a41ab4a29ac
unzip setuptools-36.2.7.zip 
cd setuptools-36.2.7
python setup.py install
```
+ 安装Scapy
> easy_install scapy