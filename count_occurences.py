word=input("Enter word: ")
with open("words.txt") as f:
    content=f.read()
    print(f"{word} occurs {content.count(word)} times")
