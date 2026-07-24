# 1
# with open("poems.txt") as f:
#     data=f.read()
#     if("twinkle" in data):
#         print("The given text contains the word twinkle")
#     else:
#         print("The given text does not contain the word twinkle")

# import random
# def game():
#     score=random.randint(1,100)
#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore==""):
#             hiscore=0
#         else:
#             hiscore=int(hiscore)
#     print(f"Your score : {score}")
#     if(score>hiscore):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
# game()

def generateTable(n):
    table=""
    for i in range(1,11):
        table+=(f"{n} X {i} = {n*i}\n")
    with open(f"Files/Table {n}.txt","w") as f:
        f.write(table)
for i in range(2,21):
    generateTable(i)

# with open("MyFile.txt") as f:
#     content=f.read()
#     contentNew=content.replace("donkey","######")
# with open("MyFile.txt","w") as f:
#     f.write(contentNew)

# list=["donkey","good","pretty"]
# with open("MyFile.txt","r") as f:
#     content=f.read()
# for word in list:
#     content=content.replace(word,"#"*len(word))
# with open("MyFile.txt","w") as f:
#     f.write(content)

# with open("this.txt") as f:
#     content=f.read()
# with open("this2.txt","w") as f:
#     f.write(content)

# with open("MyFile.txt") as f:
#     content=f.read()
# with open("MyFile2.txt") as f:
#     content2=f.read()
# if(content==content2):
#     print("The two files are identical")
# else:
#     print("The two files are not identical")
