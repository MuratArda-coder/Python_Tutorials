#!/usr/bin/python3

many = int(input("how many wordsare you going to enter?\n"))
lista=[]
print("Enter the words")
for x in range(many):
	word=input("")
	lista.append(word)

best = lista[0]
bestcount = 0
for word in lista:
	print("w",word)
	count = 0
	for letter in word:
		print("l",letter)
		if(letter == 'e' or letter == 'E'):
			count = count+1
	if(count>bestcount):
		best = word
		bestcount = count

print("The word with the most E's is ",best)
