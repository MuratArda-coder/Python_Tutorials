#!/usr/bin/python3

List = []

Number = int(input("How many students: "))

for index in range(0,Number):
	Name = input("Enter a name: ")
	List = List + [Name]
print(List)
List[Number-2] = ['Arda']
print(List)
