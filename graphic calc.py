import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def set_numbers(self, x, y):
        self.x = float(x)
        self.y = float(y)
    
    def add(self):
        return self.x + self.y
    
    def subtract(self):
        return self.x - self.y
    
    def multiply(self):
        return self.x * self.y
    
    def divide(self):
        if self.y != 0:
            return self.x / self.y
        else:
            return "Cannot divide by zero"

class ScientificCalculator(Calculator):
    def square(self):
        return self.x ** 2
    
    def cube(self):
        return self.x ** 3
    
    def power(self, y):
        return self.x ** y

def calculate():
    x = entry_x.get()
    y = entry_y.get()

    if choice.get() == 1:
        basic_calc.set_numbers(x, y)
        if operation.get() == '+':
            result.set(basic_calc.add())
        elif operation.get() == '-':
            result.set(basic_calc.subtract())
        elif operation.get() == '*':
            result.set(basic_calc.multiply())
        elif operation.get() == '/':
            result.set(basic_calc.divide())
    elif choice.get() == 2:
        scientific_calc.set_numbers(x, y)
        if operation.get() == 'square':
            result.set(scientific_calc.square())
        elif operation.get() == 'cube':
            result.set(scientific_calc.cube())
        elif operation.get() == 'power':
            y_power = float(entry_power.get())
            result.set(scientific_calc.power(y_power))

def show_about():
    messagebox.showinfo("About", "This is a simple calculator GUI.")

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create calculator instances
basic_calc = Calculator()
scientific_calc = ScientificCalculator()

# Create GUI elements
choice = tk.IntVar()
operation = tk.StringVar()
result = tk.StringVar()

label_x = tk.Label(root, text="Enter the first number:")
entry_x = tk.Entry(root)

label_y = tk.Label(root, text="Enter the second number:")
entry_y = tk.Entry(root)

label_power = tk.Label(root, text="Enter the power:")
entry_power = tk.Entry(root)

radio_basic = tk.Radiobutton(root, text="Basic Calculator", variable=choice, value=1)
radio_scientific = tk.Radiobutton(root, text="Scientific Calculator", variable=choice, value=2)

label_operation = tk.Label(root, text="Select operation:")
radio_add = tk.Radiobutton(root, text="+", variable=operation, value='+')
radio_subtract = tk.Radiobutton(root, text="-", variable=operation, value='-')
radio_multiply = tk.Radiobutton(root, text="*", variable=operation, value='*')
radio_divide = tk.Radiobutton(root, text="/", variable=operation, value='/')
radio_square = tk.Radiobutton(root, text="Square", variable=operation, value='square')
radio_cube = tk.Radiobutton(root, text="Cube", variable=operation, value='cube')
radio_power = tk.Radiobutton(root, text="Power", variable=operation, value='power')

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_about = tk.Button(root, text="About", command=show_about)

label_result = tk.Label(root, textvariable=result)

# Place GUI elements using grid layout
label_x.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_x.grid(row=0, column=1, padx=10, pady=5)

label_y.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
entry_y.grid(row=1, column=1, padx=10, pady=5)

radio_basic.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
radio_scientific.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

label_operation.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
radio_add.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
radio_subtract.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)
radio_multiply.grid(row=4, column=2, padx=10, pady=5, sticky=tk.W)
radio_divide.grid(row=4, column=3, padx=10, pady=5, sticky=tk.W)
radio_square.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
radio_cube.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)
radio_power.grid(row=5, column=2, padx=10, pady=5, sticky=tk.W)

entry_power.grid(row=5, column=3, padx=10, pady=5, sticky=tk.W)

button_calculate.grid(row=6, column=0, padx=10, pady=5)
button_about.grid(row=6, column=1, padx=10, pady=5)

label_result.grid(row=7, column=0, columnspan=4, padx=10, pady=5)

root.mainloop()
