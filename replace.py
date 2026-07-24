words=["Donkey","bad","ganda"]
with open("File.txt")as f:
    content=f.read()
    for word in words:
       content=content.replace(word,"#"*len(word))
with open("File.txt","w")as f:
    f.write(content)