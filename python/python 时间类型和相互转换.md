## time有四种类型（time, datetime, string, timestamp）

**1. time string**

string是最简单的表示time的方式

如如下代码生成的即为string

或者更简单的生成一个字符串

 

**2. datetime tuple(datetime obj)**

datetime tuple是datetime.datetime对象类型

 

**3. time tuple(time obj)**

time tuple是time.struct_time对象类型

 

**4. timestamp**

时间戳类型:自1970年1月1日(00:00:00 GMT)以来的秒数

 

## time, datetime, string, timestamp相互转换

**1. string 转换为其它**

初始化:

​    date_str = "2016-11-30 13:53:59"

 

**1.1 string --> datetime obj**

 

**1.2 string --> time obj**

 

**2. datetime obj转换为其它**

datetime obj转换为其它类型,用的都是datetime的函数

初始化:

​    dt_obj = datetime.datetime(2016, 11, 30, 13, 53, 59)

**2.1 dt obj --> string**

 

**2.2 dt obj --> time obj**

 

**3. time obj转换为其它**

初始化:

​    time_tuple = (2016, 11, 30, 13, 51, 18, 2, 317, 0)

 

**3.1 time obj --> string**

 

**3.2 time obj --> datetime obj**

 

**3.3 time obj --> timestamp**

 

**4. timestamp转换为其它**

初始化:

​    timestamp = 1480486369.75

 

--!!--注意以下两种都使用local时区

**4.1 timestamp --> dt obj**

 

**4.2 timestamp --> time obj**

 

--!!--以下两种方式和时区相关,比较标准时区时间和本地时区时间

**4.3 使用UTC --> dt obj**

\#本地时区时间

\#标准时区时间

 

**4.4 使用UTC --> time obj**

\#本地时区时间

\#标准时区时间