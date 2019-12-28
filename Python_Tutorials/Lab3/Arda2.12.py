#/!/usr/bin/python3

a = int(input("enter an integer1: "))
b = int(input("enter an integer2: "))
c = int(input("enter an integer3: "))

print("a:", a)
print("b:", b)
print("c:", c)
print("a>b is ", a>b)
print("b==c is ", b==c)
print("b!=c is ", b!=c)
print("(a>b) and (b==c) is ", (a>b) and (b==c))
print("(a>b) or (b==c) is ", a>b or b==c)
print("(b!=c) or (b==c) is ", (b!=c) or (b==c))
print("After a %= b, a:", a)

a = 12
b = 5
a //= b
print("After a //= b, a:", a)
