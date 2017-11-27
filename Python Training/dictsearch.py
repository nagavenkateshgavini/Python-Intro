import sys
import os


if len(sys.argv) < 2:
	str1 = input("Please Enter the Search Term By Using the Quotes:")
else:
	str1 = sys.argv[1]

list_of_files = os.listdir("Data")



dict1 = {}
for file_name in list_of_files:
	with open("./Data"+"/"+file_name,"r") as filee:
		for line in filee:
			for word in line.split(" "):
				if word not in dict1:
					dict1[word] = [file_name]  
				elif  word in dict1:
					dict1[word].append(file_name)
				        
print(dict1)			
						
