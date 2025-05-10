################################################################################
#       __ ____  ____  ____ ____ __  __ _____ ____ ___  ______ ___ ___ 144     #
#      / / __  / ___// __  /___// / / /__  __/ __/ ___/__  __/ __/ __ \        #
#   __/ / /_/ / /__ / /_/ / __//  \/ /  / / / __/\ \    / / / __/ /_/_/        #
#  / / /  ___/ /_/ /  ___/ /_ / /\  /  / / / /_ __\ \  / / / /_/ /\ \          #
#  \__/__/   \____/__/  /___//_/ \_/  /_/ /___//____/ /_/ /___/_/  \_\         #
#      slotmachine.py                                   version 1.0            #
#                                                                              #
# VERSION                                                                      #
# 1.0                                                                          #
#                                                                              #
# CHANGELOG                                                                    #
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
##########################################

######### VARIABLE DECLARATION ############
day_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
winning_prize = 0
counter = 0
###########################################

############# MAIN SCRIPT #################

clear_screen()
print("\nCurrent Day: " + day_of_week[counter])
print("\n")

user_choice = input("\nWould you like to play Slot Machine game(yes/no)? ")

while user_choice.lower() == "yes":
    clear_screen()
    print("###############################################")
    print("############## SLOT MACHINE GAME ##############")
    print("###############################################")
    print("###############################################")
    print("############## 0 ## 0 ## 0 ## 0 ###############")
    print("###############################################")
    print("###############################################")

    print("\nCurrent Day: " + day_of_week[counter])

    user_play = input("\nHit enter to play: ")

    while user_play == "":
        a = str(random.randint(0, 2))
        b = str(random.randint(0, 2))
        c = str(random.randint(0, 2))
        d = str(random.randint(0, 2))

        clear_screen()
        print("###############################################")
        print("############## SLOT MACHINE GAME ##############")
        print("###############################################")
        print("###############################################")
        print("############## " + a + " ## " + b + " ## " + c + " ## " + d + " ###############")
        print("###############################################")
        print("###############################################")

        print("\nCurrent Day: " + day_of_week[counter] + "    " + "Winning Prize: $" + str(winning_prize) + ".00")

        if a == b and b == c and c == d:
            print("\nCONGRATULATIONS IT'S A MATCH!!!")
            print("\nYou won: $" + str(winning_prize) + ".00!")
            print("\n")
            pause_screen()
        else:
            print("\nYou did not win. Try again.")
            winning_prize = winning_prize + 1

        user_play = input("\nHit enter to play again: ")
    

    
    pause_screen()


    user_choice = input("\nContinue playing (yes/no)? ")
############### END OF MAIN SCRIPT #################


############# RANDOM TEST THIS IS MESSY ##################

    print("")


user_input = input("\nSkip next day? ")
while user_input == "":
    
    print("###############################################")
    print("###############################################")
    print("###############################################")
    print("############# SLOT MACHINE GAME ###############")
    print("###############################################")
    print("###############################################")
    print("###############################################")
    print("###############################################")
    print("\nCurrent Day: " + day_of_week[counter])
    print("\n")
    user_input = input("\nSkip next day? ")

    if counter <= 5:
        counter += 1
    else:
        counter = 0


time.sleep(40)







user_input = input("\nPull lever (enter to continue)? ")

random1 = random.randint(1, 60)
random2 = random.randint(1, 60)
random3 = random.randint(1, 60)
random4 = random.randint(1, 60)
random5 = random.randint(1, 60)
random6 = random.randint(1, 60)
random7 = random.randint(1, 60)
random8 = random.randint(1, 60)
random9 = random.randint(1, 60)

while user_input == "":
    clear_screen()
    # Get the current time in seconds since the epoch
    clock_time = time.localtime()
    seconds = time.strftime("%S", clock_time)
    print("Seconds since epoch =", seconds)
    count = int(seconds)
    if count >= 11 and count <= 20:
        print("\nSLOT MACHINE GAME\n")
        print(str(random.randint(1, 3)) + " " + str(random.randint(1, 3)) + " " + str(random.randint(1, 3)))
        
       
        print("\n")
        print("\n")
        print("\n")
        user_input = input("Pull lever (enter to continue)? ")
    elif count >= 21 and count <= 30:
        print("\nSLOT MACHINE GAME\n")
        print(str(random.randint(5, 6)) + " " + str(random.randint(4, 5)) + " " + str(random.randint(5, 10)))
        
       
        print("\n")
        print("\n")
        print("\n")
        user_input = input("Pull lever (enter to continue)? ")

    elif count >= 31 and count <= 40:
        print("\nSLOT MACHINE GAME\n")
        print(str(random.randint(1, 4)) + " " + str(random.randint(1, 4)) + " " + str(random.randint(1, 4)))
        
       
        print("\n")
        print("\n")
        print("\n")
        user_input = input("Pull lever (enter to continue)? ")

    elif count >= 41 and count <= 50:
        print("\nSLOT MACHINE GAME\n")
        print(str(random.randint(3, 6)) + " " + str(random.randint(3, 6)) + " " + str(random.randint(3, 6)))
        
       
        print("\n")
        print("\n")
        print("\n")
        user_input = input("Pull lever (enter to continue)? ")

    else:
        print("\nSLOT MACHINE GAME\n")
        print(str(random.randint(1, 10)) + " " + str(random.randint(1, 10)) + " " + str(random.randint(1, 10)))
        
       
        print("\n")
        print("\n")
        print("\n")
        user_input = input("Pull lever (enter to continue)? ")










