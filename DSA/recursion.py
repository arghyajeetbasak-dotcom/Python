# count=0
# def func():
#     global count
#     if(count==4):
#         return
#     count+=1
#     func()
#     print("Arghyajeet")
# func()

def display(n):
    if(n==0):
        return
    display(n-1)
    print(n)
display(5)

def recurse(i,n):
    if(i>n):
        return
    print(i)
    recurse(i+1,n)
recurse(1,12)

def tailrecurse(n):
    if(n==0):
        return
    tailrecurse(n-1)
    print(n)
tailrecurse(9)

def rev(n):
    if(n==0):
        return
    print(n)
    rev(n-1)
rev(9)

def tailrev(i,n):
    if(i>n):
        return
    tailrev(i+1,n)
    print(i)
tailrev(1,7)