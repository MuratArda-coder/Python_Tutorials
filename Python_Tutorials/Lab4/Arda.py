#!/usr/bin/python3


Tuple = ()

Number = int(input("How many students: "))

for index in range(0,Number):
	Name = input("Enter a name: ")
	Tuple = Tuple + (Name,)
print(Tuple)
