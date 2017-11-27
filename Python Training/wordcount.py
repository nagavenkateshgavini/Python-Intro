import sys, collections, pprint
pprint.pprint(collections.Counter(word.lower().strip() 
for line in (sys.stdin if len(sys.argv) < 2 else open(sys.argv[1])) 
for word in line[:-1].split()).most_common())
