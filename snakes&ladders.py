# Francis Oludhe
# Snakes & Ladders

import random
import time
import sys

pick = ["Y","y","N","n"]

""""Starting position"""
pos, pospos = 0, 0

"""" This will act as the dice roll. Emulating chance """
roll = [1,2,3,4,5,6]

dice = (random.choice(roll))

# Title Card - Version
print "Welcome to Snakes & Ladders 1.0\n"
print "  /--------------------------------------------\ "
print "<                                              : >--<"
print "  \--------------------------------------------/ \n"

print " "
print " "

# Actual gameplay code
def game(pos, dice, pospos):
    rolling = raw_input("Dare to roll? ")

    while rolling not in pick:
        print "-------------------------------------------------------------\n"
        print "\nPlease answer with Y/N\n"
        rolling = raw_input("Roll again? ")
        print "-------------------------------------------------------------\n"

    if (rolling == "n" or rolling == "N"):
        print "\nThank you for visiting.\n"
        time.sleep(3)
        sys.exit()

    elif (rolling == "Y" or rolling == "y"):
        dice = (random.choice(roll))
        time.sleep(2)
        print "\nYou rolled a", dice, "\n"
        time.sleep(1)

        if (pospos < 50):
            pos = pospos + dice
            print "You are at tile", pos, "\n"
            print "-------------------------------------------------------------\n"

            if (pos == 2):
                pos = 21
                time.sleep(1)
                print "Luckily, you come across a ladder. You move forward to tile", pos, ".\n"
                print "-------------------------------------------------------------\n"

            elif (pos == 14):
                pos = 27
                time.sleep(1)
                print "Luckily, you come across a ladder. You move forward to tile", pos, ".\n"
                print "-------------------------------------------------------------\n"

            elif (pos == 38):
                pos = 45
                time.sleep(1)
                print "Luckily, you come across a ladder. You move forward to tile", pos, ".\n"
                print "-------------------------------------------------------------\n"

            elif (pos == 49):
                pos = 25
                time.sleep(1)
                print "Oops! You stand face to face with a snake.\n"
                print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                print "You move back to tile", pos, ".\n"
                print "-------------------------------------------------------------\n"

            elif (pos == 23):
                pos = 6
                time.sleep(1)
                print "Oops! You stand face to face with a snake.\n"
                print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                print "You move back to tile", pos, ".\n"
                print "-------------------------------------------------------------\n"

            elif (pos == 39):
                pos = 17
                time.sleep(1)
                print "Oops! You stand face to face with a snake.\n"
                print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                print "You move back to tile", pos, ".\n"
                print "-------------------------------------------------------------\n"

            elif (pos > 50):
                pos = 50-((pospos+dice)-50)
                time.sleep(1)
                print "Because you passed tile 50, you go back to tile", pos, "\n"
                print "-------------------------------------------------------------\n"

                if (pos == 2):
                    pos = 21
                    time.sleep(1)
                    print "Luckily, you come across a ladder. You move forward to tile", pos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pos == 14):
                    pos = 27
                    time.sleep(1)
                    print "Luckily, you come across a ladder. You move forward to tile", pos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pos == 38):
                    pos = 45
                    time.sleep(1)
                    print "Luckily, you come across a ladder. You move forward to tile", pos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pos == 49):
                    pos = 25
                    time.sleep(1)
                    print "Oops! You stand face to face with a snake.\n"
                    print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                    print "You move back to tile", pos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pos == 23):
                    pos = 6
                    time.sleep(1)
                    print "Oops! You stand face to face with a snake.\n"
                    print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                    print "You move back to tile", pos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pos == 39):
                    pos = 17
                    time.sleep(1)
                    print "Oops! You stand face to face with a snake.\n"
                    print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                    print "You move back to tile", pos, ".\n"
                    print "-------------------------------------------------------------\n"

            elif (pos == 50):
                print ("YOU WIN. Thank you for playing.")
                print "-------------------------------------------------------------\n"
                time.sleep(5)
                sys.exit()

        rolling = raw_input("Dare to roll? ")

        while rolling not in pick:
            print "-------------------------------------------------------------\n"
            print "\nPlease answer with Y/N\n"
            rolling = raw_input("Roll again? ")
            print "-------------------------------------------------------------\n"

        if (rolling == "n" or rolling == "N"):
            print "\nThank you for visiting.\n"
            time.sleep(3)
            sys.exit()

        elif (rolling == "Y" or rolling == "y"):
            dice = (random.choice(roll))
            time.sleep(2)
            print "\nYou rolled a", dice, "\n"
            time.sleep(1)

            if (pos < 50):
                pospos = pos + dice
                print "You are at tile", pospos, "\n"
                print "-------------------------------------------------------------\n"

                if (pospos == 2):
                    pospos = 21
                    time.sleep(1)
                    print "Luckily, you come across a ladder. You move forward to tile", pospos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pospos == 14):
                    pospos = 27
                    time.sleep(1)
                    print "Luckily, you come across a ladder. You move forward to tile", pospos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pospos == 38):
                    pospos = 45
                    time.sleep(1)
                    print "Luckily, you come across a ladder. You move forward to tile", pospos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pospos == 49):
                    pospos = 25
                    time.sleep(1)
                    print "Oops! You stand face to face with a snake.\n"
                    print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                    print "You move back to tile", pospos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pospos == 23):
                    pospos = 6
                    time.sleep(1)
                    print "Oops! You stand face to face with a snake.\n"
                    print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                    print "You move back to tile", pospos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pospos == 39):
                    pospos = 17
                    time.sleep(1)
                    print "Oops! You stand face to face with a snake.\n"
                    print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                    print "You move back to tile", pospos, ".\n"
                    print "-------------------------------------------------------------\n"

                elif (pospos > 50):
                    pospos = 50-((pos+dice)-50)
                    time.sleep(1)
                    print "Because you passed tile 50, you go back to tile", pospos, "\n"
                    print "-------------------------------------------------------------\n"

                    if (pospos == 2):
                        pospos = 21
                        time.sleep(1)
                        print "Luckily, you come across a ladder. You move forward to tile", pospos, ".\n"
                        print "-------------------------------------------------------------\n"

                    elif (pospos == 14):
                        pospos = 27
                        time.sleep(1)
                        print "Luckily, you come across a ladder. You move forward to tile", pospos, ".\n"
                        print "-------------------------------------------------------------\n"

                    elif (pospos == 38):
                        pospos = 45
                        time.sleep(1)
                        print "Luckily, you come across a ladder. You move forward to tile", pospos, ".\n"
                        print "-------------------------------------------------------------\n"

                    elif (pospos == 49):
                        pospos = 25
                        time.sleep(1)
                        print "Oops! You stand face to face with a snake.\n"
                        print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                        print "You move back to tile", pospos, ".\n"
                        print "-------------------------------------------------------------\n"

                    elif (pospos == 23):
                        pospos = 6
                        time.sleep(1)
                        print "Oops! You stand face to face with a snake.\n"
                        print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                        print "You move back to tile", pospos, ".\n"
                        print "-------------------------------------------------------------\n"

                    elif (pospos == 39):
                        pospos = 17
                        time.sleep(1)
                        print "Oops! You stand face to face with a snake.\n"
                        print "Paralysed with fear, you can't help but fall victim to its jaws.\n"
                        print "You move back to tile", pospos, ".\n"
                        print "-------------------------------------------------------------\n"

                elif (pospos == 50):
                    print ("YOU WIN. Thank you for playing.")
                    print "-------------------------------------------------------------\n"
                    time.sleep(5)
                    sys.exit()

# The repeat portion of this definition
    while ((pospos < 50), (pospos > 50)):
        game(pos, dice, pospos)

# Process Start
game(pos, dice, pospos)
