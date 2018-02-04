#装饰器
def show_time():
	print('20180201')

f = show_time
f()
print(f.__name__)

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

print("====================")
@log
def now():
	print('2018-02-01')

now