#!/usr/bin/python3

def Matris(col,row,List,name):
	print(name,List)
	if(row*col <= len(List)):
		print("Matrix",name)
		for r in range(row):
			for c in range(col):
				print(List[r*col+c], end=" ")
			print("\n")
	else:
		print("not enough number")


List1 = [1,2,3,4,5,6,7,8,9]
r1 = int(input("row1 = "))
c1 = int(input("col1 = "))
Matris(c1,r1,List1,"MatrixA")

List2 = [11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
r2 = int(input("row2 = "))
c2 = int(input("col2 = "))
Matris(c2,r2,List2,"MatrixB")
