n=int(input("Enter the number : "))
m=str(n)
digits=len(m)
sum=0
for item in m:
    sum+=int(item)**digits
if(sum==n):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")