from uuid import uuid4, UUID


class Divvy:
    """
    Divvy class serves as the parent class for Divvy-Split and Divvy-Up.
    """

    def __init__(self):
        members = []
        expenses = []
        self.members = members
        self.expenses = expenses

    def add_member(self, member_name: str) -> UUID:
        """
        Add a new member to the list of members. New members are assigned a unique ID on creation.
        :param member_name:
        :return: UUID instance of the new member.
        """
        member_id = uuid4()
        self.members.append({
            "id": str(member_id),
            "name": member_name
        })
        return member_id

    def add_expense(self, expense_name: str, expense_amount: float) -> UUID:
        """
        Add a new expense to the list of expenses. New expenses are assigned a unique ID on creation.
        :param expense_name:
        :param expense_amount:
        :return: UUID instance of the new expense.
        """
        expense_id = uuid4()
        self.expenses.append({
            "id": str(expense_id),
            "name": expense_name,
            "amount": expense_amount
        })
        return expense_id

    def remove_member(self, member_id: str):
        """
        Removes a member from the list of members based on the member ID.
        :param member_id: The unique ID of the member to be removed.
        :return: Return True if the member was removed, False otherwise.
        """
        for member in self.members:
            if member["id"] == member_id:
                self.members.remove(member)
                return True
        return False

    def remove_expense(self, expense_id: str):
        """
        Removes an expense from the list of expenses based on the expense ID.
        :param expense_id: The unique ID of the expense to be removed.
        :return: Return True if the expense was removed, False otherwise.
        """
        for expense in self.expenses:
            if expense["id"] == expense_id:
                self.expenses.remove(expense)
                return True
        return False

    def get_members(self):
        """
        Returns the list of members.
        :return: List of member dictionaries.
        """
        return self.members

    def get_expenses(self):
        """
        Returns the list of expenses.
        :return: List of expense dictionaries.
        """
        return self.expenses
