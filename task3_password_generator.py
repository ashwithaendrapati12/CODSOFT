import random
import string

length = int(input("Enter password length: "))

letters = string.ascii_letters
numbers = string.digits
symbols = "!@#$%^&*()"

all_chars = letters + numbers + symbols

password = "".join(random.choice(all_chars) for i in range(length))

print("Generated Password:", password)