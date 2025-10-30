import tkinter as tk
import tkinter

# This is called when a button is pressed.
# It activates the button handler
def which_button(button_text):
    buttonHandler(button_text)

# Deals and processes the button presses
def buttonHandler(button_text):
    global number
    global total
    global operator

    if button_text == "C":
        number = 0
        total = 0
        labeltext.set("0")

    elif button_text == "+":
        total = total+int(number)
        number = "0"
        operator = button_text
        labeltext.set(operator)


    elif button_text == "-":
        total = total+int(number)
        number = "0"
        operator = button_text
        labeltext.set(operator)


    elif button_text == "*":
        total = total+int(number)
        number = "0"
        operator = button_text
        labeltext.set(operator)


    elif button_text == "/":
        total = total+int(number)
        number = "0"
        operator = button_text
        labeltext.set(operator)


    elif button_text == "=":
        if operator == "+":
            total = total+int(number)
            operator=""
        elif operator == "-":
            total  =total-int(number)
            operator = ""
        elif operator == "*":
            total = total*int(number)
            operator = ""
        elif operator == "/":
            total = total/int(number)
            operator = ""
        elif operator=="":
            total = total
        number = "0"
        labeltext.set(total)

    else:
        if int(number) == 0:
            number = button_text
        else:
            number = number + button_text
        labeltext.set(number)


# global variable for total
number = "0"
total = 0
operator = ""

# Makes the main window tk
window = tk.Tk()
window.title("Sigma 67 Ⓒ1969")

# Default value for output / input box
labeltext = tk.StringVar()
labeltext.set("0")

# Create the buttons and other widgets
label1 = tk.Label(textvariable=labeltext, font=("Arial", 25), height=3)
button1 = tk.Button(text="1", height=3, width=6, font=("Arial", 25), command=lambda: which_button("1"))
button2 = tk.Button(text="2", height=3, width=6, font=("Arial", 25),command=lambda: which_button("2"))
button3 = tk.Button(text="3", height=3, width=6, font=("Arial", 25),command=lambda: which_button("3"))
button4 = tk.Button(text="4", height=3, width=6, font=("Arial", 25),command=lambda: which_button("4"))
button5 = tk.Button(text="5", height=3, width=6, font=("Arial", 25),command=lambda: which_button("5"))
button6 = tk.Button(text="6", height=3, width=6, font=("Arial", 25),command=lambda: which_button("6"))
button7 = tk.Button(text="7", height=3, width=6, font=("Arial", 25),command=lambda: which_button("7"))
button8 = tk.Button(text="8", height=3, width=6, font=("Arial", 25),command=lambda: which_button("8"))
button9 = tk.Button(text="9", height=3, width=6, font=("Arial", 25),command=lambda: which_button("9"))
button0 = tk.Button(text="0", height=3, width=6, font=("Arial", 25),command=lambda: which_button("0"))
cancel = tk.Button(text="C", height=3, width=6, font=("Arial", 25),command=lambda: which_button("C"))
plus = tk.Button(text="+", height=3, width=6, font=("Arial", 25),command=lambda: which_button("+"))
minus = tk.Button(text="-", height=3, width=6, font=("Arial", 25),command=lambda: which_button("-"))
times = tk.Button(text="*", height=3, width=6, font=("Arial", 25),command=lambda: which_button("*"))
divide = tk.Button(text="/", height=3, width=6, font=("Arial", 25),command=lambda: which_button("/"))
equals = tk.Button(text="=", height=3, width=6, font=("Arial", 25),command=lambda: which_button("="))

# Adds the buttons and lays them out on the window
# Row 0
label1.grid(row=0, columnspan=4)

# Row 1
button7.grid(row=1, column=1)
button8.grid(row=1, column=2)
button9.grid(row=1, column=3)
times.grid(row=1, column=4)

# Row 2
button4.grid(row=2, column=1)
button5.grid(row=2, column=2)
button6.grid(row=2, column=3)
divide.grid(row=2, column=4)

# Row 3
button1.grid(row=3, column=1)
button2.grid(row=3, column=2)
button3.grid(row=3, column=3)
minus.grid(row=3, column=4)

# Row 4
cancel.grid(row=4, column=1)
button0.grid(row=4, column=2)
equals.grid(row=4,column=3)
plus.grid(row=4, column=4)

# Must be added to keep the window open
tk.mainloop()