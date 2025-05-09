import random
import string

def generate_password(length):
    # Define character pools for password complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character pools
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Ensure the password contains at least one character from each category
    password_characters = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    remaining_length = length - 4
    if remaining_length > 0:
        password_characters += random.choices(all_characters, k=remaining_length)

    # Shuffle the list to prevent predictable sequences
    random.shuffle(password_characters)

    # Join the list into a string to form the password
    password = ''.join(password_characters)
    return password

def main():
    # Prompt user for desired password length
    try:
        length = int(input("Enter the desired password length: "))
        if length < 4:
            print("Password length should be at least 4 to include all character types.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()