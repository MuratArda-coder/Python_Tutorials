#!/usr/bin/python3

def f(x):
	max = x[0]
	for index in range(1,len(x)):
		if(max < x[index]):
			max = x[index]
	print(max)
	return(max)

List1 = [1, -1, 10000, 3, 56, -90, -1000]

print(List1)
f(List1)

List2 = [5, 6, 7, 23]
a = f(List1)
print("a ="+str(a))

print(List2)
f(List2)

