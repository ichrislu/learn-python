# 可变参数、关键字参数

def mysum(*numbers):
	sum = 0;
	for index in numbers:
		sum += index;
	return sum;

print(mysum(1, 2, 3, 4));

mynum = (1, 2, 3, 4, 5);
print(mysum(*mynum))

def myfun1(name, **others):
	if 'sex' in others:
		pass;
	print("name:", name, ", others:", others);

print(myfun1("a"));
print(myfun1("a", b = "b"));
print(myfun1("a", sex = "man", age = "33"));