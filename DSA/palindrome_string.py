str=input("Enter a string: ")
def palindrome(str,left,right):
    if(left>=right):
        print(f"{str} is palindrome string")
        return
    if(str[left]==str[right]):
        palindrome(str,left+1,right-1)
    else:
        print(f"{str} is not palindrome string")
        return
palindrome(str,0,len(str)-1)