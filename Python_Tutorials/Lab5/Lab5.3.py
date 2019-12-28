#!/usr/bin/python3

b = input("")
key = 1
while(key == 1):
	
	if(b == 'q'):
		print("Goodbye!")
		break
	else:
		b = int(b)
		print(b, "is maximum")
		

	while(1):
		a = input("")
		if(a == 'q'):
			print("Goodbye!")
			key = 0
			break
		a = int(a)
		if(a>b):
			b = a
			print(a, "is maximum")
		else:
			print(b, "is maximum")
