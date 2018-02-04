# list
# 切片，从参数1开始，到参数2结束，但不包含参数2
users = ["u1", "u2", "u3", "u4", "u5"];

print(users);
print(users[1:3]);
print(users[3]);

# 参数1如果是0，可以省略
print(users[:2])

# 负数
print(users[-1])

numbers = list(range(10))
print(numbers)
print(numbers[::2]) # 间隔2个取数

print("=======================")
# tuple
nums = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(nums)
print(nums[1:3])

print("=======================")
str = "abcdefg"
print(str)
print(str[0:3])

print("=======================")
nums = list(range(1,10))
print(nums)
