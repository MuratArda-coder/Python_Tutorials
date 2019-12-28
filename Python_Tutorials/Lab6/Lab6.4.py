#!/usr/bin/python3

def g(x):
	min = x[0]
	for index in range(1,len(x)):
		if(min > x[index]):
			min = x[index]
	print(min)
	return(min)


List1 = [1, -1, 10000, 3, 56, -90, -1000]

print(List1)
g(List1)

a = g(List1)
print("a ="+str(a))
