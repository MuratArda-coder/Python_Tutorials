#!/usr/bin/python3

def Area(length,width):
	Area = length*width
	print("Area is ",Area)
	return(Area)

def Volume(Area,depth):
	print("Volume is", Area*depth)
	return(Area*depth)

a = int(input("length = "))
b = int(input("Width = "))
c = int(input("depth = "))

Volume(Area(a,b),c)
