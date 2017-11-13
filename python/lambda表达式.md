# Python中lambda表达式学习

lambda只是一个表达式，函数体比def简单很多。

lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。

lambda表达式是起到一个函数速写的作用。允许在代码内嵌入一个函数的定义。

如下例子：



定义了一个lambda表达式，求三个数的和。

再看一个例子：

用lambda表达式求n的阶乘。



------------------------------

lambda表达式也可以用在def函数中。

看例子：



这里定义了一个action函数，返回了一个lambda表达式。其中lambda表达式获取到了上层def作用域的变量名x的值。

a是action函数的返回值，a(22)，即是调用了action返回的lambda表达式。

这里也可以把def直接写成lambda形式。如下

