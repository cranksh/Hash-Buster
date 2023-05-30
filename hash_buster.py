import hashlib

import itertools

import pyfiglet

from colorama import Fore, Style

def display_menu():

    menu_title = " Hash Buster "

    menu_options = [

        {"key": "1", "description": "Generate hash", "action": generate_hash},

        {"key": "2", "description": "Decrypt hash", "action": decrypt_hash},

        {"key": "Q", "description": "Quit", "action": quit_program}

    ]

    # Print PyFiglet logo

    logo = pyfiglet.figlet_format(menu_title)

    print(Fore.YELLOW + logo + Style.RESET_ALL)

    # Print menu box

    print("-" * 30)

    print(" MENU ")

    print("-" * 30)

    for option in menu_options:

        print(f" [{option['key']}] {option['description']}")

    print("-" * 30)

    # Prompt for user choice

    choice = input("Enter your choice: ").upper()

    # Execute chosen action

    for option in menu_options:

        if choice == option['key']:

            option['action']()

            break

    else:

        print(Fore.RED + "Invalid choice!" + Style.RESET_ALL)

def generate_hash():

    print("=== Generate Hash ===")

    plaintext = input("Enter the plaintext to hash: ")

    # Hash the plaintext using MD5 algorithm

    hashed_text = hashlib.md5(plaintext.encode()).hexdigest()

    # Print the hashed result

    print(Fore.GREEN + "Hashed Result: " + hashed_text + Style.RESET_ALL)

def decrypt_hash():

    print("=== Decrypt Hash ===")

    hashed_text = input("Enter the hashed text: ")

    charset = input("Enter the character set to use: ")

    max_length = int(input("Enter the maximum length of plaintext to try: "))

    print(Fore.YELLOW + "Decrypting..." + Style.RESET_ALL)

    # Try to decrypt the hash

    for length in range(1, max_length + 1):

        for combination in itertools.product(charset, repeat=length):

            plaintext = ''.join(combination)

            hashed_guess = hashlib.md5(plaintext.encode()).hexdigest()

            if hashed_guess == hashed_text:

                print(Fore.GREEN + "Plaintext Found: " + plaintext + Style.RESET_ALL)

                return

    # If no match found

    print(Fore.RED + "Plaintext not found within the specified length and character set!" + Style.RESET_ALL)

def quit_program():

    print("Goodbye!")

    exit()

# Run the hash buster

while True:

    display_menu()

# Made with love
