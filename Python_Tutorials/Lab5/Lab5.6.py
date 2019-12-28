#!/usr/bin/python3

a = int(input("a= "))
d = int(input("d= "))
n = int(input("n= "))
sum1 = 0

for index in range(n):
	sum1 += a+(index*d)
print(sum1)
