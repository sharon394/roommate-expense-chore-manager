class User:
    def __init__(self, user_id, name, points=0):
        self.user_id = user_id
        self.name = name
        self.points = points  # Karma points earned by completing chores

    def __repr__(self):
        return f"User({self.name}, Karma Points: {self.points})"


class Expense:
    def __init__(self, expense_id, payer_id, amount, description, split_among):
        self.expense_id = expense_id
        self.payer_id = payer_id
        self.amount = float(amount)
        self.description = description
        self.split_among = split_among  # List of user_ids

    def calculate_split(self):
        if not self.split_among:
            return 0
        return round(self.amount / len(self.split_among), 2)


class Chore:
    def __init__(self, chore_id, title, assigned_to, weight=1, is_completed=False):
        self.chore_id = chore_id
        self.title = title
        self.assigned_to = assigned_to
        self.weight = weight  # Chore difficulty weight (1-5)
        self.is_completed = is_completed
