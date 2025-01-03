class bank:
    def __init__(self,account_number,name,account_type,balance):
        self.account_number=account_number
        self.name=name
        self.account_type=account_type
        self.balance=balance

    def deposit(self,amount):
        if amount > 0:
            self.balance+=amount
            return f"amount deposited successfully,new balance{self.balance}"
        else:
            return "amount should be greater than 0"

    def withdraw(self,amount):
        if amount > 0:
            if amount<=self.balance:
                self.balance-=amount
                return f"amount successfully withdrawn,new balance{self.balance}"
            else:
                return f"insufficient balance,balance{self.balance}"
        else:
            return "amount should be greater than 0"

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"account name:{self.name} \n account type:{self.account_type} \n account number:{self.account_number} \n balance:{self.balance} \n"

def display_menu():
    print("\n---Bank account menu---\n")
    print("1.display account details")
    print("2.display your balance")
    print("3.deposit")
    print("4.withdraw")
    print("5.exit")

    print("welcome to bank")


account = bank(987654321, "shamroodh", "savings", 500)


if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("enter your choice (1-5):")

        if choice == '1':
            print(account)

        elif choice == '2':
            print(f"balance:{account.get_balance()}")

        elif choice == '3':
            amount=float(input("enter the amount:"))
            print(f"deposited amount:{account.deposit(amount)}")

        elif choice == '4':
            amount=float(input("enter the amount:"))
            print(f"withdrawn amount:{account.withdraw(amount)}")

        elif choice == '5':
            print("thank you for choosing our bank")
            break

        else:
            print("invalid option!select from(1-5)")
