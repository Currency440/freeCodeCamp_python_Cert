class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = f"{item['amount']:.2f}"[:7]
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate spending per category (only negative amounts, excluding transfers out)
    # freeCodeCamp logic counts all withdrawals as spending
    spent_amounts = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent_amounts.append(spent)
    
    total_spent = sum(spent_amounts)
    
    # Calculate percentages rounded down to the nearest 10
    percentages = []
    for spent in spent_amounts:
        if total_spent == 0:
            percentages.append(0)
        else:
            percentages.append(int((spent / total_spent) * 10) * 10)

    # Build the bar chart string
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percent in percentages:
            chart += "o  " if percent >= i else "   "
        chart += "\n"
        
    # Add horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # Add category names vertically
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += f"{name[i]}  "
        if i < max_len - 1:
            chart += "\n"
            
    return chart