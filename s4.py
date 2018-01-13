def gen_name(x):
    return 'chris ' + x;

def sum(a, b):
    if not isinstance (a, (int, float)) or not isinstance (b, (int, float)):
        raise TypeError("bad operand type");

    return a+b;

name = gen_name('liu');
print(name);

print(sum(1.2, 3));
