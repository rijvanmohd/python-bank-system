class AccountRepository:
    def __init__(self):
        self.accounts = []

    def save_account(self, account):
        self.accounts.append(account)

    def find_account_by_id(self, account_id):
        for account in self.accounts:
            if account.account_id == account_id:
                return account

    def find_accounts_by_customer_id(self, customer_id):
        return [account for account in self.accounts if account.customer_id == customer_id]

class CustomerRepository:
    def __init__(self):
        self.customers = []

    def save_customer(self, customer):
        self.customers.append(customer)

    def find_customer_by_id(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer