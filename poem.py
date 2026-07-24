with open("poems.txt") as f:
    if("twinkle" in f.read()):
        print("The text contains the word twinkle")
    else:
        print("Not")