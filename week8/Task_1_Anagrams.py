# Task 1 - Check whether two words are anagrams using dictionaries.

def tally_letters(word):
    counts = {}
    for letter in word.lower():
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

first = input("Enter the first word: ").strip()
second = input("Enter the second word: ").strip()
first_counts = tally_letters(first)
second_counts = tally_letters(second)
print("First word letter counts:", first_counts)
print("Second word letter counts:", second_counts)
if first_counts == second_counts:
    print("These words are anagrams.")
else:
    print("These words are NOT anagrams.")
