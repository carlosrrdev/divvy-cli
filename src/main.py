import os
import platform
from divvy import DivvySplit

__title__ = "Divvy-CLI"
__version__ = "0.1.0"
__author__ = "Carlos Rodriguez"


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def display_menu():
    print(f"{__title__} - v{__version__}\nby {__author__}\n")
    print("Welcome to Divvy, an expense splitting tool.\nWhat would you like to do?\n")
    print("1. Split expenses evenly among members.")
    print("2. Divvy up expenses based on individual contributions.")
    print("3. Exit.\n")
    is_valid_choice = False
    while not is_valid_choice:
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3"]:
            is_valid_choice = True
            if choice == "1":
                create_divvy_split()
            elif choice == "2":
                create_divvy_up()
            elif choice == "3":
                exit_program()
        else:
            print("Invalid choice. Please enter a valid choice.\n")

def create_divvy_split():
    clear_console()
    new_divvy = DivvySplit()
    print("Creating a new Divvy Split\n")
    new_divvy.initial_steps()
    print(new_divvy.get_members())
    print(new_divvy.get_expenses())


def create_divvy_up():
    clear_console()
    print("Creating a new Divvy Up...")

def exit_program():
    print("\nExiting Divvy-CLI...\nBye!")

def main():
    clear_console()
    display_menu()

if __name__ == "__main__":
    main()
