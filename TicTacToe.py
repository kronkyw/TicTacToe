# Simple TicTacToe game, my first time working with a GUI, so not too pretty
import tkinter as tk
from tkinter import ttk

# Specifies the board length, this can be changed but I wouldnt reccomend it
BOARD_LEN = 3

#Initializes the window
window = tk.Tk()
window.config(bg="skyblue")
window.title("TicTacToe")

turns = 0

restart = ttk.Button(window, text = "Restart", command = lambda: create_board())
label = ttk.Label(window)

current_player = 'X'

# The TicTacToe board
Board = [['' for j in range(BOARD_LEN)] for i in range(BOARD_LEN)]

# Stores the info on the board
Board_info = [['' for i in range(BOARD_LEN)] for j in range(BOARD_LEN)]

frame = ttk.Frame(window)
frame['borderwidth'] = 5

# Configures the rows, should only be done once
for i in range (BOARD_LEN):
    window.rowconfigure(i, weight = 1)
    window.columnconfigure(i, weight = 1)

# Creates the board
def create_board():
    frame.pack()
    restart.pack_forget()
    label.pack_forget()
    for i in range (BOARD_LEN):
            for j in range (BOARD_LEN):
                Board_info[i][j] = ''
                Board[i][j] = ttk.Button(frame, text = '', command = lambda i=i, j=j: button_clicked(i, j))
                Board[i][j].grid(column = i, row = j)

#Switches the players
def switch_player():
    global current_player
    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'

def check_for_win():
    X = 0
    O = 0
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            if Board_info[i][j] == 'X' and O == 0:
                X += 1
            elif Board_info[i][j] == 'O' and X == 0:
                O += 1
            else:
                break
            if X == BOARD_LEN: game_finished('X')
            if O == BOARD_LEN: game_finished('O')
        X = 0
        O = 0
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            if Board_info[j][i] == 'X' and O == 0:
                X += 1
            elif Board_info[j][i] == 'O' and X == 0:
                O += 1
            else:
                break
            if X == BOARD_LEN: game_finished('X')
            if O == BOARD_LEN: game_finished('O')
        X = 0
        O = 0
    for i in range(BOARD_LEN):
        if Board_info[i][i] == 'X' and O == 0:
            X += 1
        elif Board_info[i][i] == 'O' and X == 0:
            O += 1
        else:
            break
        if X == BOARD_LEN: game_finished('X')
        if O == BOARD_LEN: game_finished('O')
    for i in range(BOARD_LEN):
        if Board_info[BOARD_LEN - 1 - i][i] == 'X' and O == 0:
            X += 1
        elif Board_info[BOARD_LEN - 1 - i][i] == 'O' and X == 0:
            O += 1
        else:
            break
        if X == BOARD_LEN: game_finished('X')
        if O == BOARD_LEN: game_finished('O')
    return False

# Activates when someone clicks one of the buttons on the board
def button_clicked(x, y):
    global current_player
    global turns
    Board[x][y] = ttk.Button(frame, text = current_player)
    Board[x][y].grid(column = x, row = y)
    Board_info[y][x] = current_player
    print(x, y, current_player, turns)
    print(Board_info[0])
    print(Board_info[1])
    print(Board_info[2])
    current_player = switch_player()
    turns += 1
    check_for_win()
    if turns == BOARD_LEN * BOARD_LEN and check_for_win() == False:
        game_finished('D')

def game_finished(winner):
    global current_player
    global turns
    turns = 0
    current_player = 'X'
    label.config(text = ("Winner: ", winner))
    frame.pack_forget()
    restart.pack()
    label.pack()

create_board()

window.mainloop()