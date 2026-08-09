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