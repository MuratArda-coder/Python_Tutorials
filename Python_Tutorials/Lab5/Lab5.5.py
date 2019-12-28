#!/usr/bin/python3

N = int(input(""))
sum1 = (N*(N+1))/2
print(sum1)

sum2 = 0
for index in range(N+1):
	sum2 += float(index)		
print(sum2)

