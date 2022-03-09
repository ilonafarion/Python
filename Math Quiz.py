#multiplication quiz
import pyinputplus, random, time
print('Welcome to the Multiplication Quiz. You will be asked to solve 10 multiplication problems. You have 5 seconds for each and only one chance to give the right answer. Good luck!')
while True:
    questions = 10
    correctanswers = 0

    for question in range(questions):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

        task = '#%s: %s x %s = ?' % (question+1, num1, num2)
        try:
            pyinputplus.inputStr(task, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes = [('.*', 'Incorrect')],timeout = 5, limit =1)
        except pyinputplus.TimeoutException:
            print('sorry, you exceeded the time given for answer. You score 0 points. for this question.')
        except pyinputplus.RetryLimitException:
            continue
        else:
            print('Correct')
            correctanswers +=1
        time.sleep(1)
    print('score: %s/ %s ' % (correctanswers, questions))
    anothergame = pyinputplus.inputChoice(['yes', 'no'], 'do you want to play again?')
    if anothergame == 'yes':
        continue
    elif anothergame == 'no':
        print('thank you for the game')
        break
