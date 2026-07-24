def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
n=int(input("Enter value of n : "))
print(f"Sum of first {n} natural numbers is {sum(n)}")