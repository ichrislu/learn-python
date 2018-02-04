# 返回函数
def lazy_sum(*args):
	def sum():
		s = 0
		for i in args:
			s += i
		return s
	return sum

# 返回的函数并没有马上执行，直到调用了f1()
f1 = lazy_sum(2, 4, 6, 8)
print(f1())

# 这种程序结构即为闭包
# lazy_sum的每次调用都返回一个新的函数，即使传入的参数是一样的
f2 = lazy_sum(2, 4, 6, 8)
print(f1 == f2)

# 关于闭包的大坑
# 以下示例演示：实际上count函数返回的是3个函数，这3个函数在实际打印的时候才会执行，但此时函数中变量i的值以是3，所以3个函数返回值一样！！！
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
def count():
	fs = [];
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
