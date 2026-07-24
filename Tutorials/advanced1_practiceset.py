try:
    with (open("File1.txt") as f1, open("File2.txt") as f2, open("File3.txt") as f3):
        content1=f1.read()
        content2=f2.read()
        content3=f3.read()
except Exception as e:
    print(e)

l=[13,21,45,77,89,1,55]
for i,item in enumerate(l):
    if(i==2 or i==4 or i==6):
        print(f"The {i+1} element is {item}")

n=int(input("Enter a number: "))
l=[n*i for i in range(1,11)]
print(l)
with open("Tables.txt","a") as f:
    f.write(f"Table of {n} = {l}\n")

try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Infinite")