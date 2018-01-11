# python中的编码问题探索

## 基本概念

字符串编码常用类型：utf-8,gb2312,cp936,gbk等。

python中，我们使用decode()和encode()来进行解码和编码

在python中，使用unicode类型作为编码的基础类型。即

     decode              encode
	 
str ---------> unicode --------->str

```
u = u'中文' #显示指定unicode类型对象u
str = u.encode('gb2312') #以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8') #以utf-8编码对unicode对像进行编码
u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
u2 = str.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型

```

## 往文件中写Unicode的中文

```
#coding='utf-8'
import sys
import json
import codecs
reload(sys)
sys.setdefaultencoding('utf-8')

fp1=codecs.open('ss10.txt','w',encoding='utf-8')

tmp={u'\u672a\u6388': [u'python', u'\u8bd5\u9a8c'], u'\u6570\u91cf': 22, u'\u8bed\u8a00': u'python'}
sss=json.dumps(tmp,ensure_ascii=False,encoding="gb2312",indent=4)
fp1.write(sss)

#运行结果：
文件ss10.txt中显示结果：
{
    "未授": [
        "python", 
        "试验"
    ], 
    "数量": 22, 
    "语言": "python"
}

```

