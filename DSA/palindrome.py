n=int(input("Enter the number: "))
m=n
reverse=0
while(m>0):
    digit=m%10
    m=m//10
    reverse=reverse*10+digit
if(reverse==n):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")