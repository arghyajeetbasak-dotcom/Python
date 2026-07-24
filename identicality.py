with open("File1.txt") as f:
    content1=f.read()
with open("File2.txt") as f:
    content2=f.read()
if(content1==content2):
    print("The two files are identical")
else:
    print("The two files are not identical")