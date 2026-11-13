# Task 4 - Read a file and display its unique words.
from pathlib import Path

file_path = Path(__file__).with_name('sample_words.txt')
unique_words = set()
with file_path.open('r', encoding='utf-8') as file:
    for line in file:
        for word in line.split():
            unique_words.add(word.strip('.,!?;:"\'()').lower())

unique_words.discard('')
print('Unique words:')
for word in sorted(unique_words):
    print(word)
print('Total unique words:', len(unique_words))
