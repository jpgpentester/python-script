################################################################################
#       __ ____  ____  ____ ____ __  __ _____ ____ ___  ______ ___ ___ 144     #
#      / / __  / ___// __  /___// / / /__  __/ __/ ___/__  __/ __/ __ \        #
#   __/ / /_/ / /__ / /_/ / __//  \/ /  / / / __/\ \    / / / __/ /_/_/        #
#  / / /  ___/ /_/ /  ___/ /_ / /\  /  / / / /_ __\ \  / / / /_/ /\ \          #
#  \__/__/   \____/__/  /___//_/ \_/  /_/ /___//____/ /_/ /___/_/  \_\         #
#      slotmachine.py                                   version 1.2            #
#                                                                              #
# VERSION                                                                      #
# 1.2                                                                          #
#                                                                              #
# CHANGELOG                                                                    #
# - Added feature how casino owner can make user not win                       #
# - Added banner for game.                                                     #
# - Added start day of the week but will make it actual current date           #
# - Added winning prize that increases every play                              #
#                                                                              #
# FILES                                                                        #
# slotmachine.py                                                               #
#                                                                              #
# DATE CREATED        LAST DATE MODIFIED                                       #
# 09MAY2025           09MAY2025                                                #
#                                                                              #
# DESCRIPTION                                                                  #
# This is slot machine version but will show how game can be manipulated       #
# to either make some win or make someone lose all the time.                   #
#                                                                              #
# AUTHOR              EMAIL                                                    #
# Jose Paulo Garcia   <jpgpentester.github>@<gmail>.<com>                      #
#                                                                              #
################################################################################

import time
import random
import os


############## FUNCTIONS #################
def pause_screen():
    time.sleep(60)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def cheat_game():
    num = random.randint(1, 8)
    match num:
        case 1:
            a = str(random.randint(1, 2))
            b = str(random.randint(1, 2))
            c = str(random.randint(1, 2))
            d = str(random.randint(1, 2))
        case 2:
            a = str(random.randint(2, 3))
            b = str(random.randint(2, 3))
            c = str(random.randint(2, 3))
            d = str(random.randint(2, 3))
        case 3:
            a = str(random.randint(3, 4))
            b = str(random.randint(3, 4))
            c = str(random.randint(3, 4))
            d = str(random.randint(3, 4))
        case 4:
            a = str(random.randint(4, 5))
            b = str(random.randint(4, 5))
            c = str(random.randint(4, 5))
            d = str(random.randint(4, 5))
        case 5:
            a = str(random.randint(5, 6))
            b = str(random.randint(5, 6))
            c = str(random.randint(5, 6))
            d = str(random.randint(5, 6))
        case 6:
            a = str(random.randint(6, 7))
            b = str(random.randint(6, 7))
            c = str(random.randint(6, 7))
            d = str(random.randint(6, 7))
        case 7:
            a = str(random.randint(7, 8))
            b = str(random.randint(7, 8))
            c = str(random.randint(7, 8))
            d = str(random.randint(7, 8))
        case 8:
            a = str(random.randint(8, 9))
            b = str(random.randint(8, 9))
            c = str(random.randint(8, 9))
            d = str(random.randint(8, 9))
    return(a, b, c, d)
##########################################

######### VARIABLE DECLARATION ############
day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
winning_prize = 0
user_cash = 0
casino_bank = 0
counter = 0
cheat_mode = True
casino_min_bank = 100 # The amount of money casino wants in their bank before people start winning.
###########################################

############# MAIN SCRIPT #################

clear_screen()

user_choice = input("\nWould you like to play Slot Machine game(yes/no)? ")
while user_choice != "yes" or user_choice != "no":
    if user_choice.lower() == "yes":
        user_cash = int(input("How much cash you want to gamble? (min: $2 max: $1000)? "))

        while user_cash < 2 or user_cash > 1000:
            clear_screen()
            print("ATTN: Minimum is: $2       Maximum is: $1000")
            user_cash = int(input("How much cash you want to gamble? (min: $2 max: $1000)? "))
        break

    elif user_choice.lower() == "no":
        clear_screen()
        print("\nGood Bye!")
        time.sleep(10)
    else:
        clear_screen()
        print("\nInvalid user input. Try again.")
        user_choice = input("\nWould you like to play Slot Machine game(yes/no)? ")

