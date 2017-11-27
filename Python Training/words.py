import sys


# Opened the file in read Mode

file=open(sys.argv[1],"r")     
wordcount={}

#------------------------------------------

# We are Storing each word with the Count.

for word in file.readline().split():
	if word not in wordcount:
        	wordcount[word] = 1
    	else:
        	wordcount[word] += 1
        
#-------------------------------------------

# Finally We are Printing the Word and it's Count.
        
for k,v in wordcount.items():
    print k, v
file.close()




    

