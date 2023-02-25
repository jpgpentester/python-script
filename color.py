################################################################################
#       __ ____  ____  ____ ____ __  __ _____ ____ ___  ______ ___ ___ 144     #
#      / / __  / ___// __  /___// / / /__  __/ __/ ___/__  __/ __/ __ \        #
#   __/ / /_/ / /__ / /_/ / __//  \/ /  / / / __/\ \    / / / __/ /_/_/        #
#  / / /  ___/ /_/ /  ___/ /_ / /\  /  / / / /_ __\ \  / / / /_/ /\ \          #
#  \__/__/   \____/__/  /___//_/ \_/  /_/ /___//____/ /_/ /___/_/  \_\         #
#      color.py                                   v.1.0                        #
#                                                                              #
# VERSION                                                                      #
# v.1.0                                                                        #
#                                                                              #
# CHANGELOG                                                                    #
# - Make the code more readable and consistent                                 #
#                                                                              #
# FILES                                                                        #
# color.py                                                                     #
#                                                                              #
# DATE CREATED        LAST DATE MODIFIED                                       #
# 21 Feb 2023         25 Feb 2023                                              #
#                                                                              #
# DESCRIPTION                                                                  #
# Simple script for adding font styles, foreground colors and background       #
# colors.                                                                      #
#                                                                              #
# AUTHOR              EMAIL                                                    #
# Jose Paulo Garcia   <jpgpentester.github>(@)<gmail>.<com>                    #
#                                                                              #
# TITLE                                                                        #
# Cybersecurity Professional / Junior Penetration Tester / Junior Developer    #
#                                                                              #
################################################################################

# VARIABLE DECLARATION
# RESET FONT STYLE #
RESET = "\033[0;0m"

## FONT STYLES ##
BOLD = "\033[1;5;245m"
ITALIC = "\033[3;5;245m"
UNDERLINE = "\033[4;5;245m"
DOUBLE_UNDERLINE = "\033[21;5;245m"
STRIKEOUT = "\033[9;5;245m"

## FOREGROUND LIGHT COLORS ##
FG_LIGHT_GRAY = "\033[30;5;245m"
FG_LIGHT_RED = "\033[31;5;245m"
FG_LIGHT_GREEN = "\033[32;5;245m"
FG_LIGHT_YELLOW = "\033[33;5;245m"
FG_LIGHT_BLUE = "\033[34;5;245m"
FG_LIGHT_PURPLE = "\033[35;5;245m"
FG_LIGHT_NAVYBLUE = "\033[36;5;245m"
FG_WHITE = "\033[37;5;245m"

## FOREGROUND BRIGHT COLORS ##
FG_BRIGHT_GRAY = "\033[90;5;245m"
FG_BRIGHT_RED = "\033[91;5;245m"
FG_BRIGHT_GREEN = "\033[92;5;245m"
FG_BRIGHT_YELLOW = "\033[93;5;245m"
FG_BRIGHT_BLUE = "\033[94;5;245m"
FG_BRIGHT_PURPLE = "\033[95;5;245m"
FG_BRIGHT_NAVYBLUE = "\033[96;5;245m"
FG_WHITE = "\033[97;5;245m"
FG_BRIGHT_GRAY = "\033[90;5;245m"

## BACKGROUND COLORS NORMAL ##
BG_BLACK = "\033[40;5;245m"
BG_RED = "\033[41;5;245m"
BG_GREEN = "\033[42;5;245m"
BG_YELLOW = "\033[43;5;245m"
BG_BLUE = "\033[44;5;245m"
BG_PURPLE = "\033[45;5;245m"
BG_NAVYBLUE = "\033[46;5;245m"
BG_WHITE = "\033[47;5;245m"
BG_GRAY = "\033[48;5;245m"

## BACKGROUND LIGHT COLORS ##
BG_LIGHT_GRAY = "\033[100;5;245m"
BG_LIGHT_RED = "\033[101;5;245m"
BG_LIGHT_GREEN = "\033[102;5;245m"
BG_LIGHT_YELLOW = "\033[103;5;245m"
BG_LIGHT_BLUE = "\033[104;5;245m"
BG_LIGHT_PURPLE = "\033[105;5;245m"
BG_LIGHT_NAVYBLUE = "\033[106;5;245m"
BG_WHITE = "\033[107;5;245m"
# END OF VARIABLE DECLARATION #

# MAIN SCRIPT (UNCOMMENT IF NEEDED) #
# Display sample message with all different font styles and colors.
#sample_message = "Hello World"

#for color in range(1, 107):
#   print("Font Style " + str(color) + ": " + "\033[" + str(color) + ";5;245m" + sample_message + "\033[0;0m")

#print("")

# Example of different font styles
#print(ITALIC + STRIKEOUT + BOLD + UNDERLINE + BG_PURPLE + FG_WHITE+ sample_message + RESET)
# END OF MAIN SCRIPT #
