from time import time
from random import sample, choice

def enter_guess():
    guess = [0]*4
    for i in range(4):
        while(True):
            guess[i] = int(input("Guess {}, Enter number 1-8: ".format(i+1)))
            if guess[i] in range(1,9):
                break
            else:
                print("Guess out of range. Try again:")
            
    return guess

def check_answer(guess,answer):
    red = 0
    white = 0
    tmp_answer = answer.copy()
    tmp_guess = guess.copy()
    for i in range(len(guess)):
        if tmp_guess[i] == tmp_answer[i]:
            red += 1
            tmp_answer[i] = 'r'
            tmp_guess[i] = 'rg'
    for i in range(len(guess)):
        if guess[i] in tmp_answer:
            white += 1
            tmp_answer[tmp_answer.index(guess[i])] = 'w'

    return red, white

start = time()
answer = sample(range(1,9),4) # sample from 1 through 8, four times without replacement
    
round = 1
while(True):
    guess = enter_guess()
    print("Round: {}, guess: {}, time elapsed: {:.1f} s".format(round,guess,time()-start))
    red, white = check_answer(guess,answer)
    print("Red: {}, White: {}\n".format(red,white))
    if (red == 4):
        print("Correct!")
        break
    round += 1
