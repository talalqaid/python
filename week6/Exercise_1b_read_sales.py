# Exercise 1(b): Modified version of read_sales2.py.
# Print a report for every day stored by Exercise 1(a).

def main():
    sales_file = open('sales.txt', 'r')
    day = 1

    # Four lines make one day's record.
    children_line = sales_file.readline()
    while children_line != '':
        children = float(children_line)
        ladies = float(sales_file.readline())
        gentlemen = float(sales_file.readline())
        total = float(sales_file.readline())

        print('Day', day)
        print("Children's sales: £" + format(children, '.2f'))
        print('Ladies sales: £' + format(ladies, '.2f'))
        print("Gentlemen's sales: £" + format(gentlemen, '.2f'))
        print('Total sales: £' + format(total, '.2f'))
        print()
        day += 1
        children_line = sales_file.readline()

    sales_file.close()
main()
