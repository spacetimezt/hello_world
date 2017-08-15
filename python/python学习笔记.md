# 这是我的Python学习笔记
## 关于Json字符串的处理

```
import json
 
data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
 
json_str = json.dumps(data)
data = json.loads(json_str)
```
以上就是json数据与字符串数据的相互转换

推荐一个好用的Json字符串美化工具：[点我](http://tools.jb51.net/code/json#home)

格式化打印json字符串

>print(json.dumps(tmp,indent=4))

这样就能打印的漂漂亮亮的了O(∩_∩)O~~


## Python下telnet的使用
```
import telnetlib
def tel(host_ip,port):
    # 连接Telnet服务器
    try:
        tn = telnetlib.Telnet(host_ip,port=port)
        tn.close()
        return True
    except Exception,e:
        print(e)
        return False
```
这是一个telnet的函数，如果需要根据情况登录的话，可以参照以下代码：
```
# 输入登录用户名
tn.read_until('login: ')
tn.write(username + '\n')

# 输入登录密码
tn.read_until('Password: ')
tn.write(password + '\n')

# 登录完毕后，执行ls命令
tn.read_until(finish)
tn.write('ls\n')

# ls命令执行完毕后，终止Telnet连接（或输入exit退出）
tn.read_until(finish)
tn.close() # tn.write('exit\n')
```

## Python 装饰器
装饰器其实就是一个闭包，把一个函数当做参数然后返回一个替代版函数。
```
def outer(some_func):
     def inner():
         print "before some_func"
         ret = some_func() # 1
         return ret + 1
     return inner
def foo():
     return 1
decorated = outer(foo) # 2
decorated()
before some_func
2
```

```
def logger(func):
    def inner(*args, **kwargs):  # 1
        print "Arguments were: %s, %s" % (args, kwargs)
        print func(*args, **kwargs)  # 2

    return inner


def foo3(x, y=1):
    return x * y


@logger
def foo1(x, y=1):
    return x * y


foo2 = logger(foo3)
foo1(5, 4)
print('*' * 20)
foo2(5, 4)

```
我的理解，装饰器一种简便写法。将foo2这种返回函数的写法简化成直接定义为foo1这种形式。相当于对foo1进行了装饰，用logger函数进行的装饰。

## 正在了解Python的编码方式...


