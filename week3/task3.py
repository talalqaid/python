
# Exercise 3 - Coursework Grade Calculator

mark1 = float(input("Enter coursework 1 mark: "))
mark2 = float(input("Enter coursework 2 mark: "))
mark3 = float(input("Enter coursework 3 mark: "))

average = (mark1 + mark2 + mark3) / 3

print(f"Overall mark: {average:.2f}")

if average >= 90:
    print("Your grade is A.")
elif average >= 80:
    print("Your grade is B.")
elif average >= 70:
    print("Your grade is C.")
elif average >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")
