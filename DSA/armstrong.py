n=int(input("Enter the number: "))
m=n
sum=0
while(m>0):
    digit=m%10
    m=m//10
    sum+=digit**len(str(n))
if(sum==n):
    print(f"{n} is an armstrong number")
else:
    print(f"{n} is not an armstrong number")