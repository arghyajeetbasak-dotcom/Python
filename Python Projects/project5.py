import random
import string

print("--- Password Generator ---")

# Step 1: Take password length from user
length = int(input("Enter password length: "))

# Step 2: Define characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Randomly select characters
password = ''.join(random.choice(characters) for _ in range(length))

# Step 4: Show the result
print("Generated Password:", password)
