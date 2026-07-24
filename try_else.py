try:
    with open("Kejra.txt")as f:
        content=f.read()
        print(content)
except:
    print("File not found bro")
finally:
    print("Thank You")