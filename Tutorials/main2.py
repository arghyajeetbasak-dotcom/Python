import random

n=random.randint(1,100)
guess=0
user=-1
while(user!=n):
    user=int(input("Guess a number: "))
    if(user>n):
        print("Lower number please")
    elif(user<n):
        print("Higher number please")
    guess+=1
print(f"You have guessed the number {n} correctly in {guess} attempts")
