
board = [" " for _ in range(9)]  # 3x3 empty board

def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_win(player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],      # Rows
        [0,3,6], [1,4,7], [2,5,8],      # Columns
        [0,4,8], [2,4,6]                # Diagonals
    ]
    
    for combo in win_combinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

current_player = "X"

while True:
    display_board()
    print("Player", current_player, "turn.")
    
    move = int(input("Choose a position (1-9): ")) - 1
    
    if board[move] == " ":
        board[move] = current_player
    else:
        print("Spot already taken! Try again.")
        continue

    if check_win(current_player):
        display_board()
        print("Player", current_player, "wins! 🎉")
        break

    if check_draw():
        display_board()
        print("It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
