import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def evaluate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

# Function to update the expression in the entry field
def update_expression(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(symbol))

# Function to clear the entry field
def clear_expression():
    entry.delete(0, tk.END)

# Function to handle equals button
def calculate():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create the entry widget for displaying expressions
entry = tk.Entry(root, width=20, font=('Arial', 18), bd=8, insertwidth=2, justify='right')
entry.grid(row=0, column=0, columnspan=5)

# Define the buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.','+','='
]

# Create and place buttons on the grid
row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), 
                  command=calculate).grid(row=row_val, column=col_val, columnspan=2)
        col_val += 2
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), 
                  command=lambda b=button: update_expression(b)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), 
          command=clear_expression).grid(row=row_val, column=col_val)

# Start the main loop
root.mainloop()
