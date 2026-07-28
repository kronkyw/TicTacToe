# A module for my TicTacToe game

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

current_player = 'X'

# The TicTacToe board
Board = [[''] * BOARD_LEN] * BOARD_LEN

# Stores the info on the board
Board_info = [[''] * BOARD_LEN] * BOARD_LEN

frame = ttk.Frame(window, width = 500, height = 500)
frame['borderwidth'] = 5

# Configures the rows, should only be done once
for i in range (BOARD_LEN):
    window.rowconfigure(i, weight = 1)
    window.columnconfigure(i, weight = 1)

# Creates the board
def create_board():
    frame.pack()
    if restart.winfo_exists():
        restart.pack_forget()
    for i in range (BOARD_LEN):
            for j in range (BOARD_LEN):
                Board[i][j] = ttk.Button(frame, text = '', command = lambda i=i, j=j: button_clicked(i, j))
                Board[i][j].grid(column = i, row = j)

#Switches the players
def switch_player():
    global current_player
    if current_player == 'X':
        return 'O'
    elif current_player == 'O':
        return 'X'

#Activates when someone clicks one of the buttons on the board
def button_clicked(x, y):
    global current_player
    global turns
    print(x, y, current_player)
    Board[x][y] = ttk.Button(frame, text = current_player)
    Board[x][y].grid(column = x, row = y)
    Board_info[x][y] = current_player
    current_player = switch_player()
    turns += 1
    if turns == BOARD_LEN * BOARD_LEN:
        game_finished()

def game_finished():
    Board_info = [[''] * BOARD_LEN] * BOARD_LEN
    frame.pack_forget()
    restart.pack()
    

create_board()

window.mainloop()