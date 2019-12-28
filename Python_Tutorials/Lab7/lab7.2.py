#!/usr/bin/python3

lista = []
import random

for i in range (10000):
	random.randint(-500,+500)
	lista.append(random.randint(-50,+50))
n = len(lista)
print(lista)
while(1):
	for i in range(1,n):
		if(lista[i-1]>lista[i]):
			key=lista[i]
			lista[i]=lista[i-1]
			lista[i-1]=key
			swap=0
	if(swap==0):
		swap=1
	else:
		break
print(lista)
