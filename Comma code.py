### with .JOIN method

owoce = ['apples', 'bananas','orange', 'kiwis', 'raspberrys', 'liczi','tangerine']

def CommaCode():
    print(str(', '.join(owoce[0:-1])) + ' and ' + str(owoce[-1]), end=" ")


CommaCode()

print('\n***************')

### without .JOIN method
def CommaCode_2(lista):
    for skladnik in range(len(lista[0:-2])):
        print(lista[skladnik], end=', ')
    print(lista[-2] + ' and ' + lista[-1])

CommaCode_2(owoce)
