def f(x):
    return x**2

def g(x):
    return f(x)**3

def h(x):
    x = x *2

y = g(4)

print(y)
print(h(y))