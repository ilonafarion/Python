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
