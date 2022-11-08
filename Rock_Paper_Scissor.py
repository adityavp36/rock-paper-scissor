import random

def get_choices():
  player_choice = input ("Please enter your choice (rock, paper, scissor):")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices 

def check_win(player, computer):
  print (f"you choose {player} and computer choses {computer}")
  if player == computer:
    return "it is a tie"
  elif player == "rock":
    if computer == "scissor":
      return "rock smashes scissors, You Win"
    else:
     return "Paper covers rock, you lose"
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock, You Win"
    else:
     return "Scissors cuts paper, you lose"
  elif player == "scissor":
    if computer == "paper":
      return "Scissors cuts paper, You Win"
    else:
     return "rock smashes scissors, you lose"

choices = get_choices()
result = check_win(choices["player"] , choices ["computer"])
print (result)