board = [" "," "," "," "," "," "," "," "," "," "]

def draw_board(board):
    print(board[7] + " |" + board[8] + " |" + board[9])
    print("--+--+--")
    print(board[4] + " |" + board[5] + " |" + board[6])
    print("--+--+--")
    print(board[1] + " |" + board[2] + " |" + board[3])
  
#use variables to store user names
player1 = input("Enter 1st Player mame: ")
player2 = input("Enter 2nd Player name: ")

print(player1 + ": X |" + player2 + ": O")

#Logic Validate User input
def game():
  turn = "X"
  count = 0
  player_turn = player1
  game_over = False

  while game_over == False:
    draw_board(board)
    print("It's your turn, " + player_turn + ". Move to which place?")
    
    try:
      move = eval(input())
      if move >= 10 or move <= 0:
        print("Please choose a correct spot\nMove to which place?")
        continue
      elif board[move] == " ":
        board[move] = turn
        count += 1
      else:
        print("That place is already filled.\nMove to which place?")
        continue
    except:
      print("Cannot use letters.\nMove to which place?")
      continue

    if count >= 5:
      if board[7] == board[8] == board[9] != " ":
        declare_winner(turn)
        break
      elif board[4] == board[5] == board[6] != " ":
        declare_winner(turn)
        break
      elif board[1] == board[2] == board[3] != " ":
        declare_winner(turn)
        break
      elif board[1] == board[4] == board[7] != " ":
        declare_winner(turn)
        break
      elif board[2] == board[5] == board[8] != " ":
        declare_winner(turn)
        break
      elif board[3] == board[6] == board[9] != " ":
        declare_winner(turn)
        break
      elif board[7] == board[5] == board[3] != " ":
        declare_winner(turn)
        break
      elif board[1] == board[5] == board[9] != " ":
        declare_winner(turn)
        break

    if count == 9:
      print("\nGame Over.\n")
      print("It's a Tie!!")
      game_restart()
      break

    if turn == "X":
      turn = "O"
      player_turn = player2
    else:
      turn = "X"
      player_turn = player1
#Declare winner
def declare_winner(turn):
  draw_board(board)
  print("\nGame Over.\n")
  
  if turn == "X":
    print(" **** " + player1 + " won ****")
  else:
    print(" **** " + player2 + " won ****")

  game_restart()
#GameOver. Play again
def game_restart():
  restart = input("\nDo you want to play again?(y/n): ").lower()
  if restart == "y":
    for element in board:
      board[board.index(element)] = " "
    game()

game()