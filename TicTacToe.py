import pprint, random


# Arguments: board dict
# prints board as game goes
def printBoard(board):
    print((str(board['top-L'])) + " | " + str(board['top-M']) + " | " + str(board['top-R']))
    print("-" + "-" + "-" + "-" + "-" + "-")
    print((str(board['mid-L'])) + " | " + str(board['mid-M']) + " | " + str(board['mid-R']))
    print("-" + "-" + "-" + "-" + "-" + "-")
    print((str(board['lower-L'])) + " | " + str(board['lower-M']) + " | " + str(board['lower-R']))


# Arguments: board dict & players dict
def conditions(board, players):
    if board['top-L'] == players.get('user1') and board['top-M'] == players.get('user1') and board['top-R'] == players.get('user1'):
        print("User1 wins")
        return 1

    if board['mid-L'] == players.get('user1') and board['mid-M'] == players.get('user1') and board['mid-R'] == players.get('user1'):
        print("User1 wins")
        return 1

    if board['lower-L'] == players.get('user1') and board['lower-M'] == players.get('user1') and board['lower-R'] == players.get('user1'):
        print("User1 wins")
        return 1

    if board['top-M'] == players.get('user1') and board['mid-M'] == players.get('user1') and board['lower-M'] == players.get('user1'):
        print("User1 wins")
        return 1

    if board['top-R'] == players.get('user1') and board['mid-R'] == players.get('user1') and board['lower-R'] == players.get('user1'):
        print("User1 wins")
        return 1

    if board['top-L'] == players.get('user1') and board['mid-L'] == players.get('user1') and board['lower-L'] == players.get('user1'):
        print("User1 wins")
        return 1

    if board['top-L'] == players.get('user1') and board['mid-M'] == players.get('user1') and board['lower-R'] == players.get('user1'):
        print("User1 wins")
        return 1

    if board['top-R'] == players.get('user1') and board['mid-M'] == players.get('user1') and board['lower-L'] == players.get('user1'):
        print("User1 wins")
        return 1

    # Computer Conditions
    if board['top-L'] == players.get('computer') and board['top-M'] == players.get('computer') and board['top-R'] == players.get('computer'):
        print("Computer wins")
        return 1

    if board['mid-L'] == players.get('computer') and board['mid-M'] == players.get('computer') and board['mid-R'] == players.get('computer'):
        print("Computer wins")
        return 1

    if board['lower-L'] == players.get('computer') and board['lower-M'] == players.get('computer') and board['lower-R'] == players.get('computer'):
        print("Computer wins")
        return 1

    if board['top-M'] == players.get('computer') and board['mid-M'] == players.get('computer') and board['lower-M'] == players.get('computer'):
        print("Computer wins")
        return 1

    if board['top-R'] == players.get('computer') and board['mid-R'] == players.get('computer') and board['lower-R'] == players.get('computer'):
        print("Computer wins")
        return 1

    if board['top-L'] == players.get('computer') and board['mid-L'] == players.get('computer') and board['lower-L'] == players.get('computer'):
        print("Computer wins")
        return 1

    if board['top-L'] == players.get('computer') and board['mid-M'] == players.get('computer') and board['lower-R'] == players.get('computer'):
        print("Computer wins")
        return 1

    if board['top-R'] == players.get('computer') and board['mid-M'] == players.get('computer') and board['lower-L'] == players.get('computer'):
        print("Computer wins")
        return 1


    # start game
def letsPlayAGame():
    boardDict = {
        'top-L': "",
        'top-M': "",
        'top-R': "",
        'mid-L': "",
        'mid-M': "",
        'mid-R': "",
        'lower-L': "",
        'lower-M': "",
        'lower-R': "",
    }

    print("Welcome to Tic Tac Toe")
    print("You will play against the computer")
    print("Choose X or O to play")

    while True:
        user1 = input()
        try:
            if user1 == "X":
                computer = "O"
                break

            elif user1 == "O":
                computer = "X"
                break

        except:
            pass
        print("Please Enter X or O for your choice")

    playersDict = {
        'user1': user1,
        'computer': computer
    }

    print("User1 is " + user1 + " and Computer is " + computer)
    print("User goes first")
    turnsLeft = ["top-L", "top-M", "top-R", "mid-L", "mid-M", "mid-R", "lower-L", "lower-M", "lower-R"]
    flag = 0

    while True:
        print("Place where you want to put your piece: ")
        print(turnsLeft)
        turn = 0
        # turnList = [user1, computer]

        if turn == 0:
            playerChoice = input()
            boardDict[playerChoice] = user1
            turnsLeft.remove(playerChoice)
            printBoard(boardDict)
            condition = conditions(boardDict, playersDict)
            if condition == 1:
                break
            else:
                turn = turn + 1
                print('\n')

        if turn == 1:
            print("Computer's turn")
            randomChoice = random.choice(turnsLeft)
            boardDict[randomChoice] = computer
            printBoard(boardDict)
            condition = conditions(boardDict, playersDict)
            if condition == 1:
                break
            else:
                turn = turn - 1
                print('\n')

# start game
letsPlayAGame()




