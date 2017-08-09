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

## 正在了解Python的编码方式...
