#!/usr/bin/python3


n = int(input("enter an integer:"))

if(n % 2 == 1):
	if(n<100):
		print("b")
	elif(n>100):
		print("wrong")	
elif(n % 2 == 0):
	if(6>n>1):
		print("a")
	elif(20>=n>=6):
		print("x")
	elif(n>20): 
		print("z")

