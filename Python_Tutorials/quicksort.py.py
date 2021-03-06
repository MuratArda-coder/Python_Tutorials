#!/usr/bin/python3

lista = []

import random
for i in range(10):
	random.randint(-500,+500)
	lista.append(random.randint(-500,+500))
print(lista)


def partition(myList, start, end):
	pivot = myList[start]
	left = start+1
	right = end
	done = False
	while not done:
		while left <= right and myList[left] <= pivot:
			left = left + 1
		while myList[right] >= pivot and right >=left:
			right = right -1
		if right < left:
			done= True
		else:
            # swap places
			temp=myList[left]
			myList[left]=myList[right]
			myList[right]=temp
    # swap start with myList[right]
		temp=myList[start]
		myList[start]=myList[right]
		myList[right]=temp
	return right

def quicksort(myList, start, end):
	if start < end:
        # partition the list
		pivot = partition(myList, start, end)
        # sort both halves
		quicksort(myList, start, pivot-1)
		quicksort(myList, pivot+1, end)
	return myList

print(quicksort(lista,0,len(lista)-1))
