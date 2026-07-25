num=int(input("Enter the number: "))
m=str(num)
def strong(num):
    sum=0
    for item in m:
        f=1
        for i in range(1,int(item)+1):
            f=f*i
        sum=sum+f
    if(sum==num):
        print(f"{num} is a strong number")
    else:
        print(f"{num} is not a strong number")
strong(num)