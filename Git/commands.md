# Git常用指令

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

