# Linux xz压缩解压

1. 解压 xz 格式文件

 

 方法一：

> 需要用到两步命令，首先利用 xz-utils 的 xz 命令将 linux-3.12.tar.xz 解压为 linux-3.12.tar，其次用 tar 命令将 linux-3.12.tar完全解压。
> xz -d linux-3.12.tar.xz

> tar -xf linux-3.12.tar

方法二（推荐）

> tar -Jxf linux-3.12.tar.xz

2. 创建 xz 格式文件

 方法一：
> 也是用到两步命令，首先利用 tar 命令将 linux-3.12 文件夹打包成 linux-3.12.tar，其次用 xz-utils 的 xz 命令将 linux-3.12.tar 压缩成 linux-3.12.tar.xz。
 
> tar -cf linux-3.12.tar linux-3.12/
> xz -z linux-3.12.tar
 
方法二（推荐）
> tar -Jcf linux-3.12.tar.xz linux-3.12/
