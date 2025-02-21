import tkinter as tk
from tkinter import messagebox
import random

# Game choices and rules
choices = {'s': 'Snake', 'w': 'Water', 'g': 'Gun'}
rules = {('s', 'g'): 'computer', ('s', 'w'): 'human',
         ('w', 's'): 'computer', ('w', 'g'): 'human',
         ('g', 's'): 'human', ('g', 'w'): 'computer'}

# Initialize game variables
chance = 10
computer_score = 0
human_score = 0
round_number = 1

# Function to play a round
def play_round(user_choice):
    global round_number, computer_score, human_score

    if round_number > chance:
        return  # Stop the game if chances are over

    computer_choice = random.choice(list(choices.keys()))
    winner = None

    # Determine winner
    if user_choice == computer_choice:
        result_text.set("🤝 It's a tie!")
    else:
        winner = rules.get((user_choice, computer_choice))
        if winner == "human":
            human_score += 1
            result_text.set(f"🎉 You Win! ({choices[user_choice]} beats {choices[computer_choice]})")
        else:
            computer_score += 1
            result_text.set(f"💻 Computer Wins! ({choices[computer_choice]} beats {choices[user_choice]})")

    # Update scores
    score_text.set(f"📊 Score -> You: {human_score} | Computer: {computer_score}")
    round_text.set(f"🔄 Round {round_number} of {chance}")

    # Move to next round
    round_number += 1

    # End game if chances are over
    if round_number > chance:
        end_game()

# Function to display final results
def end_game():
    if human_score > computer_score:
        final_message = "🏆 Congratulations! You won the game! 🎉"
    elif human_score < computer_score:
        final_message = "😞 Computer wins the game! Better luck next time."
    else:
        final_message = "🤝 It's a tie!"

    messagebox.showinfo("Game Over", f"{final_message}\n\nFinal Score:\nYou: {human_score} | Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Snake, Water, Gun Game")
root.geometry("400x500")
root.resizable(False, False)
root.config(bg="lightblue")

# Game title
title_label = tk.Label(root, text="🐍 Snake, Water, Gun Game 🎮", font=("Arial", 16, "bold"), bg="lightblue")
title_label.pack(pady=10)

# Instruction label
instruction_label = tk.Label(root, text="Choose one:", font=("Arial", 12), bg="lightblue")
instruction_label.pack()

# Display game result
result_text = tk.StringVar()
result_text.set("Make your choice!")
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14, "bold"), fg="darkred", bg="lightblue")
result_label.pack(pady=10)

# Score tracker
score_text = tk.StringVar()
score_text.set("📊 Score -> You: 0 | Computer: 0")
score_label = tk.Label(root, textvariable=score_text, font=("Arial", 12), bg="lightblue")
score_label.pack()

# Round tracker
round_text = tk.StringVar()
round_text.set(f"🔄 Round {round_number} of {chance}")
round_label = tk.Label(root, textvariable=round_text, font=("Arial", 12), bg="lightblue")
round_label.pack(pady=5)

# Buttons for choices
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=20)

snake_button = tk.Button(button_frame, text="🐍 Snake", font=("Arial", 14), width=10, command=lambda: play_round('s'))
snake_button.grid(row=0, column=0, padx=10)

water_button = tk.Button(button_frame, text="💧 Water", font=("Arial", 14), width=10, command=lambda: play_round('w'))
water_button.grid(row=0, column=1, padx=10)

gun_button = tk.Button(button_frame, text="🔫 Gun", font=("Arial", 14), width=10, command=lambda: play_round('g'))
gun_button.grid(row=0, column=2, padx=10)

# Start the main event loop
root.mainloop()
