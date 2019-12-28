#!/usr/bin/python3

Key = 1

print("Arda's calculator")
print( """
	q: quit
	s: sum
	m: minus
	p: product
	d: divided by
	e: exponential
	fd: floor division	
	""")

while(Key == 1):
	
	Command = input("enter your Command: ")

	if(Command == "q"):
		print("quit")
		Key = 0
	elif(Command == "s"):
		x1 = int(input("Enter number x1: "))
		x2 = int(input("Enter number x2: "))
		print("sum command")
		print("x1 + x2 = ", x1 + x2 )
	elif(Command == "m"):
		x1 = int(input("Enter number x1: "))
		x2 = int(input("Enter number x2: "))
		print("minus command")
		print("x1 - x2 = ", x1 - x2 )
	elif(Command == "p"):
		x1 = int(input("Enter number x1: "))
		x2 = int(input("Enter number x2: "))
		print("product command")
		print("x1 * x2 = ", x1 * x2 )
	elif(Command == "d"):
		x1 = float(input("Enter number x1: "))
		x2 = float(input("Enter number x2: "))
		print("divided by command")
		print("x1 / x2 = ", x1 / x2 )
	elif(Command == "fd"):
		x1 = float(input("Enter number x1: "))
		x2 = float(input("Enter number x2: "))
		print("floor division command")
		print("x1 // x2 = ", x1 // x2 )
	elif(Command == "e"):
		x1 = int(input("Enter number x1: "))
		x2 = int(input("Enter number x2: "))
		print("Exponential command")
		print("x1 ** x2 = ", x1 ** x2 )				
	elif(Command != "q","s","m","p","d","fd","e"):
		print("Wrong Command")
			
			
					
				
