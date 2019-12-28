#!/usr/bin/python3,

lista = []

import random

for i in range (10000):
	random.randint(-500,+500)
	lista.append(random.randint(-50,+50))
n = len(lista)
print(lista)
for i in range(1,n):
	j = i-1
	key = lista[i]
	while(j>=0 and lista[j]>key):
		lista[j+1]=lista[j]
		lista[j]=key
		j=j-1
	lista[j+1]=key
	


print(lista)
		
