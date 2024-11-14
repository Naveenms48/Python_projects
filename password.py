#Random Password Generator
import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special):
    character_pool = ""
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4.")
                continue
            
            use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
            use_special = input("Include special characters? (y/n): ").lower() == 'y'
            
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special)
            print(f"Generated Password: {password}")
            
            another = input("Generate another password? (y/n): ").lower()
            if another != 'y':
                print("Goodbye!")
                break
        except ValueError as e:
            print(e)


main()
