#A module for my TicTacToe game

import tkinter as tk
from tkinter import ttk

BOARD_LEN = 3

window = tk.Tk()
window.config(bg="skyblue")
window.title("TicTacToe")

current_player = 'X'

Board = [[''] * BOARD_LEN] * BOARD_LEN

for i in range (BOARD_LEN):
    window.rowconfigure(i, weight = 1)
    window.columnconfigure(i, weight = 1)

def create_board():
    for i in range (BOARD_LEN):
            for j in range (BOARD_LEN):
                Board[i][j] = ttk.Button(window, text = '', command = lambda i=i, j=j: board_clicked(i, j))
                Board[i][j].grid(column = i, row = j)

def board_clicked(x, y):
    global current_player
    print(x, y, current_player)
    Board[x][y] = ttk.Button(window, text = current_player)
    Board[x][y].grid(column = x, row = y)
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'

create_board()

window.mainloop()