from getpass import getpass as input
print("Rock, Paper, Scissors!")
print("Select your move (R = Rock,\tP = Paper,\t S = Scissors.")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")
if player1 == player2:
  print("Draw!")
elif player1 == "R":
  if player2 == "P":
    print("Paper covers rock! Player 2 wins.")
  else:
    print("Rock smashes Scissors! Player 1 wins.")
    
elif player1 == "P":
  if player2 == "S":
    print("Scissors cuts paper! Player 2 wins.")
  else:
    print("Rock covers paper! Player 1 wins.")
    
elif player1 == "S":
  if player2 == "R":
    print("Rock smashes scissors! Player 2 wins.")
  else:
    print("Scissors cut paper! Player 1 wins.")
