import sys

### Rading From Text File.

def reading():
    f = open(sys.argv[1], "r")
    text = f.read()
    print(text)
    f.close()

# End of Reading.

#-----------------------------------------------

# Writing, Appending to a Text File

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
    else:
        print("Only Two options '>', '>>' ")

# End of Writing.

#-----------------------------------------------------       

# The Program Starts From here
        
if(len(sys.argv) == 2):
    reading()
elif(len(sys.argv) > 2):
    append_or_create()
else:
    print("Please Give the Valid Input")



