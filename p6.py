#wapp to red the marks of your freind
#an print the name in alphabettical order 



marks=[]
res=input("do you want to enter marks y/n ")
while res== "y":
	n=input("inter the name ")
	marks.append(n)
	res=input("do you want to enter more y/n ")
print(marks)
print("min = ",min(marks))
print("max = ",max(marks))

#logic2
marks.sort()
min=marks[0]
max=marks[-1]
print("min = ",min)
print("max = ",max)

	