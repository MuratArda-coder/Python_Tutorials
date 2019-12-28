#!/usr/bin/python3

b = input("")
key = 1
while(key == 1):
	if(b == 'q'):
		print("Goodbye!")
		break
	else:
		b = int(b)
		print(b, "is minimum", b , "is maximum")
	while(1):
		a = input("")
		if(a == 'q'):
			print("Goodbye!")
			key = 0
			break
		a = int(a)
		if(a<b):
			
			print(a, "is minimum", b , "is maximum")
			
		else:
					
			print(b, "is minimum", a , "is maximum")
			
