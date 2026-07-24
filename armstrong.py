n=int(input("Enter a number : "))
Digits=len(str(n))
def armstrong(n):
    sum_of_powers=0
    for digit in str(n):
        sum_of_powers+=int(digit)**Digits
    if(sum_of_powers==n):
        print(f"{n} is an armstrong number")
    else:
        print(f"{n} is not an armstrong number")
armstrong(n)