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

推送其他分支的时候
$ git push origin [分支名称]
```

5.要查看远程库的信息

```
$ git remote
origin

$ git remote -v
origin  git@github.com:michaelliao/learngit.git (fetch)
origin  git@github.com:michaelliao/learngit.git (push)
```

6.抓取分支

```
$ git clone git@github.com:michaelliao/learngit.git
Cloning into 'learngit'...
remote: Counting objects: 46, done.
remote: Compressing objects: 100% (26/26), done.
remote: Total 46 (delta 16), reused 45 (delta 15)
Receiving objects: 100% (46/46), 15.69 KiB | 6 KiB/s, done.
Resolving deltas: 100% (16/16), done.

$ git pull

```

7.将本地的分支dev 与远程的origin/dev分支链接

```
$ git branch --set-upstream dev origin/dev
Branch dev set up to track remote branch dev from origin.
```

8.多人协作的基本工作模式

```
首先，可以试图用git push origin branch-name推送自己的修改；
如果推送失败，则因为远程分支比你的本地更新，需要先用git pull试图合并；
如果合并有冲突，则解决冲突，并在本地提交；
没有冲突或者解决掉冲突后，再用git push origin branch-name推送就能成功！
如果git pull提示“no tracking information”，则说明本地分支和远程分支的链接关系没有创建，用命令git branch --set-upstream branch-name origin/branch-name。
这就是多人协作的工作模式，一旦熟悉了，就非常简单。

小结
查看远程库信息，使用git remote -v；
本地新建的分支如果不推送到远程，对其他人就是不可见的；
从本地推送分支，使用git push origin branch-name，如果推送失败，先用git pull抓取远程的新提交；
在本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name，本地和远程分支的名称最好一致；
建立本地分支和远程分支的关联，使用git branch --set-upstream branch-name origin/branch-name；
从远程抓取分支，使用git pull，如果有冲突，要先处理冲突。
```





## 分支管理

1.创建与切换分支

```
$ git checkout -b dev
Switched to a new branch 'dev'

这一条指令相当于：
创建分支dev
$ git branch dev			
切换到dev分支
$ git checkout dev
Switched to branch 'dev'

```

2.查看分支

```
git branch命令会列出所有分支，当前分支前面会标一个*号。
```

3.合并分支

```
$ git checkout master
使用Fast forward模式，删除分支后，丢失分支信息
$ git merge dev
Updating d17efd8..fec145a
Fast-forward
 readme.txt |    1 +
 1 file changed, 1 insertion(+)
 
 使用no-ff模式合并，也就是普通模式
$ git merge --no-ff -m "merge with no-ff" dev
 
```

4.删除分支

```
合并分支后就可以安全的删除之前的分支
$ git branch -d dev
Deleted branch dev (was fec145a).

如果要丢弃一个没有被合并过的分支，可以通过git branch -D <name>强行删除。
```



5.查看分支合并情况

```
$ git log --graph --pretty=oneline --abbrev-commit
*   59bc1cb conflict fixed
|\
| * 75a857c AND simple
* | 400b400 & simple
|/
* fec145a branch test
...
```

6.解决冲突

```
有时候需要手动解决冲突，然后手动add，commit
```

7.将工作区修改暂时保存以及还原（类似压栈）

```
$ git stash
Saved working directory and index state WIP on dev: 6224937 add merge
HEAD is now at 6224937 add merge

查看保存的内容
$ git stash list

还原：
不删除栈区：
git stash apply
或者
删除栈区：
git stash pop

```



## 标签管理

1.创建标签

```
$ git branch
* dev
  master
$ git checkout master
Switched to branch 'master'

敲命令git tag <name>就可以打一个新标签：
$ git tag v1.0
```

2.查看所有标签

```
$ git tag
v1.0
```

3.给前面的commit打标签

```
$ git log --pretty=oneline --abbrev-commit
6a5819e merged bug fix 101
cc17032 fix bug 101
7825a50 merge with no-ff
6224937 add merge
59bc1cb conflict fixed
400b400 & simple
75a857c AND simple
fec145a branch test
d17efd8 remove test.txt
...

$ git tag v0.9 6224937

```

4.查看标签信息

```
$ git show v0.9
commit 622493706ab447b6bb37e4e2a2f276a20fed2ab4
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Thu Aug 22 11:22:08 2013 +0800

    add merge
...
```

5.创建带有说明的标签

```
$ git tag -a v0.1 -m "version 0.1 released" 3628164
$ git show v0.1
tag v0.1
Tagger: Michael Liao <askxuefeng@gmail.com>
Date:   Mon Aug 26 07:28:11 2013 +0800

version 0.1 released

commit 3628164fb26d48395383f8f31179f24e0882e1e0
Author: Michael Liao <askxuefeng@gmail.com>
Date:   Tue Aug 20 15:11:49 2013 +0800

    append GPL

```

6.删除标签

```
$ git tag -d v0.1
Deleted tag 'v0.1' (was e078af9)
因为创建的标签都只存储在本地，不会自动推送到远程。所以，打错的标签可以在本地安全删除。
```

7.推送某个标签到远程

```
$ git push origin v1.0
Total 0 (delta 0), reused 0 (delta 0)
To git@github.com:michaelliao/learngit.git
 * [new tag]         v1.0 -> v1.0
 
 一次性推送全部尚未推送到远程的本地标签：
 $ git push origin --tags
Counting objects: 1, done.
Writing objects: 100% (1/1), 554 bytes, done.
Total 1 (delta 0), reused 0 (delta 0)
To git@github.com:michaelliao/learngit.git
 * [new tag]         v0.2 -> v0.2
 * [new tag]         v0.9 -> v0.9
```

8.删除远程标签

```
先删除本地
$ git tag -d v0.9
Deleted tag 'v0.9' (was 6224937)
从远程删除
$ git push origin :refs/tags/v0.9
To git@github.com:michaelliao/learngit.git
 - [deleted]         v0.9
```

