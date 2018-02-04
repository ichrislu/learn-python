# 高阶函数过滤

def f1(i):
	return i % 2 == 0

nums = list(range(10))

result = list(filter(f1, nums))
for i in result:
	print(i)

def f2(s):
	return s and s.strip()

strs = "chris is enginer"
str2 = list(filter(f2, strs))
print(str2)
