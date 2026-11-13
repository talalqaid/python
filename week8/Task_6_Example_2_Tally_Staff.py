# Task 6
def tally_staff(staff):
    totals = {}
    for name in staff:
        totals[name] = totals.get(name, 0) + 1
    return totals

staff_list = ['Alex', 'Sam', 'Alex', 'Jordan', 'Sam', 'Alex']
print('Staff counts:', tally_staff(staff_list))
