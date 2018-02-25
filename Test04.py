# This is a guess the number game.

import random

print ('Hello. What is your name?')
name = input()

print ('Well, ' + name + ', I am thinking of a number between 1-20.')
secretNum = random.randint (1,20)

for guessNum in range (1,7):
    print ('Take a guess:')
    guess = int(input())

    if guess < secretNum:
        print ('Your guess is too low.')

    elif guess > secretNum:
        print ('Your guess is too high.')

    else: 
        break # guessed correctly

if guess == secretNum:
    print ('Good job, ' + name + '! ' 'You got it it right in ' + str(guessNum)+ ' guesses!')

else:
    print ('Nope. The number I was thinking of is ' + str(secretNum) +'.')
