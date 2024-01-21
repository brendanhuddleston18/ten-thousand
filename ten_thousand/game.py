from ten_thousand.game_logic import GameLogic

dice_remaining = 6
unbanked_score = 0
banked_score = 0
round_num = 1
roll = 0
hot_dice_index = 0
dice_chosen = []
current_roll = []
string_rolled_dice = ''

def play(roller=None):
  welcome(roller)

def welcome(roller=None):
  """
  Welcomes user to Ten Thousand game

  Parameters
  - None

  Returns
  - None
  """

  print("""Welcome to Ten Thousand
(y)es to play or (n)o to decline""")
  user_start = input("> ")
  if user_start.lower() == 'n':
    print("OK. Maybe another time")
  elif user_start.lower() == 'y':
    play_round(roller)
  else:
    print("Bro follow the rules")
    welcome()


def play_round(roller=None):
  """
  Starts a round of the Ten Thousand game

  Parameters
  - Round Number that the user is on

  Returns
  - None
  """
  if banked_score:
    print(f"Total score is {banked_score} points")

  print(f"Starting round {round_num}")
  roll_dice(roller)


def roll_dice(roller=None):
  """
  Rolls the dice using the game logic method "roll_dice"

  parameters
  - None

  Returns
  - None
  """
  global dice_remaining
  global roll
  global current_roll
  global string_rolled_dice

  if roller:
    mock_roll = roller()
    # print(f"mock roll: {mock_roll}")
    mock_roll_str = ''
    for num in mock_roll:
      mock_roll_str += str(num) + " "
    print(f"Rolling 6 dice...")
    print(f"*** {mock_roll_str} ***")
    zilch_checker(mock_roll)
  else:
    tuple_rolled_dice = GameLogic.roll_dice(dice_remaining)
    current_roll = tuple_rolled_dice
    string_rolled_dice = ' '.join(str(dice) for dice in tuple_rolled_dice)
    print(f"Rolling {dice_remaining} dice...")
    print(f"*** {string_rolled_dice} ***")
    zilch_dice = GameLogic.calculate_score(tuple_rolled_dice)
    zilch_checker(zilch_dice)
  roll += 1
  user_answer(user_inputted_value=True)
  


def user_answer(user_inputted_value=False):
  """
  Handles all user inputs and directs them to the corresponding function

  Parameters
  - None

  Returns
  - None
  """

  if user_inputted_value == True:
    print("Enter dice to keep, or (q)uit:")
  else:
    print("(r)oll again, (b)ank your points or (q)uit:")

  user_input = input("> ")

  if user_input == "r":
    roll_dice()
  elif user_input == "b":
    bank_score()
  elif user_input == "q":
    handle_quit()
  else:
    handle_keep(user_input)

def handle_keep(user_input):
  """
  Handles the dice that the user selects, adds them to dice_chosen list and calls calculate_score()

  Parameters
  - user_input if they decide to keep a dice

  Returns
  - None
  """
  global dice_remaining
  dice_chosen.extend([int(dice) for dice in user_input])

  if check_user_cheating(current_roll, dice_chosen):
    dice_remaining -= len(dice_chosen)
    calculate_score()
    # dice_chosen.clear()r   
  else:
    print("Cheater!!! Or possibly made a typo...")
    print(f"*** {string_rolled_dice} ***")
    dice_chosen.clear()
    user_answer()

def calculate_score():
  """
  Calculates score, Get's called automatically from handle_keep when user selects di

  Parameters
  - None

  Returns 
  - None
  """
  global unbanked_score
  global hot_dice_index
  global roll
  score = GameLogic.calculate_score(dice_chosen)
  if score:
    hot_dice_index += len(dice_chosen)
  unbanked_score += score
  print(f"You have {unbanked_score} unbanked points and {dice_remaining} dice remaining")
  roll += 1
  hot_dice_checker()
  dice_chosen.clear()
  user_answer()


def bank_score():
  """
  Banks user score if they decide to in user_answer

  Parameters
  - None

  Returns 
  - None
  """
  global banked_score
  global unbanked_score
  global round_num
  global dice_remaining
  global roll
  print(f"you banked {unbanked_score} in round {round_num}")
  banked_score += unbanked_score
  round_num +=1
  dice_remaining = 6
  unbanked_score = 0
  roll = 0
  dice_chosen.clear()
  play_round()

def zilch_checker(roll_score):
  """
  
  """
  global round_num
  global dice_remaining
  global roll
  global unbanked_score
  if roll_score == 0:
    print("""****************************************
**        Zilch!!! Round over         **
****************************************""")
    round_num += 1
    dice_remaining = 6
    roll = 0
    unbanked_score = 0
    dice_chosen.clear()
    play_round()

def hot_dice_checker():
  """
  Will Check if the all of the user's dice score

  Parameters 
  - None

  Return 
  - None
  """
  global dice_remaining
  global hot_dice_index
  if hot_dice_index >= 6:
    hot_dice_index = 0
    dice_chosen.clear()
    # dice_remaining = 6
    # roll_dice()

def check_user_cheating(dice_list, dice_chosen):
    dice_list_count = {num: dice_list.count(num) for num in set(dice_list)}
    dice_chosen_count = {num: dice_chosen.count(num) for num in set(dice_chosen)}

    for num in dice_chosen_count:
        if dice_chosen_count[num] > dice_list_count.get(num, 0):
            return False
    return True

def check_dice_score():
  pass
      
    

def handle_quit():
  """
  Will quit the game if user types 'q' in user_answer function

  Parameters
  - None

  returns 
  - None
  """
  print(f"Thanks for playing. You earned {banked_score} points")

if __name__ == "__main__":

  rolls = [(5, 2, 3, 5, 4, 2), (2, 3, 1, 3, 1, 2), (4, 1, 4, 4, 3, 4), (3, 2, 3, 2, 1, 4), (1, 2, 5, 1, 2, 1)]

  def mock_roller():
    return rolls.pop(1)


  # play(mock_roller)
  play()