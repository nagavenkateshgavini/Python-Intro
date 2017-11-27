import sys
import os
direc = os.listdir("Data")

str1 = sys.argv[1]

for fname in direc:
        with open("./Data"+"/"+fname) as file:
                for line in file:
			cnt = 0
			for word in line.split(" "):
                       		 if str1 in word:
					cnt+=1
                                	print(fname)
                        	 	break
			if cnt == 1:
				break		
			
