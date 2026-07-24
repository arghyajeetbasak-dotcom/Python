str="kakakakakak"
reverse=""
for item in str:
    reverse=item+reverse
if(str==reverse):
    print("The string is palindrome")
else:
    print("The string is not palindrome")