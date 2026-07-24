n=int(input("Enter the number: "))
def neon(n):
    m=str(n*n)
    sum=0
    for item in m:
        sum+=int(item)
    if(sum==n):
        print(f"{n} is a neon number")
    else:
        print(f"{n} is not a neon number")
neon(n)