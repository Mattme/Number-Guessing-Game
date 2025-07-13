# Number Guessing Game
from random import randrange
import tkinter as tk

# Creating window with input and button
frame = tk.Tk()
frame.title("Number Guessing Game")
frame.geometry("300x200")

label = tk.Label(frame, text="Guess a number between 0 and 100")
label.pack(pady=10)

input = tk.Entry(frame)
input.pack()

def checkguess():
    guess = input.get()

    try:
        number = int(guess)
    except ValueError:
        output_label.config(text=f"Please enter a number.")
        return

    if number == number_to_guess: 
        output_label.config(text=f"You guessed right!")
    elif number < number_to_guess:
        output_label.config(text=f"Your guess is too low.")
    elif number > number_to_guess:
        output_label.config(text=f"Your guess is too high.")
    else:
        output_label.config(text=f"Not a valid guess.")

button = tk.Button(frame, text="Enter", command=checkguess)
button.pack(pady=10)

output_label = tk.Label(frame, text="")
output_label.pack()

# Defining guessing number
number_to_guess = randrange(100)

frame.mainloop()