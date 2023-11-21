from models.repository import AccountRepository, CustomerRepository
from utils.account_utils import CreateAccount
from utils.statement import GenerateAccountStatement
from utils.transaction import MakeTransaction

account_repository = AccountRepository()
customer_repository = CustomerRepository()

create_account = CreateAccount(account_repository, customer_repository)
make_transaction = MakeTransaction(account_repository)
generate_account_statement = GenerateAccountStatement(account_repository)

# creating account
account = create_account.create_account('account123', 'customer123', '1234567890', '1000', 'test user','user@test.com', '1234567890')

# making transaction
make_transaction.make_transaction(account.account_id, 1000, 'deposit')

# generating account statement
print(generate_account_statement.generate_account_statement(account.account_id))