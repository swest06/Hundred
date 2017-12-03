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


def computer_move(computer_score, human_score):
    turn = True
    while turn:
        a = roll()
        if a == 1:
            computer_score = 0
            turn = False
        else:
            computer_score = computer_score + a

            if computer_score => human_score:
                roll_again == random.randint(1, 2)

                if roll_again = 1:
                    continue
                else:
                    break
                
                
        
    
   ''' while computer_score < human_score:
        a = roll()
        if a == 1:
            computer_score = 0
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
                total = total + a'''
            
    return total


def human_move(computer_score, human_score):
    turn = True
    while turn:
        
        if ask_yes_or_no() == False:
            turn == False
            break
        else:
            a = roll()

            if a == 1:
                human_score = 0
                turn = False
            else:
                print("You rolled a " + a)
                human_score = human_score + a
                print("Your score is now " + human_score)
                continue

    if human_score > computer_score:
        print("You are winning by " + human_score - computer_score + " points")
    elif computer_score > human_score:
        print("You are losing by " + computer_score - human_score + " points")
    else:
        print("You are tied with the computer")

    return human_score


def ask_yes_or_no():
    response = False
    while response == False:
        a = input("Do you want to roll again? Y/N: ").lower()
        if a[0] == "y":
            response = True
            return True
        elif a[0] == "n":
            response = True
            return False
        else:
            continue

    
roll = roll()
