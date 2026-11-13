# Task 3
scrabble = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}

word = input('Enter a word: ').upper()
word_score = 0
for ch in word:
    for score, letters in scrabble.items():
        if ch in letters:
            word_score += score
print(word, 'scores', word_score, 'points')
