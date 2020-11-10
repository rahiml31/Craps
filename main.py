from random import randint
import time

# Rolls a pair of dice
def dice_roll():
  dice1 = randint(1, 6)
  dice2 = randint(1, 6)
  return sum((dice1, dice2))

# Runs play method whenever a point value has not been set
def no_point_play():
  print("Code for whenever a point has not been set. Figure out if you want to re-up bet if a winner.")

# Runs the result post roll once point has been set. Will return payout, if any.
def point_play(roll, point_val, line_bet, bar_bet, bankroll, bet_type, point_boo, point_dic):
  result = ""
  if bet_type == "line":
    if roll == point_val:
      print(f"Winner! Point value {str(point_val)} was hit! Pays 1|1.")
      bankroll += line_bet
      point_boo = False
      result = "w"
      #print(f"Bankroll:\t {str(bankroll)}")
    else: pass
    # Check if value of roll in dictionary is >0, if so winner and payout else pass
    if (roll in point_dic.keys() and point_dic[roll] > 0):
      if roll in (4, 10):
        print(f"Winner! Free odds point {str(roll)} was hit! Pays 2|1.")
        bankroll += (point_dic[roll]*(2/1))
        print(f"Bankroll:\t {str(bankroll)}")
        result = "w"
      elif roll in (5, 9):
        print(f"Winner! Free odds point {str(roll)} was hit! Pays 3|2.")
        bankroll += (point_dic[roll]*(3/2))
        print(f"Bankroll:\t {str(bankroll)}")
        result = "w"
      else: #(6, 8)
        print(f"Winner! Free odds point {str(roll)} was hit! Pays 5|6.")
        bankroll += (point_dic[roll]*(5/6))
        print(f"Bankroll:\t {str(bankroll)}")
        result = "w"
  else: #bar
    if roll in (7, 11):
      print(f"Winner! A 7 or 11 was rolled while the point value was set.")
      bankroll += bar_bet
      print(f"Bankroll:\t {str(bankroll)}")
      result = "w"
    elif roll == point_val:
      print(f"Loser. Point value {str(point_val)} was rolled.")
      point_boo = False
      result = "l"
    else: pass
    # Check if value of roll in dictionary is >0, if so winner and payout else pass
    if (roll in point_dic.keys() and point_dic[roll] > 0):
      if roll in (4, 10):
        print(f"Winner! Free odds point {str(roll)} was hit! Pays 1|2.")
        bankroll += (point_dic[roll]*(1/2))
        print(f"Bankroll:\t {str(bankroll)}")
        result = "w"
      elif roll in (5, 9):
        print(f"Winner! Free odds point {str(roll)} was hit! Pays 2|3.")
        bankroll += (point_dic[roll]*(2/3))
        print(f"Bankroll:\t {str(bankroll)}")
        result = "w"
      else: #(6, 8)
        print(f"Winner! Free odds point {str(roll)} was hit! Pays 5|6.")
        bankroll += (point_dic[roll]*(5/6))
        print(f"Bankroll:\t {str(bankroll)}")
        result = "w"
  return [bankroll, point_boo, line_bet, bar_bet, result]

def make_additional_bet(point_dic, bankroll):
  print("Code to add additional bets to other non-point values.")
  # put the additional bet values into a dictionary?
  # {4:0, 5:0, 6:0, 8:0, 9:0, 10:0}
  print(point_dic)
  while True:
    num = int(input("Which value would you like to make a bet on(4/5/6/8/9/10). Please enter 0 when finished: "))
    if num == 0: break
    print("Minimum bets: 6/8 - $12, 4/5/9/10 - $10")
    bet = int(input("How much do you want to bet on the value: " ))
    bankroll -= bet
    print(f"Bankroll:\t {str(bankroll)}")
    point_dic[num] = bet
  return [point_dic, bankroll]

