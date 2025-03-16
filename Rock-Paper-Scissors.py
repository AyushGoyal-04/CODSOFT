import random
import tkinter as tk
from tkinter import messagebox

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n"
    if winner == "tie":
        result_text += "It's a tie!"
    elif winner == "user":
        result_text += "You win!"
    else:
        result_text += "You lose!"
    messagebox.showinfo("Result", result_text)

def play_game(user_choice):
    global user_score, computer_score
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1
    
    score_label.config(text=f"Scores:\nYou: {user_score}\nComputer: {computer_score}")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

user_score = 0
computer_score = 0

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

welcome_label = tk.Label(root, text="Welcome to Rock-Paper-Scissors Game!", font=("Helvetica", 16))
welcome_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play_game("rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play_game("paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play_game("scissors"))
scissors_button.grid(row=0, column=2, padx=5)

score_label = tk.Label(root, text="Scores:\nYou: 0\nComputer: 0", font=("Helvetica", 14))
score_label.pack(pady=10)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()