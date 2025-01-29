
import tkinter as tk
from tkinter import StringVar

# Function to update the display when a number or operator is clicked
def button_click(value):
    current = add_text.get()  # Get the current value in the entry widget
    add_text.set(current + str(value))  # Update the entry with the clicked value

# Function to evaluate the expression when "=" is pressed
def evaluate_expression():
    try:
        result = eval(add_text.get())
        add_text.set(result)
    except Exception as e:
        add_text.set("Error")

# Function to clear the display when "C" is pressed
def clear_input():
    add_text.set("")  # Clear the entry widget

# Initialize the main window
root = tk.Tk()
root.title('MY CAL')

# Variable for the display text
add_text = StringVar()

# Screen setup
screen = tk.Entry(root, bg='white', width=13, bd=3, textvariable=add_text, font=('Times New Roman', 25, 'bold'), fg='black')
screen.grid(row=0, columnspan=4)

# Button setup with text, positions, and grid layout
x = 4  # Width of buttons
y = 1  # Height of buttons

bcol = 'gray'  # Background color for buttons
fcol = 'black'  # Foreground color for buttons

# Define the buttons for digits and operators
button_7 = tk.Button(root, text='7', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('7'))
button_8 = tk.Button(root, text='8', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('8'))
button_9 = tk.Button(root, text='9', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('9'))
button_4 = tk.Button(root, text='4', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('4'))
button_5 = tk.Button(root, text='5', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('5'))
button_6 = tk.Button(root, text='6', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('6'))
button_1 = tk.Button(root, text='1', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('1'))
button_2 = tk.Button(root, text='2', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('2'))
button_3 = tk.Button(root, text='3', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('3'))
button_0 = tk.Button(root, text='0', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('0'))

# Define the operator buttons
button_add = tk.Button(root, text='+', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('+'))
button_sub = tk.Button(root, text='-', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('-'))
button_mul = tk.Button(root, text='*', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('*'))
button_div = tk.Button(root, text='/', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=lambda: button_click('/'))

# Define the equals and dot buttons
button_equals = tk.Button(root, text='=', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=evaluate_expression)
button_dot = tk.Button(root, text='.', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol, command=clear_input)

# Define the clearn buttons

button_clear = tk.Button(root, text='c', font=('Times New Roman', 20, 'bold'), bg=bcol, width=x, height=y, fg=fcol,
                         command=clear_input)

# Grid layout for the buttons
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_dot.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_div.grid(row=4, column=3)

button_div.grid(row=4,column=3)
button_clear.grid(row=5,column=0)
# Run the Tkinter event loop
root.mainloop()