while user_choice.lower() == "yes" and user_cash >= 2:
    clear_screen()
    
    print("###############################################")
    print("############## SLOT MACHINE GAME ##############")
    print("###############################################")
    print("###############################################")
    print("############## 0 ## 0 ## 0 ## 0 ###############")
    print("###############################################")
    print("###############################################")

    print("\nCurrent Day: " + day_of_week[counter] + "    Cash: $" + str(user_cash) + ".00    Winning Prize: $" + str(winning_prize) + ".00    Casino Bank: $" + str(casino_bank) + ".00")

    user_play = input("\nHit enter to play: ")
    winning_prize = winning_prize + 1
    casino_bank = casino_bank + 1
    user_cash = user_cash - 2

    while user_play == "" and user_cash >= 2:

        a = str(random.randint(0, 2)) # Decrease 9 to 2 to increase probability to match
        b = str(random.randint(0, 2))
        c = str(random.randint(0, 2))
        d = str(random.randint(0, 2))

        if a == b and b == c and c == d:
            print("\n")
            print("#### ATTENTION!")
            print("#### Next results: " + a + " " + b + " " + c + " " + d)
            if cheat_mode == True and casino_bank < casino_min_bank:
                a = str(random.randint(0, 9))
                b = str(random.randint(0, 9))
                c = str(random.randint(0, 9))
                d = str(random.randint(0, 9))
                
                print("#### Message: Oh no it's a match. Player is going to win!!")
                print("#### Casino Bank: $" + str(casino_bank) + ".00")
                print("#### Casino Bank Minimum Amount Set: $" + str(casino_min_bank) + ".00")
                print("#### Minimum casino bank amount is not met. Hacking slot game machine...")
                time.sleep(10)
                print("#### Manipulating next results...")
                time.sleep(7)
                print("#### Next result successfully modified: " + a + " " + b + " " + c + " " + d)
                time.sleep(2)
                print("#### Continuing...")
                time.sleep(10)

        clear_screen()
        print("###############################################")
        print("############## SLOT MACHINE GAME ##############")
        print("###############################################")
        print("###############################################")
        print("############## " + a + " ## " + b + " ## " + c + " ## " + d + " ###############")
        print("###############################################")
        print("###############################################")

        print("\nCurrent Day: " + day_of_week[counter] + "    Cash: $" + str(user_cash) + ".00    Winning Prize: $" + str(winning_prize) + ".00    Casino Bank: $" + str(casino_bank) + ".00")
        
        if a == b and b == c and c == d:
            # print(str(a + b + c + d))
            print("\nCONGRATULATIONS IT'S A MATCH!!!")
            print("\nYou won: $" + str(winning_prize) + ".00!")
            user_cash = user_cash + winning_prize
            winning_prize = 0
            user_choice = input("\nWould you like to continue to play (yes/no)? ")
        else:
            print("\nYou did not win. Try again.")
            winning_prize = winning_prize + 1
            casino_bank = casino_bank + 1
            user_cash = user_cash - 2

        user_play = input("\nHit enter to play again: ")

    clear_screen()
    print("\nCurrent Day: " + day_of_week[counter] + "    Cash: $" + str(user_cash) + ".00    Winning Prize: $" + str(winning_prize) + ".00    Casino Bank: $" + str(casino_bank) + ".00")
    print("\nSorry. You need cash to play!")
    user_choice = input("\nWould you like to play (yes/no)? ")
    user_cash = int(input("How much cash you want to gamble? (min: $2 max: $1000)? "))


pause_screen()
    
############### END OF MAIN SCRIPT #################


############ WORK IN PROGRESS ##############
# clock_time = time.localtime()
# seconds = time.strftime("%S", clock_time)
# print("Seconds =", seconds)