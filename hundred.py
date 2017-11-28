'''Sean West swest06.
    Text based Hundred game.'''
import random

def instructions():
    print("Roll the die as many times as you want to accumulate your score.")
    print("Each number you roll gets added to your score. However if you roll a '1' your score resets to '0'.")
    print("If this happens your turn ends and your opponent (the computer) gets to roll")
    print("etc...")


def roll():
    return random.randint(1, 6)    


def computer_move(computer_score, human_score, roll):
    total = 0
    while computer_score < human_score:
        a = roll()
        if a == 1:
            total = 0
            a = 0
            break
        else:
            total = total + a

    else:
        n = random.randint(0, 10)
        while n > 0:
            a = roll()
            if a == 1:
                total = 0
                a = 0
                break
            else:
                total = total + a
            
    return total

roll = roll()
