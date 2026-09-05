arr=[55,32,-97,99,3,67]
largest=float("-inf")
for n in arr:
    if(n>largest):
        largest=n
        # OR
        largest=max(n,largest)
print(largest)