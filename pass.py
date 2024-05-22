import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Password Length:").grid(row=0, column=0, padx=10, pady=5)
        self.length_var = tk.IntVar(value=12)
        tk.Entry(self.root, textvariable=self.length_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Include Letters:").grid(row=1, column=0, padx=10, pady=5)
        self.letters_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, variable=self.letters_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Include Digits:").grid(row=2, column=0, padx=10, pady=5)
        self.digits_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, variable=self.digits_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Include Symbols:").grid(row=3, column=0, padx=10, pady=5)
        self.symbols_var = tk.BooleanVar(value=True)
        tk.Checkbutton(self.root, variable=self.symbols_var).grid(row=3, column=1, padx=10, pady=5)

        tk.Button(self.root, text="Generate Password", command=self.generate_password).grid(row=4, column=0, columnspan=2, pady=10)

        self.password_entry = tk.Entry(self.root, width=40)
        self.password_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        self.strength_label = tk.Label(self.root, text="Password Strength: ", fg='blue')
        self.strength_label.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        tk.Button(self.root, text="Copy to Clipboard", command=self.copy_password).grid(row=7, column=0, columnspan=2, pady=10)

    def generate_password(self):
        length = self.length_var.get()
        include_letters = self.letters_var.get()
        include_digits = self.digits_var.get()
        include_symbols = self.symbols_var.get()

        if length < 1:
            messagebox.showwarning("Invalid Length", "Password length must be at least 1.")
            return

        characters = ""
        if include_letters:
            characters += string.ascii_letters
        if include_digits:
            characters += string.digits
        if include_symbols:
            characters += ''.join(c for c in string.punctuation if c not in '()[]{}\\/:";,<>?')

        if not characters:
            messagebox.showwarning("Invalid Selection", "You must select at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        
        self.update_strength_label(password)

    def update_strength_label(self, password):
        length = len(password)
        categories = 0
        if any(c in string.ascii_lowercase for c in password):
            categories += 1
        if any(c in string.ascii_uppercase for c in password):
            categories += 1
        if any(c in string.digits for c in password):
            categories += 1
        if any(c in string.punctuation for c in password):
            categories += 1

        strength = "Very Weak"
        if length >= 8 and categories >= 2:
            strength = "Weak"
        if length >= 12 and categories >= 3:
            strength = "Medium"
        if length >= 16 and categories >= 4:
            strength = "Strong"
        if length >= 20 and categories == 4:
            strength = "Very Strong"

        self.strength_label.config(text=f"Password Strength: {strength}")

    def copy_password(self):
        password = self.password_entry.get()
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()