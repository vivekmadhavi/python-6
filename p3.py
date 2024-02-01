#wapp to find the sum and avg 
# of the number given by the user



data=[]
res=input("do you want to enter some number y/n ")
while res=="y":
	d=float(input("inter the number "))
	data.append(d)
	res=input("do you want to enter more y/n ")


print(data)

sum ,avg = 0.0,0.0
for d in data: 
	sum += d
avg = sum /len(data)

print("sum = ",round(sum,2))
print("avg = ",round(avg,2))