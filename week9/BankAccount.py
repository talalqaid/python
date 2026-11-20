class BankAccount:
    def __init__(self, customer_name, account_number, opening_balance, overdraft_limit):
        self.customer_name = customer_name
        self.account_number = account_number
        self.opening_balance = opening_balance
        self.overdraft_limit = -abs(overdraft_limit)
        self.current_balance = opening_balance

    def print_details(self):
        print('Customer Name:', self.customer_name)
        print('Account Number:', self.account_number)
        print('Opening Balance:', self.opening_balance)
        print('Overdraft Limit:', self.overdraft_limit)

    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
        else:
            print('Amount must be positive.')
        print('The current balance is', self.current_balance)

    def check_overdraft_limit(self, amount):
        return self.current_balance - amount >= self.overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print('Amount must be positive.')
        elif self.check_overdraft_limit(amount):
            self.current_balance -= amount
        else:
            print('Overdraft Exceeded!')
            print('This transaction has not gone through')
        print('The current balance is', self.current_balance)
