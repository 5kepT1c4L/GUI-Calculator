from tkinter import *
from pygame import mixer

#TK window setup
tk = Tk()
tk.title("Calculator")
tk.geometry('600x600')
tk.configure(bg="pink")

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)


    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


def play_song():
    mixer.init()
    mixer.music.load(r'C:\Users\jinge\Downloads\song.mp3')
    mixer.music.play()

equation = StringVar()
    







#Frame for the equation input
frame1 = Frame(tk, highlightbackground="blue", highlightthickness=1,width=600, height=80, bd= 0)
frame1.pack()
frame1.pack_propagate(False)

equation_area = Label(frame1, textvariable=equation, font=("Times", 50))
equation_area.pack()

#frame for the buttons
buttons_frame = Frame(tk, highlightbackground="blue", highlightthickness=1, width=360, height=520, bd=0)
buttons_frame.pack(side="left")

#frame for the operation signs
operation_frame = Frame(tk, highlightbackground="blue", highlightthickness=1, width=240, height=520, bd=0)
operation_frame.pack(side="right")

#buttons 1-9
button1 = Button(buttons_frame, text="1", width=16, height = 8, bg="pink", command=lambda: press(1))
button2 = Button(buttons_frame, text="2", width=16, height = 8, bg="pink", command=lambda: press(2))
button3 = Button(buttons_frame, text="3", width=16, height = 8, bg="pink", command=lambda: press(3))
button4 = Button(buttons_frame, text="4", width=16, height = 8, bg="pink", command=lambda: press(4))
button5 = Button(buttons_frame, text="5", width=16, height = 8, bg="pink", command=lambda: press(5))
button6 = Button(buttons_frame, text="6", width=16, height = 8, bg="pink", command=lambda: press(6))
button7 = Button(buttons_frame, text="7", width=16, height = 8, bg="pink", command=lambda: press(7))
button8 = Button(buttons_frame, text="8", width=16, height = 8, bg="pink", command=lambda: press(8))
button9 = Button(buttons_frame, text="9", width=16, height = 8, bg="pink", command=lambda: press(9))
button0 = Button(buttons_frame, text="0", width=16, height = 8, bg="pink", command=lambda: press(0))
button_decimal = Button(buttons_frame, text=".", width=16, height = 8, bg="pink", command=lambda: press("."))

photo = PhotoImage(file = r"C:\Users\jinge\Downloads\coolgif.png")
image_button = Button(buttons_frame, image=photo, width=120, height= 130, command=play_song)




#grid for buttons
button1.grid(row=0, column=0, sticky="w")
button2.grid(row=0, column=1, sticky="w")
button3.grid(row=0, column=2, sticky="w")
button4.grid(row=1, column=0, sticky="w")
button5.grid(row=1, column=1, sticky="w")
button6.grid(row=1, column=2, sticky="w")
button7.grid(row=2, column=0, sticky="w")
button8.grid(row=2, column=1, sticky="w")
button9.grid(row=2, column=2, sticky="w")
button0.grid(row=3, column=0)
button_decimal.grid(row=3, column=1)
image_button.grid(row=3, column=2)

#operation buttons
plus_button = Button(operation_frame, text="+", width=15, height=11, bg="cyan", command=lambda: press("+"))
minus_button = Button(operation_frame, text="-", width=15, height=11, bg="cyan", command=lambda: press("-"))
multiply_button = Button(operation_frame, text="X", width=15, height=11, bg="cyan", command=lambda: press("*"))
divide_button = Button(operation_frame, text="÷", width=15, height=11, bg="cyan", command=lambda: press("/"))
enter_button = Button(operation_frame, text="ENTER", width=15, height=11, bg="cyan", command=equalpress)
clear_button = Button(operation_frame, text="CLEAR", width=15, height=11, bg="cyan", command=clear)

#grid for operations
plus_button.grid(row=0, column=0)
minus_button.grid(row=0, column=1)
multiply_button.grid(row=1, column=0)
divide_button.grid(row=1, column=1)
enter_button.grid(row=2, column=0)
clear_button.grid(row=2, column=1)





