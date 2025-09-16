#Amőba
import random

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

gameOn = True
player_1_turn = True
winner = "draw"
a = False

def show_board():
    if player_1_turn:
        print("\nAz O játékos következik.")
    else:
        print("\nAz X játékos következik.")
    print("   1   2   3 ")
    for i in range(3):
        print(f"{i+1}  {board[i][0]}   {board[i][1]}   {board[i][2]}")

def read_and_put_symbol(player_turn):
    global player_1_turn
    correct = False
    while not correct:
        if player_turn:
            sor = int(input("Adj meg egy sort:\n"))
            while sor < 1 or sor > 3:
                print("Nincs ilyen sor!, Kérlek adj meg egy újat.")
                sor = int(input("Adj meg egy sort:\n"))

            oszlop = int(input("Adj meg egy oszlopot:\n"))
            while oszlop < 1 or oszlop > 3:
                print("Nincs ilyen Oszlop!, Kérlek adj meg egy újat.")
                oszlop = int(input("Adj meg egy oszlopot:\n"))
        else:
            sor = random.randint(1,3)
            oszlop = random.randint(1,3)

        if board[sor-1][oszlop-1] == "-":
            correct = True
            if player_1_turn:
                board[sor-1][oszlop-1] = "O"
            else:
                board[sor-1][oszlop-1] = "X"
        elif player_1_turn:
            print("Ez a hely már elvan foglalva kérlek válasz egy másik mezőt!")

def Set_win():
    global winner
    if player_1_turn:
        winner = "O wins"
    else:
        winner = "X wins"

def check_for_win():
    #sorok
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "-":
            Set_win()
            return True
    #oszlopok
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != "-":
            Set_win()
            return True
    #átlók
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        Set_win()
        return True
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != "-":
        Set_win()
        return True
    return False
    
def check_for_draw():
    for lista in board:
        if "-" in lista:
            return False
    return True

answer = input("Számítógép ellen szeretnél játszani? (igen/nem)\n")
if answer == "igen":
    against_computer = True
else:
    against_computer = False

while gameOn:
    show_board()
    if not player_1_turn and against_computer:
        read_and_put_symbol(False)
    else:
        read_and_put_symbol(True)
    have_winner = check_for_win()

    if have_winner:
        gameOn = False
        break

    draw = check_for_draw()
    if draw:
        break

    player_1_turn = not player_1_turn
    
show_board()
print(winner)

    