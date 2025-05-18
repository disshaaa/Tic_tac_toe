import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" "]*3 for _ in range(3)]
        self.buttons = [[None]*3 for _ in range(3)]

        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=("Arial", 24), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button

        self.status_label = tk.Label(self.root, text="Player X's turn", font=("Arial", 14))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def on_click(self, row, col):
        if self.board[row][col] != " ":
            return

        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)

        if self.check_winner(self.current_player):
            self.status_label.config(text=f"Player {self.current_player} wins!")
            self.disable_buttons()
            self.ask_restart()
        elif self.is_tie():
            self.status_label.config(text="It's a tie!")
            self.ask_restart()
        else:
            self.current_player = "O" if self.current_player == "X" else "X"
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_tie(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def reset_game(self):
        self.board = [[" "]*3 for _ in range(3)]
        self.current_player = "X"
        self.status_label.config(text="Player X's turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal")

    def ask_restart(self):
        result = messagebox.askyesno("Game Over", "Do you want to play again?")
        if result:
            self.reset_game()
        else:
            self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
