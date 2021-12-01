import random
while True: # i  wanted to make this a game and ask questions in loop, not necessry step here 
    def getanswer(number_of_answer):
        if number_of_answer == 1:
            return "yes"
        elif number_of_answer == 2:
            return "no"
        elif number_of_answer == 3:
            return "i guess we will never know"
    print("what is ur question?")
    ur_question = input()
    zakres = [1,2,3]
    print(getanswer(random.choice(zakres)))

# augmented version :
import random

messages = ['yes', 'no', 'i gues we will never know']
while True:
    print('what is ur question? (enter nothing to stop)')
    question = input()
    if question == "":
        print('nice talking to you, see u!')
        break
    print(random.choice(messages))
