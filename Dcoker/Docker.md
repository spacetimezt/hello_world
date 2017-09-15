# 这是我的Docker学习笔记

这是学习的[网站](http://www.runoob.com/docker/docker-tutorial.html)

## 简介
Docker 是一个开源的应用容器引擎，基于 Go 语言 并遵从Apache2.0协议开源。
Docker 可以让开发者打包他们的应用以及依赖包到一个轻量级、可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。
容器是完全使用沙箱机制，相互之间不会有任何接口（类似 iPhone 的 app）,更重要的是容器性能开销极低。
image相当于类
container相当于类实例化产生的对象
每个container都是image产生的

## 安装
### CentOs下的安装
> yum -y install docker

## 使用
- 启动docker服务
> service docker start

- 运行一个容器

通过docker的两个参数 -i -t，让docker运行的容器实现"对话"的能力,-d 代表后台执行
> docker run -i -t ubuntu:15.10 /bin/bash

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