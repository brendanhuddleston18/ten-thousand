from ten_thousand.game_logic import GameLogic

roll = 1
user_round = 1
banked_score = 0
unbanked_points = 0
dice_chosen = []
split_list = []
dice_remaining = 6
user_answer = ''
rolled_dice = ''

def welcome():
  """
  """

  print("""Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
  user_start = input("> ")
  if user_start.lower() == 'n':
    print("OK. Maybe another time")
  elif user_start.lower() == 'y':
    game()
  else:
    print("Bro follow the rules")
    welcome()

def keep_bank_quit_function():
  """
  """

  global roll
  global user_answer
  global dice_chosen
  global banked_score
  global unbanked_points
  global dice_remaining
  global user_round

  if roll == 1:
    print("Enter dice to keep, or (q)uit:")
    user_answer = input("> ")
    if user_answer.lower() == "q":
      print("OK. Maybe another time")
    else:
      roll += 1
      dice_chosen.extend([int(dice) for dice in user_answer])
      subtract_dice_remaining()
      calculate_score()
      game()
  else: 
    print("(r)oll again, (b)ank your points or (q)uit:")
    user_answer = input("> ")
    if user_answer.lower() == "q":
      print(f"Thanks for playing. You earned {banked_score} points")
    elif user_answer.lower() == "b":
      banked_score += unbanked_points
      unbanked_points = 0
      dice_chosen.clear()
      dice_remaining = 6
      user_round += 1
      game()
    elif user_answer.lower() == "r":
      unbanked_points = 0
      dice_chosen = []
      dice_remaining = 6
      game()
    else:
      roll += 1
      dice_chosen = [int(dice) for dice in user_answer]
      calculate_score()
      dice_remaining = 6 - len(dice_chosen)
      game()

def game():
  """
  """
  global roll
  global dice_remaining
  global unbanked_points
  global rolled_dice
  global banked_score

  rolled_dice = GameLogic.roll_dice(dice_remaining)
  if unbanked_points:
    print(f"you have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
  if banked_score:
    print(f"Total Score is {banked_score}")
  print(f"Starting round {user_round}")
  print(f"Rolling {dice_remaining} dice")
  print(f"*** {rolled_dice} ***")
  keep_bank_quit_function()


def calculate_score():
 """
 """
 global unbanked_points
#  global dice_chosen
 global rolled_dice
 global split_list
 global dice_remaining
#  int_dice_chosen = []
#  split_list = [char for num in dice_chosen for char in num]
#  for num in split_list:
#    int_dice_chosen.append(int(num))
 roll_score = GameLogic.calculate_score(dice_chosen)
 unbanked_points += roll_score

def subtract_dice_remaining():
  """
  """
  global dice_remaining
  print(split_list)
  dice_remaining = 6 - len(split_list)


welcome()