import tkinter as tk
import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    label_result.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create and pack widgets
label_prompt = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
label_prompt.pack(pady=10)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_rock = tk.Button(frame_buttons, text="Rock", command=lambda: play_game("rock"))
button_rock.pack(side=tk.LEFT, padx=5)

button_paper = tk.Button(frame_buttons, text="Paper", command=lambda: play_game("paper"))
button_paper.pack(side=tk.LEFT, padx=5)

button_scissors = tk.Button(frame_buttons, text="Scissors", command=lambda: play_game("scissors"))
button_scissors.pack(side=tk.LEFT, padx=5)

label_result = tk.Label(root, text="", font=("Helvetica", 14))
label_result.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
