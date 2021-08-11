"""
Let’s create a GUI based simple calculator using Python & Tkinter module.
Which can perform basic following arithmatic operations:
        --> Addition
        --> Subtraction
        --> Multiplication
        --> Division
        --> Percentage

            CALCULATOR
_______________________________________
|                                     |
|                   12 + 15 = 27      |
|_____________________________________|
|                                     |
|     C       Del       %       /     |
|                                     |
|     7        8        9       X     |
|                                     |
|     4        5        6       -     |
|                                     |
|     1        2        3       +     |
|                                     |
|        0          .       =         |
|_____________________________________|
"""

# import everything from tkinter module
import tkinter
from tkinter import *

# Global varible for storing expressions
expression = ""
first_value_of_expression = 0
operator = ""


# MAIN FUNCTION FOR CALCULATING ALL MATHEMATICAL OPERATIONS
def calculation():

    global expression
    global first_value_of_expression
    global operator
    expression2 = expression

    if operator == "+":
        second_value_of_expression = float((expression2.split("+"))[1])
        result = first_value_of_expression + second_value_of_expression
        data.set(result)
        expression = str(result)

    elif operator == "-":
        second_value_of_expression = float((expression2.split("-"))[1])
        result = first_value_of_expression - second_value_of_expression
        data.set(result)
        expression = str(result)

    elif operator == "*":
        second_value_of_expression = float((expression2.split("*"))[1])
        result = first_value_of_expression * second_value_of_expression
        data.set(result)
        expression = str(result)

    elif operator == "/":
        second_value_of_expression = float((expression2.split("/"))[1])
        result = first_value_of_expression / second_value_of_expression
        data.set(result)
        expression = str(result)

    else:
        if operator == "%":
            second_value_of_expression = float((expression2.split("%"))[1])
            result = first_value_of_expression * second_value_of_expression
            result = result / 100
            data.set(result)
            expression = str(result)


def button_1_isclicked():
    global expression
    expression = expression + "1"
    data.set(expression)

def button_2_isclicked():
    global expression
    expression = expression + "2"
    data.set(expression)

def button_3_isclicked():
    global expression
    expression = expression + "3"
    data.set(expression)

def button_4_isclicked():
    global expression
    expression = expression + "4"
    data.set(expression)

def button_5_isclicked():
    global expression
    expression = expression + "5"
    data.set(expression)

def button_6_isclicked():
    global expression
    expression = expression + "6"
    data.set(expression)

def button_7_isclicked():
    global expression
    expression = expression + "7"
    data.set(expression)

def button_8_isclicked():
    global expression
    expression = expression + "8"
    data.set(expression)

def button_9_isclicked():
    global expression
    expression = expression + "9"
    data.set(expression)

def button_0_isclicked():
    global expression
    expression = expression + "0"
    data.set(expression)

def button_dot_isclicked():
    global expression
    expression = expression + "."
    data.set(expression)

def press_button_plus():
    global first_value_of_expression
    global operator
    global expression
    first_value_of_expression = float(expression)
    operator = "+"
    expression = expression + "+"
    data.set(expression)


def press_button_minus():
    global first_value_of_expression
    global operator
    global expression
    first_value_of_expression = float(expression)
    operator = "-"
    expression = expression + "-"
    data.set(expression)

def press_button_multiple():
    global first_value_of_expression
    global operator
    global expression
    first_value_of_expression = float(expression)
    operator = "*"
    expression = expression + "*"
    data.set(expression)

def press_button_divide():
    global first_value_of_expression
    global operator
    global expression
    first_value_of_expression = float(expression)
    operator = "/"
    expression = expression + "/"
    data.set(expression)

def press_button_percent():
    global first_value_of_expression
    global operator
    global expression
    first_value_of_expression = float(expression)
    operator = "%"
    expression = expression + "%"
    data.set(expression)

def press_clear_button():
    global expression
    global first_value_of_expression
    global operator
    expression = ""
    first_value_of_expression = 0
    operator = ""
    data.set(expression)

def press_del_button():
    global expression
    expression = expression[:-1]
    data.set(expression)


