# 用高阶函数将不规则的用户名改为首字母大写
def do_name(name):
	return name.capitalize()

names = ['chriS', "Email", "coby", 'ACE']

names2 = map(do_name, names)
for name in names2:
	print(name)