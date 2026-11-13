# Task 2 (optional) - Encode text and save it to morse_message.txt.
# Use / to separate words so they can be recovered when decoding.
from pathlib import Path
from Task_2_Morse_Code import MORSE

message = input('Enter a message: ').upper()
words = []
for word in message.split():
    letters = [MORSE[ch] for ch in word if ch in MORSE]
    if letters:
        words.append(' '.join(letters))

encoded = ' / '.join(words)
output = Path(__file__).with_name('morse_message.txt')
output.write_text(encoded, encoding='utf-8')
print('Saved Morse code to:', output.name)
print(encoded)
