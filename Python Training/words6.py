import sys
wordcount={}
with open(sys.argv[1]) as fobj:
    for line in fobj:
        for word in line.split(" "):
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
print(wordcount)



