# pip下载保存Python包，pip离线安装

#  新版pip下载安装包命令：

pip download  -r requirements.txt  -d  /tmp/paks/

**在linux下**

 1.下载指定的包到指定文件夹。

​          pip list #查看安装的包

​          pip freeze > requirements.txt   将已经通过pip安装的包的名称记录到 requirements.txt文件中

​          创建存放安装包的目录：mkdir /packs

​           pip install   --download   /packs  pandas(存放一个pandas包)    或 pip install   --download   /packs -r requirements.txt（存放requirements.txt列出的所有包）

2.安装指定的离线包

​      pip install   --no-index   --find-links=/packs/   pandas 或 pip install   --no-index   --find-links=/packs/   -r   requirements.txt    （也可能是 --find-link）