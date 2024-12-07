import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Small Calculator")

        # Entry widget to display calculations
        self.result_var = tk.StringVar()
        self.entry = tk.Entry(master, textvariable=self.result_var, font=('Red', 16), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Button definitions including backspace
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+',
            '<-'  # Backspace button
        ]

        # Create buttons and place them on the grid
        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def create_button(self, value, row, column):
        button = tk.Button(self.master, text=value, padx=20, pady=20, font=('Arial', 16),
                           command=lambda: self.on_button_click(value))
        button.grid(row=row, column=column)

    def on_button_click(self, value):
        if value == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)  # Evaluate the expression
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif value == 'C':
            self.result_var.set("")  # Clear the entry
        elif value == '<-':
            current_text = self.result_var.get()
            self.result_var.set(current_text[:-1])  # Remove last character
        else:
            current_text = self.result_var.get()
            new_text = current_text + str(value)
            self.result_var.set(new_text)  # Update the entry with the new value

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
