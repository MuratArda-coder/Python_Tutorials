#!/usr/bin/python3

a = input("enter a digit number: ")
List = list(a)
t = int(a)

if(t>=100 and t<=999):
	b = input("enter a single digit number: ")
	if(b not in List):
		print(b, "is not a digit of ", a)
	else:
		print("Good")
else:
	print(t, "is not 3 digit number")
	
