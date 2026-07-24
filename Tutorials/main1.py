import random

compvalue=random.randint(-1,1)

you=input("Enter your choice: ")

youDict={"s":-1,
         "w":0,
         "g":1}

Dict={-1:"Snake",
          0:"Water",
          1:"Gun"}
younum=youDict[you]
user=Dict[younum]
computer=Dict[compvalue]
print(f"You chose {user} & Computer chose {computer}")

if(younum==compvalue):
    print("Its a draw!")
else:
    if(younum==-1 and compvalue==1):
        print("You lose")
    elif(younum==1 and compvalue==-1):
        print("You win")
    elif(younum==-1 and compvalue==0):
        print("You win")
    elif(younum==0 and compvalue==-1):
        print("You lose")
    elif(younum==0 and compvalue==1):
        print("You lose")
    elif(younum==1 and compvalue==0):
        print("You win")
    else:
        print("Invalid input!")