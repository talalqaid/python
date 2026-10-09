
# Exercise 1 - Average Test Scores

high_score = 70
low_score = 40

test1 = float(input("Enter score for test 1: "))
test2 = float(input("Enter score for test 2: "))
test3 = float(input("Enter score for test 3: "))
test4 = float(input("Enter score for test 4: "))

average = (test1 + test2 + test3 + test4) / 4

print(f"The average score is {average:.1f}")

if average > high_score:
    print("Congratulations! Great average!")
elif average < low_score:
    print("Warning! You need to improve your performance.")
else:
    print("You have achieved a satisfactory average.")
