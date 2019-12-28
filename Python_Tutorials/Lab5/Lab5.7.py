#!/usr/bin/python3

N = int(input("N= "))
sum1 = 0
sum2 = 0

for i in range(N+1):
	for j in range(i+1):
		sum1 = (2*j**3)
		sum2 += sum1
		print("inside:",j,":",sum2 )
print(sum2)
