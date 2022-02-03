# bullet point adder program with help of the book 'Automate the Boring Stuff with Python'

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
