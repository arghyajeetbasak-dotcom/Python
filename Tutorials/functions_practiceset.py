def greatest(a,b,c):
    if(a>b and a>c):
        print("The greatest number is",a)
    elif(b>a and b>c):
        print("The greatest number is",b)
    else:
        print("The greatest number is",c)
greatest(78,45,98)


def convert(celsius):
    f=(9/5)*celsius+32
    return f
celsius=int(input("Enter temperature in Celsius: "))
print(convert(celsius))


def sum(n):
    if(n==1):
        return 1
    return n + sum(n-1)
n=int(input("Enter n: "))
print(f"Sum of first {n} natural numbers is {sum(n)}")


def pattern(n):
    for i in range(1,n+1):
        print("*"*(n+1-i),end="")
        print("")
n=int(input("Enter n: "))
pattern(n)


def conversion(inch):
    cm=inch*2.54
    print(f"{inch} inch = {cm} cm")
inch=float(input("Enter inch: "))
conversion(inch)


def remove(list):
    word=input("Enter the word to remove: ")
    n=[]
    for item in list:
        if(not(item==word)):
            n.append(item.strip(word))
    print(n)
list=["Arghya","Shubham","Tanisha","Nikhil","Sonia","am"]
remove(list)


def multiplication(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
n=int(input("Enter the number: "))
multiplication(n)