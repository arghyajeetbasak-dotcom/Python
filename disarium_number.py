n=int(input("Enter the number: "))
m=str(n)
def disarium(n):
    position=1
    sum=0
    for digit in m:
        sum=sum+int(digit)**position
        position+=1
    if(sum==n):
        print(f"{n} is a disarium number")
    else:
        print(f"{n} is not a disarium number")
disarium(n)