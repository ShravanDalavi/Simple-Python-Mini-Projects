import tkinter as tk
from tkinter import messagebox

# Initialize the game variables
current_player = "X"  # Starting player
moves = 0  # Total moves made

# Create the main Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Function to check if any player has won
def check_win():
    global moves
    # Check rows
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != " ":
            return buttons[row][0]["text"]
    # Check columns
    for col in range(3):
        if buttons[0][col]["text"] == buttons[1][col]["text"] == buttons[2][col]["text"] != " ":
            return buttons[0][col]["text"]
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != " ":
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != " ":
        return buttons[0][2]["text"]
    # Check for tie
    if moves == 9:
        return "tie"
    return None

# Function to handle button click
def handle_click(row, col):
    global current_player, moves
    if buttons[row][col]["text"] == " ":
        buttons[row][col]["text"] = current_player
        moves += 1
        result = check_win()
        if result is not None:
            if result == "tie":
                messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            else:
                messagebox.showinfo("Tic-Tac-Toe", f"Player {result} wins!")
            reset_board()
        else:
            # Switch players
            current_player = "O" if current_player == "X" else "X"

# Function to reset the board
def reset_board():
    global current_player, moves
    current_player = "X"
    moves = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = " "

# Create a 3x3 grid of buttons
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=('Arial', 20), width=10, height=4,
                                  command=lambda i=i, j=j: handle_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Run the main loop
root.mainloop()
