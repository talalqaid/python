
# Exercise 6 - Fixed Bank Loan Program

min_salary = 30000.0
min_months = 24

salary = float(input("Enter your annual salary: "))

months_employed = int(input("Enter the number of months employed: "))

if salary >= min_salary or months_employed >= min_months:
    print("You qualify for the loan.")
else:
    print("You do not qualify for this loan.")
