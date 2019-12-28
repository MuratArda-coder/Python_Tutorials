#!/usr/bin/python3

def h(x):
	average = 0
	for index in range(len(x)):
		average += x[index] 

	average = average/len(x)
	print(average)
	return(average)


List1 = [1, -1, 10000, 3, 56, -90, -1000]

print(List1)
h(List1)

a = h(List1)
print("a ="+str(a)) 
