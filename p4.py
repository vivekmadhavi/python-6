#wapp to find the sum and avg 
# of the number given by the user



data=[]
res=input("do you want to enter some number y/n ")
while res=="y":
	d=float(input("inter the number "))
	data.append(d)
	res=input("do you want to enter more y/n ")


print(data)

pos,neg,zero= 0.0,0.0,0.0
for d in data: 
	if d>0:
		pos=pos+1
	elif d<0:
		neg = neg+1
	else:
		zero = zero+1
print("pos ",pos)
print("neg ",neg)
print("zero",zero)