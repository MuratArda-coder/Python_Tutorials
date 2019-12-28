#!/usr/bin/python3

def num_letter(x):
	if(ord(x)>=ord('A') and ord(x)<=ord('Z')):
		return(ord(x)-ord('A'))
	if(ord(x)>=ord('a') and ord(x)<=ord('z')):
		return(ord(x)-ord('a'))

def is_smaller(a,b):
	l = 0
	if(len(a)<len(b)):
		l=(len(a))
	if(len(b)<len(a)):
		l=(len(b))
	for i in range(l):
		if(num_letter(a[i])<num_letter(b[i])):
			return True
		if(num_letter(a[i])>num_letter(b[i])):
			return False
	if(len(a)==len(b)):
		return True
	else:
		return False

many = int(input("how many words are you going to enter?\n"))
lista=[]
print("Enter the words")
for x in range(many):
	word=input("")
	lista.append(word)

best_index = 0
for i in range(len(lista)):
	if(is_smaller(lista[i],lista[best_index])):
		best_index = i

print("The first word alphabetically is ",lista[best_index])