# Driver Code
if __name__ == '__main__':

    # Main Window of Calculator
    main_window = tkinter.Tk()
    main_window.geometry("400x500+300+300")
    #main_window.resizable(0,0)
    main_window.title("Calculator")
    main_window.configure(background = "light green")
    
    # StringVar() is the varible class
    # we create an instance of this class
    data = StringVar()

    # Text Level of Main Window
    input_lavel_box = Label(
    main_window,
    text = "",
    textvariable = data,
    anchor = SE,
    font = ("Verdana", 20),
    background = "#ffffff",
    fg = "#000000",
    height=2,
    width=12,
    )
    input_lavel_box.pack(expand = True, fill = "both",)
    
    # Frame 01 of Main Window
    first_row_buttons = Frame(main_window)
    first_row_buttons.pack(expand = True, fill = "both",)

    # Frame 02 of Main Window
    second_row_buttons = Frame(main_window)
    second_row_buttons.pack(expand = True, fill = "both",)

    # Frame 03 of Main Window
    third_row_buttons = Frame(main_window)
    third_row_buttons.pack(expand = True, fill = "both",)

    # Frame 04 of Main Window
    fourth_row_buttons = Frame(main_window)
    fourth_row_buttons.pack(expand = True, fill = "both",)

    # Frame 05 of Main Window
    fifth_row_buttons = Frame(main_window)
    fifth_row_buttons.pack(expand = True, fill = "both",)
    
    # button_all_erase for frame of first_row_buttons
    # Delete or clear all the text of text box
    button_all_erase = Button(
        first_row_buttons,
        text = 'C',
        font = ("Verdana", 25),
        height = 1,
        width = 2,
        #border = 0,
        command = press_clear_button,
    )
    button_all_erase.pack(side = LEFT, expand = True, fill = "both",)
    
    # button_single_digit_erase for frame of first_row_buttons
    # Delete single digit of text box
    button_single_digit_erase = Button(
        first_row_buttons,
        text = 'Del',
        font = ("Verdana", 25),
        height=1,
        width=2,
       #border = 0,
       command = press_del_button,
    )
    button_single_digit_erase.pack(side = LEFT, expand = True, fill = "both",)

    # button_percent for frame of first_row_buttons
    button_percent = Button(
        first_row_buttons,
        text = '%',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = press_button_percent,
    )
    button_percent.pack(side = LEFT, expand = True, fill = "both",)

    # button_divide for frame of first_row_buttons
    button_divide = Button(
        first_row_buttons,
        text = '/',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = press_button_divide,
    )
    button_divide.pack(side = LEFT, expand = True, fill = "both",)

    # button_seven for frame of second_row_buttons
    button_seven = Button(
        second_row_buttons,
        text = '7',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_7_isclicked,
    )
    button_seven.pack(side = LEFT, expand = True, fill = "both",)

    # button_eight for frame of second_row_buttons
    button_eight = Button(
        second_row_buttons,
        text = '8',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_8_isclicked,
    )
    button_eight.pack(side = LEFT, expand = True, fill = "both",)

    # button_nine for frame of second_row_buttons
    button_nine = Button(
        second_row_buttons,
        text = '9',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_9_isclicked,
    )
    button_nine.pack(side = LEFT, expand = True, fill = "both",)

    # button_multiple for frame of second_row_buttons
    button_multiple = Button(
        second_row_buttons,
        text = 'X',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = press_button_multiple,
    )
    button_multiple.pack(side = LEFT, expand = True, fill = "both",)

    # button_four for frame of third_row_buttons
    button_four = Button(
        third_row_buttons,
        text = '4',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_4_isclicked,
    )
    button_four.pack(side = LEFT, expand = True, fill = "both",)

    # button_five for frame of third_row_buttons
    button_five = Button(
        third_row_buttons,
        text = '5',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_5_isclicked,
    )
    button_five.pack(side = LEFT, expand = True, fill = "both",)

    # button_six for frame of third_row_buttons
    button_six = Button(
        third_row_buttons,
        text = '6',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_6_isclicked,
    )
    button_six.pack(side = LEFT, expand = True, fill = "both",)

    # button_minus for frame of third_row_buttons
    button_minus = Button(
        third_row_buttons,
        text = '-',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = press_button_minus,
    )
    button_minus.pack(side = LEFT, expand = True, fill = "both",)

    # button_one for frame of fourth_row_buttons
    button_one = Button(
        fourth_row_buttons,
        text = '1',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_1_isclicked,
    )
    button_one.pack(side = LEFT, expand = True, fill = "both",)

    # button_two for frame of fourth_row_buttons
    button_two = Button(
        fourth_row_buttons,
        text = '2',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_2_isclicked,
    )
    button_two.pack(side = LEFT, expand = True, fill = "both",)

    # button_three for frame of fourth_row_buttons
    button_three = Button(
        fourth_row_buttons,
        text = '3',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_3_isclicked,
    )
    button_three.pack(side = LEFT, expand = True, fill = "both",)

    # button_plus for frame of fourth_row_buttons
    button_plus = Button(
        fourth_row_buttons,
        text = '+',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = press_button_plus,
    )
    button_plus.pack(side = LEFT, expand = True, fill = "both",)

    # button_zero for frame of fifth_row_buttons
    button_zero = Button(
        fifth_row_buttons,
        text = '0',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_0_isclicked,
    )
    button_zero.pack(side = LEFT, expand = True, fill = "both",)

    # button_dot for frame of fifth_row_buttons
    button_dot = Button(
        fifth_row_buttons,
        text = '.',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = button_dot_isclicked,
    )
    button_dot.pack(side = LEFT, expand = True, fill = "both",)

    # button_equal for frame of fifth_row_buttons
    button_equal = Button(
        fifth_row_buttons,
        text = '=',
        font = ("Verdana", 25),
        height=1,
        width=2,
        #border = 0,
        command = calculation,
    )
    button_equal.pack(side = LEFT, expand = True, fill = "both",)
    
    main_window.mainloop()
