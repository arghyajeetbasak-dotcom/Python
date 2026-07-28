# METHOD 1
n=int(input("Enter the number: "))
l=[]
for i in range(1,n+1):
    if(n%i==0):
        l.append(i)
print(l)
# METHOD 2
for i in range(1,(n//2)+1):
    if(n%i==0):
        l.append(i)
l.append(n)
print(l)
# METHOD 3
from math import sqrt
for i in range(1,int(sqrt(n))+1):
    if(n%i==0):
        l.append(i)
        if(n//i!=i):
            l.append(n//i)
l.sort()
print(l)