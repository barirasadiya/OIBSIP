import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number ≥ 4")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digit_var.get()
    use_symbols = symbol_var.get()

    if not (use_upper or use_lower or use_digits or use_symbols):
        messagebox.showerror("Error", "Select at least one character type")
        return

    exclude_chars = exclude_entry.get()

    char_pool = ""
    password = []

    if use_upper:
        chars = "".join(c for c in string.ascii_uppercase if c not in exclude_chars)
        char_pool += chars
        password.append(random.choice(chars))

    if use_lower:
        chars = "".join(c for c in string.ascii_lowercase if c not in exclude_chars)
        char_pool += chars
        password.append(random.choice(chars))

    if use_digits:
        chars = "".join(c for c in string.digits if c not in exclude_chars)
        char_pool += chars
        password.append(random.choice(chars))

    if use_symbols:
        chars = "".join(c for c in string.punctuation if c not in exclude_chars)
        char_pool += chars
        password.append(random.choice(chars))

    if not char_pool:
        messagebox.showerror("Error", "All selected characters are excluded")
        return

    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    password_output.delete(0, tk.END)
    password_output.insert(0, "".join(password))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_output.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Advanced Password Generator")
root.state('zoomed')

tk.Label(root, text="Password Length").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var).pack( padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var).pack( padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=digit_var).pack( padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=symbol_var).pack( padx=20)

tk.Label(root, text="Exclude Characters (optional)").pack(pady=5)
exclude_entry = tk.Entry(root)
exclude_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)

password_output = tk.Entry(root, font=("Courier", 12), justify="center")
password_output.pack(pady=10, fill="x", padx=20)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

root.mainloop()
