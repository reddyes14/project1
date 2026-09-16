import tkinter as tk
import random
number = random.randint(1, 100)
attempts = 0


def check_guess():
    global number, attempts

    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="Please enter a valid number.")
        return

    guess = int(guess)
    attempts += 1

    if guess < number:
        result_label.config(text="Too low. Try again.")
    elif guess > number:
        result_label.config(text="Too high. Try again.")
    else:
        result_label.config(text=f"Correct! The number was {number}. Attempts: {attempts}")
        guess_button.config(state="disabled")
        entry.config(state="disabled")

    entry.delete(0, tk.END)


def restart_game():
    global number, attempts
    number = random.randint(1, 100)
    attempts = 0
    result_label.config(text="I'm thinking of a number between 1 and 100.")
    entry.config(state="normal")
    guess_button.config(state="normal")
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("320x220")

title_label = tk.Label(root, text="Guess the Number (1-100)", font=("Arial", 14))
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

guess_button = tk.Button(root, text="Guess", command=check_guess)
guess_button.pack(pady=5)

result_label = tk.Label(root, text="I'm thinking of a number between 1 and 100.", wraplength=280)
result_label.pack(pady=10)

restart_button = tk.Button(root, text="Play Again", command=restart_game)
restart_button.pack(pady=5)

root.bind("<Return>", lambda event: check_guess())

root.mainloop()
