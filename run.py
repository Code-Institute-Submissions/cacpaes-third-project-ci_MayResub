""" Tic Tac Toe
"""


def printboard(board):
    """ Print the dashboar using the board parameter
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerinput(input_board, player):
    """ input to enter a number
    """
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and input_board[inp-1] == "-":
        input_board[inp-1] = player
    else:
        print("Erro!")


def check_row(index, board):
    """ Check row
    """
    if board[index] == board[index + 1] and \
            board[index + 1] == board[index + 2] and board[index] != "-":
        return board[index]

    return None


def check_col(index, board):
    """
    """
    if board[index] == board[index + 3] and \
            board[index + 3] == board[index + 6] and board[index] != "-":
        return board[index]

    return None


def check_rows(input_board):
    """ check for win or tie
    """
    for index in range(0, 7, 3):
        result = check_row(index, input_board)
        if result:
            return result
    return None


def check_cols(board):
    """check for win or tie
    """
    for index in range(0, 3):
        result = check_col(index, board)
        if result:
            return result
    return None


def check_diagonal(board):
    """check for win or tie
    """
    if board[0] == board[4] and board[4] == board[8] and board[0] != "-":
        return board[0]
    elif board[2] == board[4] and board[4] == board[6] and board[4] != "-":
        return board[2]
    return None


def check_if_win(board):
    """check who won
    """
    winner = check_rows(board)
    if winner:
        printboard(board)
        print(f"The winner is {winner}!")
        return False
    
    winner = check_cols(board)
    if winner:
        printboard(board)
        print(f"The winner is {winner}!")
        return False

    winner = check_diagonal(board)
    if winner:
        printboard(board)
        print(f"The winner is {winner}!")
        return False

    return True


def check_if_tie(input_board):
    """check for tie
    """
    if "-" not in input_board:
        printboard(input_board)
        print("It is a tie!")
        return False
    return True


def switchplayer(player):
    """ Switch player based on the currentplayer parameter
    """
    return "O" if player == "X" else "X"


def main():
    """Instruction to the game
    """
    board = ['     ' for i in range(9)]
    print('Welcome to Tic Tac Toe!')
    print('____________Instruction____________')
    print('* Player needs to choose a position between 1 - 9.')
    print('* Player will play against a friend.')
    print('* If no one wins and the board run out of space would be tie!')
    play = input("Do you want to play? (yes/no) ")
    if play.lower() == "yes":
        print("Let's play!")
    elif play.lower() == "no":
        print('See you next time!')
        quit()
    else:
        print('Please choose yes/no to start or quit the game')

    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]

    currentplayer = "X"
    gamerunning = True

    while gamerunning:
        printboard(board)
        playerinput(board, currentplayer)
        gamerunning = check_if_win(board)
        if not gamerunning:
            break
        currentplayer = switchplayer(currentplayer)
        gamerunning = check_if_win(board)
        if not gamerunning:
            break
        gamerunning = check_if_tie(board)


main()
