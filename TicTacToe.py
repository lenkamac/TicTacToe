board = [' ' for b in range(9)]

game_go = True
winner = None
current_player = "x"


def play_game():
    # display initial board
    display_board()

    while game_go:
        global current_player

        print(line)

        move = input(f"Player {current_player}| Please enter your move number (1-9): ")
        move_n = int(move)
        if (move_n >= 1) and (move_n <= 9):
            position = int(move_n) - 1
            if space_free(position):
                board[position] = current_player
                display_board()
            else:
                print("Sorry, this space is occupied!")
                continue
        else:
            print('Please number between 1 - 9')
            continue

        check_game_over()

        if current_player == "x":
            current_player = "o"
        else:
            current_player = "x"

    if winner == "x" or winner == "o":
        print(f"{winner} WON!")
    else:
        print("Game is tie!")


def display_board():
    print("+---+---+---+")
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("+---+---+---+")
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("+---+---+---+")
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("+---+---+---+")


def check_game_over():
    check_win()
    check_tie()


def check_win():
    global winner

    win_row = check_rows()
    win_column = check_columns()
    win_dig = check_diagonals()
    if win_row:
        winner = win_row
    elif win_column:
        winner = win_column
    elif win_dig:
        winner = win_dig
    else:
        winner = None


def check_rows():

    global game_go

    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    if row_1 or row_2 or row_3:
        game_go = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():

    global game_go

    column_1 = board[0] == board[3] == board[6] != " "
    column_2 = board[1] == board[4] == board[7] != " "
    column_3 = board[2] == board[5] == board[8] != " "
    if column_1 or column_2 or column_3:
        game_go = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagonals():

    global game_go

    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[6] == board[4] == board[2] != " "
    if diagonal_1 or diagonal_2:
        game_go = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_tie():
    global game_go
    if " " not in board:
        game_go = False
        return True
    else:
        return False


def space_free(position):
    return board[position] == ' '


line = "=" * 50
print("{0: ^50}".format("Welcome to Tic Tac Toe"))
print(line)
print("""{0: ^50} \nEach player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a: """.format("Game Rules"))
print("* {0:<15}\n* {1:<15}\n* {2:<15}".format('horizontal', 'vertical or', 'diagonal row'))
print(line)
print("{0:^50}".format("Let's start the game"))
print('-' * 50)

play_game()
