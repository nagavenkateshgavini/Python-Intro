import sys
filepath = sys.argv[1]

with open(filepath) as fp:
    line = fp.readline()
    
    
    while line:
        print(line)
        line = fp.readline()
        
        

file=open(sys.argv[1],"r")     
wordcount={}

#------------------------------------------

# We are Storing each word with the Count.

for word in file.readline().split():
	if word not in wordcount:
        	wordcount[word] = 1
    	else:
        	wordcount[word] += 1
