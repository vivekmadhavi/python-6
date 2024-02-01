#wamdp to track frds attending bf=day party

name=[]
while True:
	op = int(input("1 add name, 2 view names, 3 remove names and 4 exit "))
	if op==1:
		n= input("enter the name ")
		name.append(n)
		print(n,"added to the list ")
	elif op== 2:
		print(name)
	elif op== 3:
		n=input("enter the name ")
		if n in name:
			name.remove(n)
			print(n,"remove")
		else:
			print(n,"not found")

	elif op==4:
		break
	else:
		print("sorry i dont understand")