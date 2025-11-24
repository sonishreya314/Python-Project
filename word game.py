import random
import tkinter as tk
from tkinter import messagebox

class GuessTheWordApp:
    def __init__(self, master):
    
        self.master = master
        master.title("Guess The Word - Python GUI")

        self.words = [
            "apple", "banana", "orange", "grape", "melon",
            "cat", "dog", "bird", "fish", "horse",
            "school", "friend", "happy", "smile", "dream",
            "python", "code", "game", "book", "music"
        ]

        self.word_display = tk.StringVar()
        self.guesses_left_var = tk.StringVar()
        self.guessed_letters_var = tk.StringVar()
        self.message_var = tk.StringVar()
        
        self.setup_widgets()
        
        self.new_game()

    def setup_widgets(self):
        """Creates and places all the GUI components (Labels, Entry, Button)."""
        
        title_label = tk.Label(self.master, text="Guess The Word!", font=('Arial', 18, 'bold'), fg='#333')
        title_label.pack(pady=10)

        
        word_label = tk.Label(self.master, textvariable=self.word_display, font=('Courier', 36), bg='#f0f0f0', padx=20, pady=10, relief='groove')
        word_label.pack(pady=15)

        
        tk.Label(self.master, textvariable=self.guesses_left_var, font=('Arial', 12)).pack()

        
        tk.Label(self.master, textvariable=self.guessed_letters_var, font=('Arial', 12)).pack()
        
        
        tk.Label(self.master, textvariable=self.message_var, font=('Arial', 14, 'italic'), fg='red').pack(pady=10)

        
        input_frame = tk.Frame(self.master)
        input_frame.pack(pady=10)
        
        tk.Label(input_frame, text="Enter letter:").pack(side=tk.LEFT, padx=5)

        
        self.guess_entry = tk.Entry(input_frame, width=3, font=('Arial', 14), justify='center')
        self.guess_entry.pack(side=tk.LEFT, padx=5)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess()) # Allows pressing Enter to submit
        
    
        self.submit_button = tk.Button(input_frame, text="Guess", command=self.check_guess, font=('Arial', 12), bg='#4CAF50', fg='white')
        self.submit_button.pack(side=tk.LEFT, padx=10)

    
        tk.Button(self.master, text="New Game", command=self.new_game, font=('Arial', 12)).pack(pady=20)


    def new_game(self):
        """Resets all game state variables and starts a new round."""
        self.secret_word = random.choice(self.words)
        self.word_length = len(self.secret_word)
        self.display = ["_"] * self.word_length
        self.max_guesses = 8 
        self.guesses_left = self.max_guesses
        self.guessed_letters = set()
        
        
        self.update_display()
        self.message_var.set("Start guessing! Good luck!")
        
    
        self.guess_entry.config(state='normal')
        self.submit_button.config(state='normal')
        self.guess_entry.delete(0, tk.END) 
        self.guess_entry.focus_set() 

    def update_display(self):
        """Updates the Tkinter StringVars to refresh the GUI."""
        self.word_display.set(" ".join(self.display))
        self.guesses_left_var.set(f"Guesses Remaining: {self.guesses_left}")
        
        sorted_letters = sorted(list(self.guessed_letters))
        self.guessed_letters_var.set(f"Guessed Letters: {', '.join(sorted_letters)}")

    def check_guess(self):
        """Handles the user's letter submission and updates the game state."""
        
        guess = self.guess_entry.get().lower().strip()
        self.guess_entry.delete(0, tk.END) 
        
        
        if not guess.isalpha() or len(guess) != 1:
            self.message_var.set("Invalid input! Enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_var.set(f"You already guessed '{guess}'. Try another!")
            return

        
        self.guessed_letters.add(guess)
        
        
        if guess in self.secret_word:
            self.message_var.set(f"Correct! '{guess}' is in the word.")
            
            
            for i in range(self.word_length):
                if self.secret_word[i] == guess:
                    self.display[i] = guess
            
            
            if "_" not in self.display:
                self.message_var.set("🎉 YOU WON! 🎉")
                self.end_game(True)
        else:
            
            self.guesses_left -= 1
            self.message_var.set(f"Incorrect. '{guess}' is not in the word.")
            
            
            if self.guesses_left == 0:
                self.message_var.set(f"❌ GAME OVER! Word was: {self.secret_word} ❌")
                self.end_game(False)
        
        
        self.update_display()

    def end_game(self, won):
        """Locks controls and displays the final message."""
        self.guess_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        
        
        if won:
            messagebox.showinfo("Game End", "Congratulations! You guessed the word!")
        else:
            messagebox.showinfo("Game End", f"Game Over! The word was: {self.secret_word}")


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheWordApp(root)
    root.geometry("450x450")
    root.mainloop()