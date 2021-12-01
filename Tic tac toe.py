import random
Theboard = {'TL':' ','TM':' ','TR':' ',
         'ML':' ','MM':' ','MR':' ',
         'LL':' ','LM':' ','LR':' ',}
def printBoard(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board ['ML'] + '|' + board ['MM'] + '|' + board ['MR'])
    print('-+-+-')
    print(board ['LL'] + '|' + board ['LM'] + '|' + board ['LR'])
turn = 'X'
computer_move = 'O'
for i in range(9):
    printBoard(Theboard)
    print('Turn for player ' + turn + '. Move on to which space?' )
    move = input()
    if move not in Theboard.keys ():
        print ('sorry , there is no such place on the board, please try again')
    if Theboard[move] != ' ':
        print('please choose different spot, there is already data here')
        continue
    Theboard[move] = turn # theboard['TL']= X
    print ('Turn for player ' + computer_move + '.')
    moveC = random.choice(list(Theboard.keys()))
    if Theboard [moveC] != ' ':
        moveC = random.choice(list(Theboard.keys()))
    Theboard [moveC] = computer_move
def winning(board):
    if board['TL']==board['TM']==board['TR']:
    elif board['ML']==board['MM']==board['MR']:
    elif board ['LL'] == board ['LM'] == board ['LR']:
    elif board['TL']==board['MM']==board['LR']:
    elif board['LL']==board['MM']==board['TR']:
    elif board ['LL'] == board ['LM'] == board ['TL']:
    elif board ['LM'] == board ['MM'] == board ['TM']:
    elif board ['LR'] == board ['MR'] == board ['TR']:

#to be continued

printBoard (Theboard)
