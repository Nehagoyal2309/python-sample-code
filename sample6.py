i = 5
def f(arg=i):
    print(arg)
i = 6
f() # function call without arguements
f(i) # with arguments

a=2
def f(a, L=[]):
    L.append(a)
    return L
print(f(a))
print(f(2))
print(f(3))
