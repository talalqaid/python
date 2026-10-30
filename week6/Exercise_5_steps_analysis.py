# Exercise 5: Average steps per month, assuming a non-leap year.

def main():
    steps_file = open('step.txt', 'r')
    steps = [int(line.strip()) for line in steps_file if line.strip() != '']
    steps_file.close()

    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

    if len(steps) != 365:
        print('Warning: expected 365 records but found', len(steps))
        return

    start = 0
    monthly_averages = []
    for index in range(12):
        end = start + days_per_month[index]
        average = sum(steps[start:end]) / days_per_month[index]
        monthly_averages.append(average)
        print(months[index] + ': ' + format(average, '.2f') + ' steps/day')
        start = end

    # Compare first six months with last six months to judge the trend.
    first_half = sum(monthly_averages[:6]) / 6
    second_half = sum(monthly_averages[6:]) / 6
    print('Average of monthly averages (Jan-Jun):', format(first_half, '.2f'))
    print('Average of monthly averages (Jul-Dec):', format(second_half, '.2f'))
    if second_half > first_half:
        print('Overall, daily steps tend to increase during the year.')
    elif second_half < first_half:
        print('Overall, daily steps tend to decrease during the year.')
    else:
        print('The two halves have the same average.')
main()
