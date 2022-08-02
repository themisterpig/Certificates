global position
board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
from IPython.display import clear_output


def display(board):
    clear_output(wait=True)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def user_choise():
    acceptance_range = range(0, 10)
    within_range = False
    choise = "choise"
    while not within_range or not choise.isdigit():
        choise = input("Please enter a value:")

        if choise.isdigit():

            if int(choise) in acceptance_range:
                if board[int(choise)] == " ":
                    within_range = True

    return int(choise)


def check_won(board):
    check = False
    for a in range(1, 10, 3):
        if not board[a] == " " and board[a] == board[a + 1] == board[a + 2]:
            return True
            break
    for a in range(3):
        if not board[a] == " " and board[a] == board[a + 3] == board[a + 6]:
            return True
            break
    if not board[3] == " " and board[7] == board[5] == board[3]:
        return True

    if not board[1] == " " and board[1] == board[5] == board[9]:
        return True
    return False

def clean_board():
    global board
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def isfull(board):
    for a in board:
        if a == " ":
            return False

    return True

end = True
i = 0
draw=0
while end:
    if i == 2: i = 0
    available = ["X", "O"]

    board[user_choise()] = available[i]
    i += 1
    draw +=draw
    if not check_won(board) and isfull(board):
        print("Draw")
        choise = input("Wanna play again? (y/n)")
        if choise == "n": end = False
        i = 0
        clean_board()
    elif not check_won(board):
        display(board)
    else:
        display(board)
        if i == 2:
            print(available[1]," Won")
        else:
            print(available[0]," Won")

        choise = input("Wanna play again? (y/n)")
        if choise == "n": end = False
        i = 0
        clean_board()
