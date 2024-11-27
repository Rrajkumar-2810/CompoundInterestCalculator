import random
import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.configure(bg="Light blue")

# Generate a random number
number_to_guess = random.randint(1, 100)
chances = 7
guess_counter = 0

# Define functions
def check_guess():
    global guess_counter
    guess_counter += 1
    try:
        my_guess = int(entry_guess.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
    
    if my_guess == number_to_guess:
        messagebox.showinfo("Congratulations!", f'The number is {number_to_guess}. You found it right in {guess_counter} attempts!')
        reset_game()
    elif guess_counter >= chances:
        messagebox.showinfo("Game Over", f'Oops, the number was {number_to_guess}. Better luck next time!')
        reset_game()
    elif my_guess > number_to_guess:
        label_feedback.config(text="Your guess is too high!")
    else:
        label_feedback.config(text="Your guess is too low!")

def reset_game():
    global number_to_guess, guess_counter
    number_to_guess = random.randint(1, 100)
    guess_counter = 0
    entry_guess.delete(0, tk.END)
    label_feedback.config(text="You have 7 chances to guess the number.")

# Create and place widgets
label_title = tk.Label(root, text="Welcome to the Number Guessing Game!", font=("Arial", 14), bg="yellow")
label_title.pack(pady=10)

label_instruction = tk.Label(root, text="Guess a number between 1 and 100:", bg="orange")
label_instruction.pack()

entry_guess = tk.Entry(root, font=("Arial", 12), width=10)
entry_guess.pack(pady=5)

button_guess = tk.Button(root, text="Guess", command=check_guess, bg="light green")
button_guess.pack(pady=10)

label_feedback = tk.Label(root, text="You have 7 chances to guess the number.", font=("Arial", 12), bg="light grey")
label_feedback.pack(pady=10)

button_reset = tk.Button(root, text="Reset Game", command=reset_game, bg="Red")
button_reset.pack(pady=10)

# Run the application
root.mainloop()
