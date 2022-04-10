# print the game board
def printboard(board):
    """ Print the dashboar using the board parameter
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerinput(input_board, player):
    """
    """
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and input_board[inp-1] == "-":
        input_board[inp-1] = player
    else:
        print("Erro!")


def checkhorizontle(input_board):
    """ check for win or tie
    """
    if input_board[0] == input_board[1] == input_board[2] and \
            input_board[0] != "-":
        return input_board[0]
    elif input_board[3] == input_board[4] == input_board[5] and \
            input_board[3] != "-":
        return input_board[3]
    elif input_board[6] == input_board[7] == input_board[8] and \
            input_board[6] != "-":
        return input_board[6]
    return None


def checkrow(board):
    if board[0] == board[3] == board[6] and board[0] != "-":
        return board[0]
    elif board[1] == board[4] == board[7] and board[1] != "-":
        return board[1]
    elif board[2] == board[5] == board[8] and board[2] != "-":
        return board[3]
    return None


def checkdiag(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        return board[0]
    elif board[2] == board[4] == board[6] and board[4] != "-":
        return board[2]
    return None


def check_if_win(board):
    """
    """
    if winner := checkhorizontle(board):
        printboard(board)
        print(f"The winner is {winner}!")
        return False
    elif winner := checkrow(board):
        printboard(board)
        print(f"The winner is {winner}!")
        return False
    elif winner := checkdiag(board):
        printboard(board)
        print(f"The winner is {winner}!")
        return False
    return True


def check_if_tie(input_board):
    """
    """
    if "-" not in input_board:
        printboard(input_board)
        print("It is a tie!")
        return False
    return True


def checkwin(input_board):
    """
    """
    winner = checkdiag(input_board)
    if winner := checkdiag(input_board):
        print(f"The Winner is {winner}")
    elif winner := checkhorizontle(input_board):
        print(f"The Winner is {winner}")
    elif winner := checkrow(input_board):
        print(f"The Winner is {winner}")


# swith the player
def switchplayer(player):
    """ Switch player based on the currentplayer parameter
    """
    return "O" if player == "X" else "X"

# check for win or tie again


def main():
    """
    """
    board = ['     ' for i in range(9)]
    print('Welcome to Tic Tac Toe!')
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
