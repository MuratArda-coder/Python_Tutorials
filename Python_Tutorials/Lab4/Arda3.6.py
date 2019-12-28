#!/usr/bin/python3

Dict = {}
Number = int(input("How many students: "))

for index in range(Number):
	Name = input("Enter the name: ")
	İd = int(input("Enter the İd: "))
	Dict[Name]=İd
print(Dict)
