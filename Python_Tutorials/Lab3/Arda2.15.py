#/!/usr/bin/python3
#/!/usr/bin/python3

a =int(input("Enter a number1: "))
b =int(input("Enter a number2: "))

print("a = ", a)
print("b = ", b)
a = b
print("After a = b, a:", a)

print("a = ", a)
print("b = ", b)
a += b
print("After a += b, a:", a)

print("a = ", a)
print("b = ", b)
a = a+b
print("After a = a+b, a:", a)

print("a = ", a)
print("b = ", b)
a -= b
print("After a *= b, a:", a)

print("a = ", a)
print("b = ", b)
a *= b
print("After a *= b, a:", a)

print("a = ", a)
print("b = ", b)
a /= b
print("After a /= b, a:", a)

print("a = ", a)
print("b = ", b)
a %= b
print("After a %= b, a:", a)

print("a = ", a)
print("b = ", b)
a //= b
print("After a //= b, a:", a)
