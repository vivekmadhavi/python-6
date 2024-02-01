#read tuple of integer from user 


data =()
res=input("do u want to enter integer y/n ")
while res =="y":
	d=int(input("enter the integer "))
	data= data+(d,)
	res =input("do u want to enter more y/n ")
print(data)
	