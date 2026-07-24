num=int(input("Enter the number: "))
for i in range(1,11):
    print(num*i)

l=["Harry","Soham","Sachin","Rahul"]
for item in l:
    if(item.startswith("S")):
        print(f"Hello {item}")

num=int(input("Enter the number: "))
i=1
while(i<11):
    print(num*i)
    i+=1

num=int(input("Enter the number : "))
for i in range(2,num):
    if(num%i==0):
        print("The number is not prime")
        break;
else:
    print("The number is prime")

n=int(input("Enter value of n: "))
s=0
i=1
while(i<n+1):
    s=s+i
    i+=1
print(f"The sum of first {n} natural numbers is {s}")

num=int(input("Enter the number: "))
f=1
for i in range(1,num+1):
    f=f*i
print(f"Factorial of {num} is {f}")

n=int(input("Enter n: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print("")

n=int(input("Enter n: "))
for i in range(1,n+1):
    print("*"*i,end="")
    print("")

n=int(input("Enter n: "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
        print("")

n=int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")
