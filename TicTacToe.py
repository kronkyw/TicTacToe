#A module for my TicTacToe game

import tkinter as tk

BOARD_LEN = 3

Board = [['X'] * BOARD_LEN] * BOARD_LEN


window = tk.Tk()
window.config(bg="skyblue")
tk.title(window, text="TicTacToe").pack()

for i in range (BOARD_LEN):
    for j in range (BOARD_LEN):
        tk.Button
        (
            window,
            text = f"Cell ({i}, {j})",
            width = 10
            height = 10
        ).grid(row=i, column=j)

window.mainloop()