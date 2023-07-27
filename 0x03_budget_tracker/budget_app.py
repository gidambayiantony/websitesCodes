class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount
        return f"Deposited {amount} into {self.category} category."

    def withdraw(self, amount):
        if self.amount >= amount:
            self.amount -= amount
            return f"Withdrew {amount} from {self.category} category."
        else:
            return f"Insufficient funds in {self.category} category."

    def check_balance(self):
        return f"Balance in {self.category} category: {self.amount}"


def main():
    # Sample usage
    categories = ['Food', 'Transportation', 'Entertainment']
    budget_list = []

    for category in categories:
        amount = float(input(f"Enter initial amount for {category} category: "))
        budget = Budget(category, amount)
        budget_list.append(budget)

    while True:
        print("\nBudget Tracking App Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            category = input("Enter category to deposit into: ")
            amount = float(input("Enter amount to deposit: "))
            for budget in budget_list:
                if budget.category == category:
                    print(budget.deposit(amount))
                    break
            else:
                print("Category not found!")

        elif choice == 2:
            category = input("Enter category to withdraw from: ")
            amount = float(input("Enter amount to withdraw: "))
            for budget in budget_list:
                if budget.category == category:
                    print(budget.withdraw(amount))
                    break
            else:
                print("Category not found!")

        elif choice == 3:
            category = input("Enter category to check balance: ")
            for budget in budget_list:
                if budget.category == category:
                    print(budget.check_balance())
                    break
            else:
                print("Category not found!")

        elif choice == 4:
            print("Exiting the Budget Tracking App.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

