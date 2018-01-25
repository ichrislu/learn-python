# 高阶函数

def f1(x):
	return x*x;

nums = list(range(10))
print(nums)

l = map(f1, nums)
for i in l:
	print(i)
