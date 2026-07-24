n=int(input("Enter the number : "))
list=[n*i for i in range(1,11)]
with open("Tables.txt","a")as f:
    f.write(f"Table of {n} : {list}\n")