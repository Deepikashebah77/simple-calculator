import tkinter as tk

# Function to handle button click
def on_click(button_text):
    current_expression = entry.get()
    if button_text == "=":
        try:
            result = str(eval(current_expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Setting up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Adding buttons to the grid
row_value = 1
col_value = 0
for button_text in buttons:
    button = tk.Button(root, text=button_text, width=5, height=2, font=('Arial', 18), command=lambda text=button_text: on_click(text))
    button.grid(row=row_value, column=col_value)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Start the Tkinter event loop
root.mainloop()
