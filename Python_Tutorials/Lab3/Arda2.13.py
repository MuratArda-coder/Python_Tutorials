#/!/usr/bin/python3

mylist = [1, 6, 8, 2, 7,]

a = int(input("Enter a number which is not in my list: "))

if(a not in mylist):
	print(a ,"is not in my list, true")

else:
	print(a ,"is my list, false")
