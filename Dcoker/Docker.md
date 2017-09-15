# 这是我的Docker学习笔记

这是学习的[网站](http://www.runoob.com/docker/docker-tutorial.html)

## 简介
Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从Apache2.0协议开源。
Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。
容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。

image相当于类

container相当于类实例化产生的对象

每个container都是image产生的
![](https://github.com/spacetimezt/hello_world/blob/master/Dcoker/Docker%E6%9E%B6%E6%9E%84.png)
## 安装
### CentOs下的安装
> yum -y install docker

## 使用
- 启动docker服务
> service docker start

- 运行一个容器

通过docker的两个参数 -i -t，让docker运行的容器实现"对话"的能力,-d 代表后台执行，-P 将容器内部使用的网络端口映射到我们使用的主机上。
> docker run -i -t ubuntu:15.10 /bin/bash
> docker run -d -P training/webapp python app.py

- 查看现在运行的容器
> docker ps

- 查看已有镜像
> docker images

- 查找image
> docker search ***

- 下载image
> docker pull ***

- 停止容器,***代表CONTAINER ID
> docker stop ***

- WEB 应用容器
> docker run -d -p 5000:5000 training/webapp python app.py

## 创建镜像

- 更新镜像
我们可以通过更新镜像的方式来创建一个镜像。

更新镜像之前，我们需要使用镜像来创建一个容器。
```
root@local:~$ docker run -t -i ubuntu:15.10 /bin/bash
root@e218edb10161:/# 
```
然后可以对容器进行各种需要的操作

此时ID为e218edb10161的容器，是按我们的需求更改的容器。我们可以通过命令 docker commit来提交容器副本。

其中：v2代表TAG，可以在以后创建容器的时候使用

```
root@local:~$ docker commit -m="has update" -a="Dark" e218edb10161 runoob/ubuntu:v2
sha256:70bf1840fd7c0d2d8ef0a42a817eb29f854c1af8f7c59fc03ac7bdee9545aff8
-m:提交的描述信息
-a:指定镜像作者
e218edb10161：容器ID
runoob/ubuntu:v2:指定要创建的目标镜像名
```

使用新镜像来启动一个容器
> docker run -t -i runoob/ubuntu:v2 /bin/bash     

