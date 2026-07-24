import random
print("Welcome to the Number Guessing Game!")

computer=random.randint(1,100)
attempts=0
while True:
    guess=int(input("Guess the number(1-100) : "))
    attempts+=1
    if(guess<1 or guess>100):
        print("Please enter a valid number between 1 and 100")
    elif(guess<computer):
        print("Higher number please")
    elif(guess>computer):
        print("Lower number please")
    elif(guess==computer):
        print(f"Correct! You guessed the number {computer} in {attempts} attempts")
        break
    else: 
        print("Invalid input")
