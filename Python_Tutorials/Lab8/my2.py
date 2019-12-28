#!/usr/bin/python3

number = int(input("how many wordsare you going to enter?\n"))
print("Enter the words.")
t = 0
lista=[]
while(t != number):
	words = input("")
	lista.append(words)
	t = t+1
listb = []
z = []
for i in range(len(lista)):
	a = list(lista[i])
	if('E' or 'e' in a):
		z = lista[i]
		listb.append(z)
listc = []
d = 0
for i in range(len(listb)):
	a = list(listb[i])
	for j in range(len(a)):
		if(a[j]=='E'):
			d = d+1
		if(a[j]=='e'):
			d = d+1
	listc.append(d)
	d=0

s=0
for i in range(len(listc)):
	if(s < listc[i]):
		s = listc[i]
		word=lista[i]
if(z==[]):
	print("no words")
else:
	print("The word with the most Es is", word)
