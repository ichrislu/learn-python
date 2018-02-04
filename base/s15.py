#进制转换
i1 = int('123')
print(i1)

i2 = int('0x123', base=16)
print(i2)

i3 = int('110', 2)
print(i3)

#偏函数
#functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
import functools

int2 = functools.partial(int, base=2)
print(int2('110'))
print(int2('0x12f', base=16))

max2 = functools.partial(max, 100)
print(max2(1,4,6,7))