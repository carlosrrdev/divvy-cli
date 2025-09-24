import os
import platform

__title__ = "Divvy-CLI"
__version__ = "0.1.0"
__author__ = "Carlos Rodriguez"


def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def main():
    clear_console()
    print("Welcome to Divvy-CLI!")


if __name__ == "__main__":
    main()
