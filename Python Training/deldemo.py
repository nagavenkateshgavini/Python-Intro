x=10
print(x>5)
x = range(10)
print(type(x), id(x), x)

y = list(x)
print(type(y), id(y), y)

z= "Naga Venkatesh Gavini"
sum = 0
for ch in z:
	print(ord(ch),end=" ")
	sum=sum+ord(ch)
print("\n"+str(sum))

k = 65
print(chr(65))	

y = input("Input please: ")
for i in y:
	print(i)
u = input("Next One Please: ")
mul = u * 2
print(mul,type(mul))



d = 10
l = 20
print("d= ",d,"l= ",l)

str1 = "Venkatesh"
list1 = list(str1)
print(list1[::-1])
str = "".join(list1[::-1])
print(str)






