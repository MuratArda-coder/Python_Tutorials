#!/usr/bin/python3

def factorial(x):
	F = 1
	for index in range(1,x+1):
		F *= index
	print(str(x)+"! =", F)
	return(F)



def combination(x,y):
	C = factorial(x)/(factorial(y)*factorial(x-y))
	print("Combination("+str(x)+","+str(y)+") = ",C)
	return("Combination("+str(x)+","+str(y)+") = ",C)


x = int(input("x = "))
y = int(input("y = "))

if(x>=y):
	combination(x,y)

else:
	print("something wrong")
