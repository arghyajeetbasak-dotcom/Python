
marks1=int(input("Enter marks in 1st subject : "))
marks2=int(input("Enter marks in 2nd subject : "))
marks3=int(input("Enter marks in 3rd subject : "))
totalpercent=((marks1+marks2+marks3)/300)*100
if(totalpercent>40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("Passed")
else:
    print("Failed")


spam1="Make a lot of money"
spam2="buy now"
spam3="subscribe this"
spam4="click this"
text=input("Enter the text : ")
if(spam1 in text or spam2 in text or spam3 in text or spam4 in text):
    print("This is a spam comment!")
else:
    print("This is not a spam comment")


username=input("Enter your username: ")
if(len(username)<10):
    print("Username contains less than 10 characters")
else:
    print("Username contains greater than 10 characters")


list=["Arghya","Rohan","Shuham","Sonali","Tara"]
name=input("Enter your name: ")
if(name in list):
    print("The name is present in the list")
else:
    print("Not")


post=input("Enter the post: ")
if("harry" in post.lower()):
    print("This post is talking about Harry")
else:
    print("This post is not talking about Harry")