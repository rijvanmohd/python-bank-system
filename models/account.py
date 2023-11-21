class Account:
    def __init__(self, account_id, customer_id, account_number, balance):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if not isinstance(amount, int):
            raise ValueError("Amount must be an integer")
        self.balance = int(self.balance) +int(amount)

    def withdraw(self, amount):
        if int(amount) > int(self.balance):
            raise ValueError("Insufficient balance")
        self.balance = int(self.balance) - int(amount)

    def get_balance(self):
        return int(self.balance)