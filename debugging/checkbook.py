#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        """Initialise le solde du compte à 0.0."""
        self.balance = 0.0

    def deposit(self, amount):
        """Effectue un dépôt sur le compte."""
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """Effectue un retrait du compte."""
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Affiche le solde actuel du compte."""
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """Fonction principale pour interagir avec l'utilisateur et effectuer des opérations sur le compte."""
    cb = Checkbook()  # Crée un objet Checkbook
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the deposit.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the withdrawal.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
