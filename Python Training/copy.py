import sys
with open(sys.argv[1],"r") as f:
	with open(sys.argv[2], "a") as f1:
		for line in f:
			f1.write(line)
f.close()
f1.close()
