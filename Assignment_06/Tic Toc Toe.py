
import pyfiglet
import datetime
import random
from colorama import Fore


def show():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED, cell, Fore.RESET, end = " ")
            elif cell == "O":
                print(Fore.BLUE, cell, Fore.RESET, end = " ")
            else:
                print(Fore.WHITE, cell, Fore.RESET, end = " ")
        print()

def check_game():

        for ii in range(2):

            for i in range(3):
                if game_board[i][0] == block[ii] and game_board[i][1] == block[ii] and game_board[i][2] == block[ii]:
                    print(player[ii], " wins 👏")
                    b = datetime.datetime.now()
                    c = b - a
                    print("game's time: ", int(c.total_seconds()), "sec")
                    exit()
                elif game_board[0][i] == block[ii] and game_board[1][i] == block[ii] and game_board[2][i] == block[ii]:
                    print(player[ii], " wins 👏")
                    b = datetime.datetime.now()
                    c = b - a
                    print("game's time: ", int(c.total_seconds()), "sec")
                    exit()
                elif game_board[0][0] == block[ii] and game_board[1][1] == block[ii] and game_board[2][2] == block[ii] or game_board[2][0] == block[ii] and game_board[1][1] == block[ii] and game_board[0][2] == block[ii]:
                    print(player[ii], " wins 👏")
                    b = datetime.datetime.now()
                    c = b - a
                    print("game's time: ", int(c.total_seconds()), "sec")
                    exit()
                elif game_board[0][0] != "-" and game_board[1][0] != "-" and game_board[2][0] != "-" and game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-"and game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-":
                    print("darw!")
                    b = datetime.datetime.now()
                    c = b - a
                    print("game's time: ", int(c.total_seconds()), "sec")
                    exit()


print("1: Player vs CPU")
print("2: Player vs Player")
choice = (input("please enter your choice (1 or 2): "))

a = datetime.datetime.now()

title = pyfiglet.figlet_format("Tic Tac Toe", font = "slant")
print(title)

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]
show()

if choice == "1":
    player = ["player", "CPU"]
    block = ["X", "O"]

    while True:
            
        print("player")

        while True:
            row = int(input("row: "))
            col = int(input("col: "))

            if 0 <= row <=2 and 0 <= col <=2:

                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("This block has already been selected")

            else:
                print("Your choice should be between 0 and 2!")

        show()
        check_game()

        print("CPU")

        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                break
            else:
                print("This block has already been selected")

        show()
        check_game()

elif choice == "2":
    player = ["player1", "player2"]
    block = ["X", "O"]

    while True:

        for i in range(2):
            
            print(player[i])

            while True:
                row = int(input("row: "))
                col = int(input("col: "))

                if 0 <= row <=2 and 0 <= col <=2:

                    if game_board[row][col] == "-":
                        game_board[row][col] = block[i]
                        break
                    else:
                        print("This block has already been selected")

                else:
                    print("Your choice should be between 0 and 2!")

            show()
            check_game()
