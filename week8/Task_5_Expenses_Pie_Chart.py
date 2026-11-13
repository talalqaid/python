# Task 5 
from pathlib import Path
import matplotlib.pyplot as plt

categories = {}
total_expense = 0
with Path(__file__).with_name('expenses.txt').open('r', encoding='utf-8') as file:
    for line in file:
        parts = line.split()
        if len(parts) == 2:
            category, cost = parts[0], float(parts[1])
            categories[category] = cost
            total_expense += cost

category_names = list(categories.keys())
expenses = list(categories.values())
print(category_names)
if not expenses or total_expense <= 0:
    raise ValueError('expenses.txt must contain positive expense values.')
plt.figure(figsize=(8, 8))
plt.pie(expenses, labels=category_names, autopct='%1.1f%%', startangle=90)
plt.title('Monthly Expenses')
plt.tight_layout()
output = Path(__file__).with_name('Task_5_Expenses_Pie_Chart.png')
plt.savefig(output)
print('Total expenses:', total_expense)
print('Chart saved to:', output.name)
plt.show()
