numbers=[22,45,78,2,19]
try:
    index=int(input("Enter the index: "))
    print(f"The element at index {index} is {numbers[index]}")
except IndexError:
    print("Please enter a valid index")