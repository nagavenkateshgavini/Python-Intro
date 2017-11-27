import sys
import os

if len(sys.argv) < 2:
	str1 = input("Please Enter the Search Term by using Quotes: ")
else:
	str1 = sys.argv[1]

list_of_files = os.listdir("Data")

for file_name in list_of_files:
        with open("./Data"+"/"+file_name,"r") as filee:
                for line in filee:
                        cnt = 0
                        for word in line.split(" "):
                                 if str1 in  word:
                                        cnt+=1
                                        print(file_name)
                                        break
                        if cnt == 1:
                                break


