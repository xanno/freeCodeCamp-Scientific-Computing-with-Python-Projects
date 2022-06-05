class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spent = 0

    def deposit(self, amount, description=""):
        """
        A deposit method that accepts an amount and description. If no description is given, it should default to an
        empty string. The method should append an object to the ledger list in the form of
        {"amount": amount, "description": description}.
        """
        self.balance += amount
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(self, amount, description=""):
        """
        A deposit method that accepts an amount and description. If no description is given, it should default to an
        empty string. The method should append an object to the ledger list in the form of
        {"amount": amount, "description": description}.
        """
        if self.check_funds(amount):
            self.spent += amount
            self.balance -= amount
            self.ledger.append({"amount": float(-amount), "description": description})
            return True
        return False

    def transfer(self, amount, budget_category):
        """
        A transfer method that accepts an amount and another budget category as arguments.
        The method should add a withdrawal with the amount and the description
        "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category
         with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds,
         nothing should be added to either ledgers. This method should return True if the
        """
        if self.check_funds(amount):
            budget_category.deposit(amount, f"Transfer from {self.name}")
            self.withdraw(amount, f"Transfer to {budget_category.name}")
            return True
        return False

    def get_balance(self):
        """
        A get_balance method that returns the current balance of the budget category based on the deposits and
        withdrawals that have occurred.
        """
        return self.balance

    def check_funds(self, amount):
        """
        A check_funds method that accepts an amount as an argument.
        It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
        This method should be used by both the withdraw method and transfer method.
        """
        return self.balance >= amount

    def __str__(self) -> str:
        lst = [self.name.center(30, "*")]
        for item in self.ledger:
            desc = item["description"][:23]
            amount = f"{item['amount']:.2f}"[:7]
            lst_item = f"{desc}{amount.rjust(30 - len(desc))}"
            lst.append(lst_item)
        lst.append(f"Total: {self.balance:.2f}"[:30])

        return "\n".join(lst)

    def __repr__(self) -> str:
        return f"Category(\"{self.name}\")"


def create_spend_chart(categories):
    """
    Besides the Category class, create a function (outside the class) called create_spend_chart that takes a list of
    categories as an argument. It should return a string that is a bar chart.

    The chart should show the percentage spent in each category passed in to the function.
    The percentage spent should be calculated only with withdrawals and not with deposits.
    Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart
    should be made out of the "o" character. The height of each bar should be rounded down
    to the nearest 10. The horizontal line below the bars should go two spaces past the final bar.
    Each category name should be written vertically below the bar. There should be a title at the
    top that says "Percentage spent by category".
    """
    withdrawal = 0
    long_name = 0
    for category in categories:
        withdrawal += category.spent
        long_name = max(long_name, len(category.name))

    lst = []
    for i in range(10, 0, -1):
        w = f"{i}0|".rjust(4)
        lst.append(w)
    lst.append("0|".rjust(4))
    lst.reverse()

    for i in range(len(categories)):
        per = int((categories[i].spent / withdrawal) * 100)
        for r in range(len(lst)):
            if per >= r * 10:
                if i == 0:
                    lst[r] += " o"
                else:
                    lst[r] += "  o"
            else:
                if i == 0:
                    lst[r] += "  "
                else:
                    lst[r] += "   "
    lst.append("Percentage spent by category")
    lst.reverse()
    lst.append("    " + "-" * (len(categories) * 3 + 1))
    lst.extend([""] * long_name)
    for j in range(len(categories)):
        for i in range(long_name):
            name = categories[j].name
            if i < len(name):
                if j == 0:
                    lst[13 + i] += f"{name[i]:>6}"
                else:
                    lst[13 + i] += f"{name[i]:>3}"
            else:
                s = " "
                if j == 0:
                    lst[13 + i] += f"{s:>6}"
                else:
                    lst[13 + i] += f"{s:>3}"
    for j in range(len(lst)):
        if j == 12 or j == 0:
            continue
        for i in range(len(categories), 4):
            lst[j] += "  "

    return "\n".join(lst)


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))
print(auto.__repr__())
