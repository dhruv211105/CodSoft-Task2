import random
import string

print("Welcome to the Password Generator")

length = int(input("Enter the desired password length: "))
print("\nChoose password complexity:")
print("1. Letters only (a-z, A-Z)")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Special Characters (!@#$%^&*)")
choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    characters = string.ascii_letters
elif choice == "2":
    characters = string.ascii_letters + string.digits
elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation
else:
    print("Invalid choice! Defaulting to letters + numbers + special characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))
print(f"\nGenerated Password: {password}")
