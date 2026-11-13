# Task 2 (optional) - Read morse_message.txt and decode it.
from pathlib import Path
from Task_2_Morse_Code import MORSE

reverse_codes = {code: letter for letter, code in MORSE.items()}
print(reverse_codes)
source = Path(__file__).with_name('morse_message.txt')
encoded = source.read_text(encoding='utf-8')
words = []
for word in encoded.split(' / '):
    decoded = ''
    for code in word.split():
        decoded += reverse_codes.get(code, '')
    words.append(decoded)
print('Decoded message:', ' '.join(words))
