
# Exercise 11 - Chinese Zodiac

year = int(input("Enter a year: "))

animals = [
    "Dragon", "Snake", "Horse", "Sheep",
    "Monkey", "Rooster", "Dog", "Pig",
    "Rat", "Ox", "Tiger", "Hare"
]

if year <= 0:
    print("Please enter a year greater than zero.")
else:
    index = (year - 2000) % 12
    print(f"The animal for {year} is {animals[index]}.")
