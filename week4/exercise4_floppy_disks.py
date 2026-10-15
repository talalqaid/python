# Exercise 4: Assume decimal units: 1 TB = 10^12 bytes, 1 MB = 10^6 bytes.
import math
capacity_tb = 1e12
capacity_floppy = 1.44e6
floppy_thickness_m = 3.2e-3
number_of_floppies = math.ceil(capacity_tb / capacity_floppy)
height_m = number_of_floppies * floppy_thickness_m
print('Scientific notation examples:')
print(format(1244.23, 'e'))
print(format(1244.23, '.2e'))
print(f'Floppy disks needed: {number_of_floppies:,}')
print(f'Stack height: {height_m:,.3f} metres ({height_m / 1000:.3f} km)')
