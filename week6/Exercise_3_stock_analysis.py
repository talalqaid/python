# Exercise 3: Count stock records, find maximum, minimum and average.

def main():
    stock_file = open('stock.txt', 'r')
    values = []
    for line in stock_file:
        if line.strip() != '':
            values.append(float(line))
    stock_file.close()

    if len(values) == 0:
        print('No stock data found.')
    else:
        print('Number of daily records:', len(values))
        print('Maximum stock value: £' + format(max(values), '.2f'))
        print('Minimum stock value: £' + format(min(values), '.2f'))
        print('Average stock value: £' + format(sum(values) / len(values), '.2f'))
main()
