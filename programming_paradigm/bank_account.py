class BankAccount:
    def __init__(self, account_balance=0):
        self.__account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
        
    def withdraw(self, amount):
        if self.__account_balance > amount:
            self.__account_balance -= amount
            return True
        return False
        
    def display_balance(self):
        print(f"Current Balance: \N{DOLLAR SIGN}{self.__account_balance:.2f}")
        

                

               


