from divvy import DivvySplit, clear_console
from rich.console import Console

__title__ = "Divvy-CLI"
__version__ = "0.1.0"
__author__ = "Carlos Rodriguez"

console = Console()


def display_menu():
    console.print(f"[bold cyan]{__title__}[/bold cyan]\nby {__author__}\n")
    console.rule("[bold cyan] What would you like to do? [/bold cyan]", align="left", style="bold cyan")
    console.print("1.[yellow]Split expenses evenly among members.[/yellow]")
    console.print("2.[yellow]Divvy up expenses based on individual contributions. [/yellow]")
    console.print("3.[yellow]Exit. [/yellow]\n")
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
            console.print("[bright_red]Invalid choice. Please enter a valid choice.[/bright_red]\n")

def create_divvy_split():
    clear_console()
    new_divvy = DivvySplit()
    new_divvy.initialize()


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
