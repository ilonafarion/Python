import random
secretnumber = random.randint(1,20)
print('i am thinking of a number from 1 to 20. guess the number')
for guesses in range(1,3):
    print('take a guess')
    guess = int(input())
    if guess ==secretnumber:
        print('congrats, you guessed right!')
    elif guess > secretnumber:
        print('guess too high')
    elif guess < secretnumber:
        print('guess too low')
else:
    print('sorry, you exceeded the limit of guesses, i was thinking of ' + str(secretnumber))
# is it okay if I use else with for function?? in the internet is says it is okay to use for/while with else so i guess yeah
# below version from the book:
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
