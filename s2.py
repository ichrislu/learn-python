# 有序集合，

# 以下是关于可变的list
names = ["chris", "una", "emily", 'chris'];
for name in names:
    print(name);

names.pop(3);
names[1] = 'una li';
print(names);
print(len(names));
print(names[1]);

count = len(names);

if count < 0:
    print("集合为空");
elif count == 1:
    print("只有1外");
else:
    print('太多了')

names.clear();
print(len(names));
print(names);
print("============");

# 以下是关于不可变的tuple
names = ("shmily", "ack");
print(names);
print(names[0]);

print("============");
i = float('10');
print(i);

print("============");

i = 0;
while i < 3:
    print(i);
    i+=1;

map = {"name" : "Chris", "age" : 33};
print(map["name"]);

list = set([1, 2, 3, 5]);
list.add(10);
print(list;

print("the end!");
