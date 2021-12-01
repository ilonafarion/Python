import random, sys
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
print( 'Wins: ' + str(wins), 'Losses: ' + str(losses), 'Ties: ' + str(ties))
mylist = ['R','P','S']
while True:
    print('enter ur move: R rock P paper S scissors or Q quit')
    move = input()
    while True:
        if move == 'Q':
            print('why dont u wanna play with me:(')
            sys.exit()
        elif move == 'R':
            print('Rock versus...')
            break
        elif move == 'P':
            print('Paper versus...')
            break
        elif move == 'S':
            print('Scissors versus...')
            break


    computers_move = random.choice(mylist)
    if computers_move == 'R':
        print('Rock')
    if computers_move == 'S':
        print('Scissors')
    if computers_move == 'P':
        print('Paper')


    if move == computers_move:
        print('its a tie!')
        ties = ties +1
    elif move == 'R' and computers_move == 'P':
        print('computer wins!')
        losses = losses + 1
    elif move == 'P' and computers_move == 'R':
        print('you win!')
        wins = wins + 1
    elif move == 'S' and computers_move == 'R':
        print('computer wins!')
        losses = losses + 1
    elif move == 'R' and computers_move == 'S':
        print('you win!')
        wins = wins + 1
    elif move == 'S' and computers_move == 'P':
        print('you win!')
        wins = wins + 1
    elif move == 'P' and computers_move == 'S':
        print('computer wins!')
        losses = losses + 1

    print( 'Wins: ' + str(wins) , 'Losses: ' + str(losses), 'Ties: ' + str(ties))


