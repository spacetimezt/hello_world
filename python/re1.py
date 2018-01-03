#coding=utf-8
import re
#贪婪
ret_greed= re.findall(r'a(\d+)','a23b')
print(ret_greed)
#非贪婪
ret_no_greed= re.findall(r'a(\d+?)','a23b')
print(ret_no_greed)

a = 'one1two2three3four4'
ret = re.findall(r'(\d+)',a)
print(ret)


p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group()


ret_match= re.match("c","abcde");     #从字符串开头匹配，匹配到返回match的对象，匹配不到返回None
if(ret_match):
    print("ret_match:"+ret_match.group());
else:
    print("ret_match:None");

ret_search = re.search("c","abcde"); #扫描整个字符串返回第一个匹配到的元素并结束，匹配不到返回None
if(ret_search):
    print("ret_search:"+ret_search.group());



a = "123abc456"
ret_match= re.match("a","abcde");
print(ret_match.group())  #返回返回被 RE 匹配的字符串
print(ret_match.start())  #返回匹配开始的位置
print(ret_match.end())    #返回匹配结束的位置
print(ret_match.span())   #返回一个元组包含匹配 (开始,结束) 的位置

a = "123abc456"
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体默认返回group(0)
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456


#sub
ret_sub = re.sub(r'(one|two|three)','ok','one word two words three words') #ok word ok words ok words
print ret_sub
#subn

ret_subn = re.subn(r'(one|two|three)','ok','one word two words three words') #('ok word ok words ok words', 3) 3,表示替换的次数

print ret_subn

ret = re.split('\d+','one1two2three3four4') #匹配到1的时候结果为'one'和'two2three3four4'，匹配到2的时候结果为'one', 'two'和'three3four4', 所以结果为：
print ret

text = "JGood is a handsome boy, he is cool, clever, and so on..."
regex = re.compile(r'\w*oo\w*')
print regex.sub('hhh',text)
print regex.search(text).group(0)
print(regex.findall(text))

#https://www.cnblogs.com/yyyg/p/5498803.html