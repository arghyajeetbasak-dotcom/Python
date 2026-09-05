arr=[55,32,97,-55,45]
largest=float("-inf")
slargest=float("-inf")
for n in arr:
    if n>largest:
        slargest=largest
        largest=n
    elif n>slargest and n!=largest:
        slargest=n
print(slargest)