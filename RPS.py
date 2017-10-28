"""This program is a game between the user and the computer. You will be asked to choose rock, paper or scissors. The computer will randomly choose between rock, paper and scissors.Winner takes all."""

from random import randint

from time import sleep

option = ["R", "P", "S"]

LOSS_MESSAGE = "You lost!"
WON_MESSAGE = "You win!" 

def decide_winner(user_choice, computer_choice): 
  print "You selected: %s" % user_choice
  print "Computer selecting..."
  sleep(1)
  print " Computer selected: %s" % computer_choice
  user_choice_index = option.index(user_choice)
  computer_choice_index = option.index(computer_choice)
  if user_choice_index == computer_choice_index:
    print "It's a tie!"
  elif user_choice_index == 0 and computer_choice_index == 2:
    print WON_MESSAGE
  elif user_choice_index == 2 and computer_choice_index == 1:
    print WON_MESSAGE
  elif user_choice_index == 1 and computer_choice_index == 0:
    print WON_MESSAGE
  elif user_choice_index > 2:
    print "Invalid entry"
    return
  else:
    print LOSS_MESSAGE
            
def play_RPS():
  print "Rock, Paper or Scissors?"
  user_choice = raw_input("Select R for Rock, P for Paper or S for Scissors: ")
  user_choice = user_choice.upper()
  sleep(1)
  computer_choice = option[randint(0, len(option) - 1)]
  decide_winner(user_choice, computer_choice)

play_RPS()                                     