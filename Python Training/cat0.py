import sys

def reading():
    #print("In reading")
    f = open(sys.argv[1], "r")
    text = f.read()
    print(text)
    f.close()


### Writing to a Text File

def create_new():
    f = open(sys.argv[2], "w")
    content = sys.stdin.read()
    text = f.write(content)
    f.close()


def append_to_file():
    f = open(sys.argv[2], "a")
    content = sys.stdin.read()
    text = f.write(content)
    f.close()

def append_or_create():
    if(sys.argv[1]==">"):
        create_new()
    elif(sys.argv[1]==">>"):
        append_to_file()

if(len(sys.argv) == 2):
    #print("In if")
    reading()
elif(len(sys.argv) > 2):
    #print("In elif")
    append_or_create()
else:
    print("Please Give the Valid Input")
##print("End")
