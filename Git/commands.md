# Git常用指令

## 本地Git命令

1. 仓库初始化

   ```
   $ git init
   ```

2. 添加文件到仓库

  ```
  $ git add readme.txt
  $ git commit -m "wrote a readme file"
  [master (root-commit) cb926e7] wrote a readme file
   1 file changed, 2 insertions(+)
   create mode 100644 readme.txt
  ```

3. 添加多个文件

  ```
  $ git add file1.txt
  $ git add file2.txt file3.txt
  $ git commit -m "add 3 files."
  ```

4. 查看是否有更改

   ```
   $ git status
   # On branch master
   # Changes not staged for commit:
   #   (use "git add <file>..." to update what will be committed)
   #   (use "git checkout -- <file>..." to discard changes in working directory)
   #
   #    modified:   readme.txt
   #
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

5.查看更改细节

```
$ git diff readme.txt 
diff --git a/readme.txt b/readme.txt
index 46d49bf..9247db6 100644
--- a/readme.txt
+++ b/readme.txt
@@ -1,2 +1,2 @@
-Git is a version control system.
+Git is a distributed version control system.
 Git is free software.
```

6.查看仓库版本

```
$ git log
commit 3628164fb26d48395383f8f31179f24e0882e1e0
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Tue Aug 20 15:11:49 2013 +0800

    append GPL

commit ea34578d5496d7dd233c827ed32a8cd576c5ee85
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Tue Aug 20 14:53:12 2013 +0800

    add distributed

commit cb926e7ea50ad11b8f9e909c05226233bf755030
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Mon Aug 19 17:51:55 2013 +0800

    wrote a readme file
```

```
$ git log --pretty=oneline
3628164fb26d48395383f8f31179f24e0882e1e0 append GPL
ea34578d5496d7dd233c827ed32a8cd576c5ee85 add distributed
cb926e7ea50ad11b8f9e909c05226233bf755030 wrote a readme file
```

```
$ git reflog
ea34578 HEAD@{0}: reset: moving to HEAD^
3628164 HEAD@{1}: commit: append GPL
ea34578 HEAD@{2}: commit: add distributed
cb926e7 HEAD@{3}: commit (initial): wrote a readme file
这个是详细日志
```

7.回退到上一个版本

```
$ git reset --hard HEAD^
HEAD is now at ea34578 add distributed
```

8.回退到具体版本

```
$ git reset --hard 3628164
HEAD is now at 3628164 append GPL
后面这个是git的版本号
```

9.暂存区原理

![](/1.jfif)

10.回退到未提交的最新版本

```
$ git reset HEAD readme.txt
Unstaged changes after reset:
M       readme.txt
git reset HEAD file  可以把暂存区的修改撤销掉（unstage），重新放回工作区
```

11.丢弃工作区的修改

```
$ git checkout -- readme.txt

$ git status
# On branch master
nothing to commit (working directory clean)
```

12.删除文件

```
$ git rm test.txt
rm 'test.txt'

$ git commit -m "remove test.txt"
[master d17efd8] remove test.txt
 1 file changed, 1 deletion(-)
 delete mode 100644 test.txt
```

13.恢复删除文件

```
$ git checkout -- test.txt

git checkout其实是用版本库里的版本替换工作区的版本，无论工作区是修改还是删除，都可以“一键还原”。
```



## 远程Git命令

1.Git服务器搭建

```
#yum install -y git
[root@localhost home]# useradd git
[root@localhost home]# passwd git

创建仓库并初始化
[root@localhost home]# mkdir -p data/git/gittest.git
[root@localhost home]# git init --bare data/git/gittest.git
Initialized empty Git repository in /home/data/git/gittest.git/
[root@localhost home]# cd data/git/
[root@localhost git]# chown -R git:git gittest.git/

克隆远程仓库
在客户端
$ git clone git@192.168.56.101:/home/data/gittest.git

密钥形式登陆：
创建私钥公钥（客户端完成）
$ ssh-keygen -t rsa -C "test@qq.com"
然后产生公钥和私钥

服务器添加公钥：
进入 /etc/ssh 目录，编辑 sshd_config，打开以下三个配置的注释：
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys

重启sshd服务
[root@localhost ssh]# /etc/rc.d/init.d/sshd restart
在centos下，使用 service sshd restart
由 AuthorizedKeysFile 得知公钥的存放路径是 .ssh/authorized_keys，实际上是 $Home/.ssh/authorized_keys，由于管理 Git 服务的用户是 git，所以实际存放公钥的路径是 /home/git/.ssh/authorized_keys

重要：
修改 .ssh 目录的权限为 700
修改 .ssh/authorized_keys 文件的权限为 600

[root@localhost git]# chmod 700 .ssh
[root@localhost git]# cd .ssh
[root@localhost .ssh]# chmod 600 authorized_keys 

禁止 git 用户 ssh 登录服务器
之前在服务器端创建的 git 用户不允许 ssh 登录服务器
编辑 /etc/passwd
讲
git:x:502:504::/home/git:/bin/bash
修改为
git:x:502:504::/home/git:/bin/git-shell

```



2.添加远程仓库

```
$ git remote add origin git@192.168.0.236:/home/git/test.git
```

3.把本地库的所有内容推送到远程库上：

```
$ git push -u origin master
Counting objects: 19, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (19/19), done.
Writing objects: 100% (19/19), 13.73 KiB, done.
Total 23 (delta 6), reused 0 (delta 0)
To git@github.com:michaelliao/learngit.git
 * [new branch]      master -> master
Branch master set up to track remote branch master from origin.
```

4.之后做提交

```
$ git push origin master
```