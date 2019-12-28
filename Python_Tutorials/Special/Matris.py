#!/usr/bin/python3


n= int(input("n= "))

m= int(input("m= "))


mtrx = [11, 1,2, 3, 4, 12, 8, 2, 3, 7, 11, 10, 9, 8, 5, 6, 7, 8, 9 , 10, 11, 3, 3, 2, 1, 0, 0, -1]

if(len(mtrx) != n*m):

		print ("error")


for i in range (m):

	for j in range (n):

		print (mtrx[i*n+j], end=' ')

	print ('\n')





