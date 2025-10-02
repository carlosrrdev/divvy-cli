from .divvy import Divvy
from .clear_console import clear_console
from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Confirm


class DivvySplit(Divvy):
    """
    DivvySplit class inherits from Divvy and provides functionality for splitting expenses evenly among members.
    """

    def __init__(self):
        super().__init__()

    def calc_split_amount(self):
        self.console.rule("[bold cyan]Results[/bold cyan]", align="left")
        total_members = len(self.members)
        total_expenses = len(self.expenses)
        expenses_total = self.get_expense_total()
        split_amount = round(expenses_total / total_members, 2)
        self.console.print(f"Total members: {total_members}")
        self.console.print(f"Total expenses: {total_expenses}")
        self.console.print(f"Total expenses amount: ${expenses_total}")
        self.console.print(f"\n[bold bright_green]Split amount: ${split_amount}[/bold bright_green]\n")
        save_file = Confirm.ask("Do you want to save the split amount to a file?")
        if save_file:
            with open("split_amount.txt", "w") as file:
                file.write(f"Split amount: ${split_amount}")

       

    def show_tables(self):
        members_table = Table(title="Members", box=box.ASCII2)
        members_table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        members_table.add_column("Name", style="magenta")
        for member in self.members:
            members_table.add_row(member["id"], member["name"])

        expenses_table = Table(title="Expenses", box=box.ASCII2)
        expenses_table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        expenses_table.add_column("Name", style="magenta")
        expenses_table.add_column("Amount", justify="right", style="green")
        for expense in self.expenses:
            expenses_table.add_row(expense["id"], expense["name"], str(expense["amount"]))

        print()
        self.console.print(members_table)
        self.console.print(expenses_table)
        print()
        self.calc_split_amount()


    def initialize(self):

        # TODO add validation for members and expenses. Check to make sure there is at least two members and one expense.

        clear_console()
        self.console.print("[bold cyan]Creating new Divvy Split[/bold cyan]\n")
        self.console.print(
            Panel("A divvy split is one where all expenses are tallied up and split evenly among members.",
                  box=box.ASCII2))
        print()
        self.console.rule("[bold cyan]Step 1. Add members[/bold cyan]", align="left")
        continue_adding_members = True
        while continue_adding_members:
            member_name = self.console.input("\n[yellow]Enter the name of the new member: [/yellow]")
            if member_name:
                self.add_member(member_name)
                self.console.print(f"[green]> {member_name} added successfully.[/green]\n")
                cnt = Confirm.ask("Continue adding members?")
                if cnt:
                    continue
                else:
                    continue_adding_members = False
            else:
                continue_adding_members = False
        print()
        self.console.rule("[bold cyan]Step 2. Add expenses[/bold cyan]", align="left")
        continue_adding_expenses = True
        while continue_adding_expenses:
            expense_name = self.console.input("\n[yellow]Enter the name of the new expense: [/yellow]")
            # TODO verify that expense_amount is a valid float.
            expense_amount = self.console.input(f"[yellow]Enter the amount for {expense_name}: $[/yellow]")
            if expense_name and expense_amount:
                self.add_expense(expense_name, float(expense_amount))
                self.console.print(f"[green]> {expense_name} added successfully.[/green]\n")
                cnt = Confirm.ask("Continue adding expenses?")
                if cnt:
                    continue
                else:
                    continue_adding_expenses = False
            else:
                continue_adding_expenses = False
        self.show_tables()