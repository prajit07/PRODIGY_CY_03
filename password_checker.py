import re
import getpass

def check_password_strength(password):
    # Criteria checking
    length = len(password) >= 8
    uppercase = bool(re.search(r'[A-Z]', password))
    lowercase = bool(re.search(r'[a-z]', password))
    number = bool(re.search(r'\d', password))
    special_char = bool(re.search(r'[@$!%*?&#\W]', password))  # Allow any non-alphanumeric character

    # Evaluating strength
    strength= sum([length, uppercase, lowercase, number, special_char])

    # Feedback based on points
    if strength == 5:
        return "Your password is very strong."
    elif strength >= 3:
        return "Your password is strong."
    elif strength == 2:
        return "Your password is medium."
    else:
        return "Your password is weak. Please choose a strong password."

def main():
    print("_____________________________________________")
    print("_____________________________________________")
    print(" ____     ___    ___   ____     ___     ____ ")
    print("|  _ \   / _ \  |_ _| |  _ \   / _ \   / ___|")
    print("| |_) | | | | |  | |  | | | | | | | | | |  _ ")
    print("|  __/  | |_| |  | |  | |_| | | |_| | | |_| |")
    print("|_|      \___/  |___| |____/   \___/   \____|")
    print("_____________________________________________")
    print("_____________________________________________")
    print("\n")
    print("Password strength checker")
    print("/"*90)
    print("**Note:**This program will check your password strength and provide you with feedback. \nAnd this a very simple program to check your password strength.\nDon't use this program for real password checking.")
    print("/"*90)
    while True:
        password = getpass.getpass("Enter your password: ")
        if password:
            feedback = check_password_strength(password)
            print(feedback)
            again = input("Do you want to check another password? (y/n): ")
            if again.lower() != 'y':
                print("Goodbye!")
                break
        else:
            check_password_strength(password)

main()