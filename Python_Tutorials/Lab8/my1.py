#!/usr/bin/python3

#wrong about lower or upper case,out of range if lengt of all words are not equal#

number = int(input("how many wordsare you going to enter?\n"))
print("Enter the words.")
t = 0
lista=[]
while(t != number):
	words = input("")
	lista.append(words)
	t = t+1

listb= []
h = 0
key = 1
while(key == 1):
	for i in range(len(lista)):
		a = list(lista[i])
		z=a[h]
		b = ord(z)
		listb.append(b)
	s = listb[h]
	for i in range(1,len(listb)):
		if(s>listb[i]):
			s=listb[i]
			k = lista[i]
			key = 0
			break
	listb = []
	h = h+1

print("The first word alphabetically is ",k)
