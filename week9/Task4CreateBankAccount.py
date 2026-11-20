from BankAccount import BankAccount

name = input('Enter customer Name: ')
number = input('Enter Account Number: ')
opening_balance = float(input('Enter Opening Balance: '))
overdraft_limit = float(input('Enter Overdraft Limit: '))

account = BankAccount(name, number, opening_balance, overdraft_limit)
print('\nAccount Created!')
account.print_details()

another = 'y'
while another.lower() == 'y':
    choice = input('\nEnter 1 to deposit or 2 to withdraw: ')
    if choice == '1':
        amount = float(input('Enter the amount you want to deposit: '))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input('Enter the amount you want to withdraw: '))
        account.withdraw(amount)
    else:
        print('Invalid choice.')
    another = input("Do you want to do another transaction? ('y' for yes): ")

print('Your final balance is', account.current_balance)
