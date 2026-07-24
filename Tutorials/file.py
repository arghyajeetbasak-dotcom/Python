f=open("MyFile.txt","r")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()

f.close()

f=open("MyFile.txt","a")
f.write("\nArghyajeet loves coding")
f.close()

with open("MyFile.txt") as f:
    data=f.read()
    print(data)