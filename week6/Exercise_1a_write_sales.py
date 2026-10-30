# Exercise 1(a): Modified version of write_sales.py.
# Save children's, ladies', men's and total sales for each day.

def main():
    num_days = int(input('For how many days do you have sales? '))
    sales_file = open('sales.txt', 'w')

    for count in range(1, num_days + 1):
        print('Day', count)
        children = float(input("Enter children's sales: £"))
        ladies = float(input('Enter ladies sales: £'))
        gentlemen = float(input("Enter gentlemen's sales: £"))
        total = children + ladies + gentlemen

        # Each day is stored as four lines, always in the same order.
        sales_file.write(str(children) + '\n')
        sales_file.write(str(ladies) + '\n')
        sales_file.write(str(gentlemen) + '\n')
        sales_file.write(str(total) + '\n')

    sales_file.close()
    print('Data written to sales.txt.')
main()
