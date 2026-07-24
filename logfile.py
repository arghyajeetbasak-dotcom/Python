with open("log.txt")as f:
    content=f.readlines()
lineno=1
for line in content:
    if("python"in line):
        print(f"Python is present in line:{lineno}")
        break
    lineno+=1
else:
    print(f"Python is not present")    