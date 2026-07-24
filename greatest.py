def greatest(a,b,c):
    if(a>b and a>c):
        print("Greatest number is",a)
    elif(b>a and b>c):
        print("Greatest number is",b)
    elif(c>a and c>b):
        print("Greatest number is",c)
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
greatest(a,b,c)