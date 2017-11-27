import sys
wordcount={}
with open(sys.argv[1]) as file:
    for line in file:
        for word in line.split():
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
for k,v in wordcount.items(): print (k, v)
