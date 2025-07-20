import random
import string

def generate_password(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=== Password Generator ===")

while True:
    try:
        length = int(input("Enter password length: "))
        if length < 6:
            print("Enter a length of at least 6 for strong password.")
        if length > 32:
            print("Enter a length of at most 32 for strong password.")    
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

password = generate_password(length)
print("\nYour generated password is:", password)