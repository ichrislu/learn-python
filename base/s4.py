# 默认参数

def gen_name(x="none"):
	return 'chris ' + x;


def sum(a, b):
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
		raise TypeError("bad operand type");

	return a + b;

# 定义默认参数要牢记一点：默认参数必须指向不变对象！
def app_end(list=[]):
	list.append("end");
	return list;

def app_end2(list=None):
	if (list is None) :
		list = [];
	list.append('end');
	return list;


name = gen_name('liu');
print(name);

name = gen_name();
print(name);

print(sum(5.1, 3));
# print(sum('a', 3));

print("======================for app_end")
print(app_end(["chris", 'lu']));
print(app_end([1, 2, 4]));
print(app_end([]));
print(app_end());
print(app_end());
print(app_end());

print("======================for app_end2")
print(app_end2());
print(app_end2());
print(app_end2());
