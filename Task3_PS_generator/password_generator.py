import random
import string

def generate_password(length=12, use_letters=True, use_digits=True, use_symbols=True):
    characters = ""
    # include letters and/or digits when requested
    if use_letters + use_digits:
        characters = string.ascii_letters + string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be enabled.")
    return "".join(random.choice(characters) for i in range(length))

def main():
    try:
        length_input = input("Enter password length (default 12): ").strip()
        length = int(length_input) if length_input else 12
    except ValueError:
        print("Invalid length entered. Using default length 12.")
        length = 12

    password = generate_password(length=length)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
