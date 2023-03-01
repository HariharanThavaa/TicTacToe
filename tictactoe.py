# Initialize 2 dimensional array
board = [["","",""],["","",""],["","",""]]

#  Main method
def main():
    player = 'O'
    while not isGameOver():
        # Swap the turns
        if player == 'O' :
            player = 'X'
        else :
            player = 'O'
        play(player)
    print(f"Congratulation {player}, You won the game :)")

def isGameOver():
    # Check Horizontal Axis
    for row in board:
        if row[0] == row [1] == row [2] != '':
            return True
    #  Check vertical Axis
    for i in range(0,2):
        if board[0][i] == board [1][i] == board[2][i] != '':
            return True
    #  Check across
    if board[0][0] == board [1][1] == board[2][2] != '':
        return True
    if board[2][0] == board [1][1] == board[0][2] != '':
        return True

def play(player):
    print(f"{player} is playing :")
    x = -1
    y = -1
    while not mark(x, y, player):
        x = getInput("What's x?")
        y = getInput("What's y?")


def mark(x, y, player):
    if board[y][x] == '' and x != -1 and y != -1:
        board[y][x] = player
        printBoard()
        return True
    else:
        print(f'This box is already taken by {board[y][x]}')
        return False

def getInput(message):
    while True:
        try:
            x = int(input(message))
            if x < 0 or x > 2 :
                print("input can be in 0, 1, 2")
                continue
        except ValueError:
            print("Please provide a number")
        else:
            break
    return x

def printBoard():
    for row in board:
        print(row)

if __name__ == '__main__':
    main()