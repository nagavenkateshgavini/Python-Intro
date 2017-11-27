import sys

filepath = sys.argv[1]
wordcount = {}

with open(filepath) as fp:
        line = fp.readline()
        while line:
            for word in line.split():
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
                line = fp.readline()

for k,v in wordcount.items():
    print k, v
