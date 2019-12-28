#!/usr/bin/python3

def factorial(x):
	F = 1
	for index in range(1,x+1):
		F *= index
	print(str(x)+"! =", F)
	return(str(x)+"! =", F)

a = int(input(""))
factorial(a)
