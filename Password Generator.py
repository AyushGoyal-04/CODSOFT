import random
import string

def generate_password(length, lowercase=True, uppercase=True, digits=True, special=True):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation

    char = ""
    if lowercase:
        char += lowercase
    if uppercase:
        char += uppercase
    if digits:
        char += digit
    if special:
        char += special
    if not char:
        print("Error: At least one character set must be selected.")
        return None
    
    password = "".join(random.choice(char) for _ in range(length))
    return password

def main():
    print("====== Password Generator ======")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Password length must be a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nPassword complexity options:")
    lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include numbers? (y/n): ").lower() == 'y'
    special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, lowercase, uppercase, digits, special)
    
    if password:
        print("\nYour generated password is:")
        print(f"→ {password}")
        strength = "Weak"
        if length >= 12 and sum([lowercase, uppercase, digits, special]) >= 3:
            strength = "Strong"
        elif length >= 8 and sum([lowercase, uppercase, digits, special]) >= 2:
            strength = "Medium"   
        print(f"Password strength: {strength}")
    
if __name__ == "__main__":
    main()