# imports
import tkinter as tk
from tkinter import font
from typing import NamedTuple
from itertools import cycle

# Test code
'''
print("Hello World")
name = input()
print(name)
'''


# Player class
class Player(NamedTuple):
    label: str
    color: str


# Move class and its logic
class Move(NamedTuple):
    row: int
    col: int
    label: str = ""

BOARD_SIZE = 3
DEFAULT_PLAYERS = (
    Player(label='X', color='red'),
    Player(label='O', color='yellow'),
)

# Game class here
class TicTacToeGame:
    def __init__(self, players=DEFAULT_PLAYERS, board_size=BOARD_SIZE):
        self.players = cycle(players)
        self.board_size = board_size
        self.current_player = next(self.players)
        self.winner_combo = []
        self._current_moves = []
        self._has_winner = False
        self._winning_conditions = []
        self._setup_board()

# TicTacToeBoard class here - bulk of the interface
class TicTacToeBoard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic-Tac-Toe Game')
        self._cells = {}
        self._create_board_display()
        self._create_board_grid()

    def _create_board_display(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight="bold"),
        )
        self.display.pack()

    def _create_board_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()
        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)
            self.columnconfigure(row, weight=1, minsize=75)
            for col in range(3):
                button = tk.Button(
                    master=grid_frame,
                    text="",
                    font=font.Font(size=36, weight='bold'),
                    fg='black',
                    width=3,
                    height=2,
                    highlightbackground="lightblue",
                )
                self._cells[button] = (row, col)
                button.grid(
                    row=row,
                    column=col,
                    padx=5,
                    pady=5,
                    sticky='nsew'
                )


# Code initialization
def main():
    board = TicTacToeBoard()
    board.mainloop()


if __name__ == "__main__":
    main()
