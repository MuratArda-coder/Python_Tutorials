#!/usr/bin/python3
lista = []
import random
for i in range(100):
	random.randrange(-100,+100)
	lista.append(random.randint(-100,+100))

def minx(lista,k):
	minx=lista[k]
	m=0
	for i in range(k,len(lista)):
		if(lista[i]<=minx):
			minx=lista[i]
			m=i		
	return(m)


def sort(lista):
	for i in range(len(lista)):
		t=minx(lista,i)
		tmp=lista[t]
		lista[t]=lista[i]
		lista[i]=tmp
	return(lista)

sort(lista)
print(lista)

def binarysearch(lista,left,right,number):
	if(left>right):
		return print("wrong")
	
	medium=(left+right)//2
	if(lista[medium]>number):
		return(binarysearch(lista,left,medium-1,number))
	if(lista[medium]<number):
		return(binarysearch(lista,medium+1,right,number))
	if(number==lista[medium]):
		return(print(number,"is in the list"))
	else:
		return(print("wrong"))



binarysearch(lista,lista[0],len(lista)-1,100)

