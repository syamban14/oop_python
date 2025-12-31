class BankAccount:
    __no = ""
    __balance = 0

    def __init__(self, no):
        self.__no = no

    @property
    def no(self):
        return self.__no
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough balance")
        self.__balance -= amount

account1 = BankAccount("saya")
print("Account No:", account1.no)
print("Initial Balance:", account1.balance)

account1.deposit(500)
print("Balance after deposit:", account1.balance)

account1.withdraw(500)
print("Balance after withdrawal:", account1.balance)