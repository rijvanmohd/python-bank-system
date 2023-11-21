from models.account import Account
from models.customer import Customer

class CreateAccount:
    def __init__(self, account_repository,customer_repository):
        self.account_repository = account_repository
        self.customer_repository = customer_repository

    def create_account(self, account_id, customer_id, account_number, balance, name, email, phone_number):
        account = Account(account_id, customer_id, account_number, balance)
        self.account_repository.save_account(account)

        customer = Customer(customer_id, name, email, phone_number)
        self.customer_repository.save_customer(customer)
        return account