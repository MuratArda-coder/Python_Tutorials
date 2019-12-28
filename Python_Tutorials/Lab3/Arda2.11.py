#/!/usr/bin/python3

a = int(input("enter a binary number. a: "), base = 2)
b = int(input("enter a binary number. b: "), base = 2)

print("(a+b) is ", bin(a+b))
print("(a+b) is ", (a+b))
print("(a&b) is ", bin(a&b))
print("(a|b) is ", bin(a|b))
print("(a^b) is ", bin(a^b))
print("(~b) is ", bin(~b))
print("(~a) is ", bin(~a))
print("(a<<b) is ", bin(a<<b))
print("(a>>b) is ", bin(a>>b))
