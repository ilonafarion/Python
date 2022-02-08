# checks if the input is a phone numebr (basic program without regex)
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return      False
    for i in range (4,7):
        if not text[i].isdecimal():
            return  False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True
print('please input phone in format \d\d\d-\d\d\d-\d\d\d\d')
text = input()
if isPhoneNumber(text) == True:
    print( text + ' is a phone number')
else:
    print(text + ' is not a phone number')
    
# version 2:  searches for a phone number in a longer text:
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return      False
    for i in range (4,7):
        if not text[i].isdecimal():
            return  False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

text = 'Please feel free to call me at 123-123-1235. Take care!'
for i in range(len(text)):
    isnumber = text[i:i+12]
    if isPhoneNumber(isnumber):
        print('phone number found: ' + isnumber)
        
# ver3 using regex:
import re

PNregex =  re.compile(r'\d{3}-\d{3}-\d{4}')

text = input('please input text')
match = PNregex.search(text)
if match == None:
    print('no phone number found')
else:
    print( 'phone number found ' + match.group())
