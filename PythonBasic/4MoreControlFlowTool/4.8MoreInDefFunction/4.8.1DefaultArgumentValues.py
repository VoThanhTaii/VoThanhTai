i = 5

def f(arg=i):
    print(arg)

i = 6
f() #Will Print 5


def fa(a, L=[]):
    L.append(a)
    return L

print(fa(1))
print(fa(2))
print(fa(3))