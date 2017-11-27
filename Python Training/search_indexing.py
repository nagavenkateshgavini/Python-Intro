import sys
import os
import time

if len(sys.argv) < 2:
	str1 = input("Please Enter the Search Term By Using the Quotes:")
else:
	str1 = sys.argv[1]

list_of_files = os.listdir("Data")



dict1 = {}

start_t = time.time()
for file_name in list_of_files:
	with open("./Data"+"/"+file_name,"r") as filee:
		for line in filee:
			for word in line.split(" "):
				if word not in dict1:
					dict1[word] = [file_name]  
				elif  word in dict1:
					if file_name in dict1[word]:
						continue
					dict1[word].append(file_name)
				 
end_t = time.time()

print("Time Taken is: "+str(end_t - start_t)+"Sec's")

print(dict1[str1])
while str1:
	print(dict1[str1])
	more = input("Do you Need to continue search, Use Quotes:[y/n] ")
	if more == "y":
		str1 = input("Please Enter Search Term in Quotes: ")
		print(dict1[str1])
	else:
		str1 = False
	