def play_craps():
  
  # Setting main play variables
  starting_bankroll = 100
  bankroll = starting_bankroll
  ante = 1
  point_boo = False
  point_val = 0
  bet_type = ""
  pass_line_bet = 0
  dont_pass_bar_bet = 0
  field_bet = 0
  play_boo = True
  roll_num = 0

  # Odds that each dice roll combination will occur
  point_bets = { 4:0, 5:0, 6:0, 8:0, 9:0, 10:0 }

  while (play_boo == True):
    print(f"Bankroll:\t {bankroll}")

    # Checks to make sure that there is a positive bankroll to play with
    if bankroll <= 0:
      print("No bankroll to play with.")
      break

    # Place Pass line or Don't Pass Bar bet
    stmt = str(input("Do you want to place a bet on the Pass line(line) or the Don't Pass Bar(bar): "))
    print(f"Max bet allowed: {bankroll}")
    if (stmt.lower() == "line"):
      bet_type = "line"
      pass_line_bet = int(input("Please enter how much you are betting on the Pass Line: "))
      bankroll -= pass_line_bet
    elif (stmt.lower() == "bar"):
      bet_type = "bar"
      dont_pass_bar_bet = int(input("Please enter how much you are betting on the Don't Pass Bar: "))
      bankroll -= dont_pass_bar_bet
    else:
      print("You have not entered a valid response. Ending game session.")
      sys.exit(1)
      print(f"Bankroll:\t {bankroll}")
    
    # Plays session whenever the Point has not been set
    while (point_boo == False):
      # Place a Field bet for a single roll
      field_stmt = str(input("Do you want to make a single Field bet(2/3/4/9/10/11/12)(y/n): "))
      if field_stmt == "y":
        field_bet = int(input("Please enter how much you are betting on the Field: "))
        bankroll -= field_bet

      roll = dice_roll()
      print(roll)

      if roll in (3, 4, 9, 10, 11):
        print("Winner! A 3, 4, 9, 10, 11 was rolled. Pays 1|1.")
        bankroll += field_bet
        print(f"New bankroll: {bankroll}")
      if roll in (2, 12):
        print("Winner! A 2, 12 was rolled. Pays 2|1.")
        bankroll += field_bet
        print(f"New bankroll: {bankroll}")

      if roll in (4, 5, 6, 8, 9, 10):
        print(f"Point is set. The point is {roll}")
        point_val = roll
        point_boo = True
      elif roll in (7, 11):
        if bet_type == "line":
          print("Winner! A 7 or 11 was rolled while the Pass Line is being played. Pays 1|1.")
          bankroll += pass_line_bet
          print(f"New bankroll: {bankroll}")
        else:
          print("Loser. A 7 or 11 was rolled while the Don't Pass Bar is being played.")
          bankroll -= pass_line_bet
          print(f"New bankroll: {bankroll}")
      elif roll in (2, 3):
        if bet_type == "line":
          print("Loser. A 2, 3 or 12 was rolled while the Pass Line is being played.")
          bankroll -= pass_line_bet
          print(f"New bankroll: {bankroll}")
        else:
          print("Winner! A 2 or 3 was rolled while the Don't Pass Bar is being played. Pays 1|1.")
          bankroll += dont_pass_bar_bet
          print(f"New bankroll: {bankroll}")
      else: #12
        if bet_type == "bar":
          print("Push. A 12 was rolled while the Don't Pass Bar is being played.")
        else:
          print("Loser. A 2, 3 or 12 was rolled while a line bet was placed.")
          bankroll -= pass_line_bet
          print(f"New bankroll: {bankroll}")
      time.sleep(1)

    # Plays session whenever the Point has been set
    while (point_boo == True):
      # Makes additional Point bets, if wanted
      add_bet = str(input("Do you want to make additional bets(y/n): "))
      if (add_bet.lower() == "y"):
        point_bets, bankroll = make_additional_bet(point_bets, bankroll)
        print(point_bets)
      # Makes a field bet for a single roll, if wanted
      field_stmt = str(input("Do you want to make a single Field bet(2/3/4/9/10/11/12)(y/n): "))
      if field_stmt == "y":
        field_bet = int(input("Please enter how much you are betting on the Field: "))
        bankroll -= field_bet

      roll = dice_roll()
      print(roll)

      if roll in (3, 4, 9, 10, 11):
        print("Winner! A 3, 4, 9, 10, 11 was rolled. Pays 1|1.")
        bankroll += field_bet
        print(f"New bankroll: {bankroll}")
      if roll in (2, 12):
        print("Winner! A 2, 12 was rolled. Pays 2|1.")
        bankroll += field_bet
        print(f"New bankroll: {bankroll}")

      if roll != 7:
        bankroll, point_boo, pass_line_bet, dont_pass_bar_bet, outcome = point_play(roll, point_val, pass_line_bet, dont_pass_bar_bet, bankroll, bet_type, point_boo, point_bets)
        if outcome == "l": 
          pass_line_bet = 0
          dont_pass_bar_bet = 0
      elif roll == 7 and bet_type == "bar":
        bankroll, point_boo, pass_line_bet, dont_pass_bar_bet, outcome = point_play(roll, point_val, pass_line_bet, dont_pass_bar_bet, bankroll, bet_type, point_boo, point_bets)
        if outcome == "l": 
          pass_line_bet = 0
          dont_pass_bar_bet = 0
      else: #(roll == 7):
        print("You rolled a 7. Craps.")
        point_boo = False
        response = str(input("Do you want to continue playing(y/n): "))
        if (response.lower() == "n"):
          print("Ending Craps session.")
          print(f"Bankroll:\t {str(bankroll)}")
          print(f"Plus/Minus bankroll during session: {str(bankroll - starting_bankroll)}")
          play_boo = False
        break


if __name__ == "__main__":
  # Will execute if run as a script
  play_craps()