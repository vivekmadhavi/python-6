#wapp to red the name of your freind
#an dprint the name in alphabettical order 
#i/p: seema neema reema tina amit
#i/pamit neema reema seema tina


names=[]
res=input("do you want to enter some name y/n ")
while res== "y":
	n=input("inter the name ")
	names.append(n)
	res=input("do you want to enter more y/n ")

print(names)
names.sort()
print(names)
	



