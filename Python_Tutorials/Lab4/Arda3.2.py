#!/usr/bin/python3

name = input("Enter your name: ")
count = len(name)

for index in range(0,len(name)):
	print(name[len(name)-index-1])
