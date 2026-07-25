n=int(input("Enter the number: "))
m=str(n)
def spynumber():
    sum=0
    product=1
    for digit in m:
        sum=sum+int(digit)
        product=product*int(digit)
    if(sum==product):
        print(f"{n} is a spy number")
    else:
        print(f"{n} is not a spy number")
spynumber()