import sys
import os
direc = os.listdir("Data")
str1 = sys.argv[1]

for fname in direc:
        with open("./Data"+"/"+fname) as file:
    		for line in file:
		 	if str1 in line:
				print(fname) 
				break
				
