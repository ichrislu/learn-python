#lambda是匿名函数关键字，冒号前面表示参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
l = list(map(lambda  x:x * x, [1, 3, 5 , 7, 9]))
print(l)