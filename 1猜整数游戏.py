import sys
import random


def transform(s):
    try:
        s = int(s)
        if s < 1 or s > 100:
            s = input('Please enter a number from 1 to 100!\n')
            return transform(s)
        else:
            return s
    except ValueError:
        s = input('Please enter a number!\n')
        return transform(s)


def play():
    a = random.randint(1, 100)
    x = input(
        'It\'s your turn!\nGuess an integer from 1 to 100(You have 10 chances):'
    )
    x = transform(x)  # add type check
    i = 1
    while (i < 10):
        if x < a:
            x = input('The integer you guessed is small!\nLet' 's try again:')
            x = transform(x)
            i += 1
            continue
        elif x > a:
            x = input('The integer you guessed is big!\nLet' 's try again:')
            x = transform(x)
            i += 1
            continue
        elif x == a:
            print('You are right!The integer is %d.' % a)
            return
    print('No more chance!')
    return


play()
while (1):
    c = input('Wanna play again?\n')
    if c == 'y' or c == 'Y':
        play()
    '''else:
        sys.exit(0)'''
