n=int(input("Enter the number: "))
m=str(n)
def palindrome(n):
    reverse=m[::-1]
    if(int(reverse)==n):
        print(f"{n} is a palindrome number")
    else:
        print(f"{n} is not a palindrome number")
palindrome(n)