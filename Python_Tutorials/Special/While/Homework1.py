#!/usr/bin/python3

Dict = {}
Key = 1

while(Key == 1):
	Kod = input("Enter a Kod:")
	if(Kod == "q"):
		Key = 0
		print("quit")
	elif(Kod == "h"):
		print("Help command open:")
		print("q:quit")
		print("h:help")
		print("a:write user name and id")
		print("p:print user name and id")
	elif(Kod == "a"):
		Name = input("Enter Your name: ")
		Id = int(input("Enter your id: "))
		Dict[Name]=Id
	elif(Kod == "p"):
		print(Dict)
	elif(Kod != "q","p","h","a"):
		print("Wrong Key")
