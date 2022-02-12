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
        
# ver3 using regex and multiple assignment for groups:
import re,sys
PNregex =  re.compile(r'(\d{3})-(\d{3}-\d{3})')
text = input('please input text')

match = PNregex.search(text)
try:
    area,number = match.groups()
except:
    print ('no phone number found')
    sys.exit()
    
if match is None:
     print('no phone number found')
else:
    print( 'phone number area code found ' + area)

    
 # ver4 using regex with a few possible phone number formats
import re
import sys

try:
    while True:
        PNregex =  re.compile(r'(\(| )*?(\d{3})(\)| )*?(-| )*?(\(| )*?(\d{3}(\)| )*?(-| )*?(\(| )*?\d(\(| )*?)')
        print('input ur text')
        text = input()
        match = PNregex.search(text)
        if match is None:
            print( 'no phone number found')
            print('do you want to continue?')
            answer = input()
            if answer == 'yes':
               continue
            elif answer == 'no':
                break
            else:
                print('please input yes/no')
                continue
        else:
            print('phone number is: ' + match.group())
except KeyboardInterrupt:
    sys.exit()
   
