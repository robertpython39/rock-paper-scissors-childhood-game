#-------------------------------------------------------------------------------
# Name:        Rock / Paper / Scissors game
# Purpose:     Fun
#
# Author:      nicolescu
#
# Created:     4/11/2021
# Copyright:   (c) nicol 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
logo = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)     '''

print(logo)




print("Welcome to ROCK, PAPER, SCISSORS game!")
print("Select 1 = Rock, 2 = Paper, 3 = Scissors")
select = int(input("Select: "))
rand_number = random.randint(1, 3)
print(f"Computer chose {rand_number}")
if select == 1 & rand_number == 1:
    print("Equal. Try again!")
elif select == 1 & rand_number == 2:
    print("Paper beats Rock! Computer win!")
elif select == 1 & rand_number == 3:
    print("Rock beats Scissors! You win!")
elif select == 2 & rand_number == 2:
    print("Equal. Try again!")
elif select == 2 & rand_number == 1:
    print("Paper beats Rock! You win!")
elif select == 2 & rand_number == 3:
    print("Scissors beats Paper! Computer win!")
elif select == 3 & rand_number == 3:
    print("Equal. Try again!")
elif select == 3 & rand_number == 2:
    print("Scissors beats Paper! You win!")
elif select == 3 & rand_number == 1:
    print("Rock beats Scissors! Computer win!")
else:
    print("Invalid number. You lose!")
