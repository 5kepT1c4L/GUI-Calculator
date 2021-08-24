from tkinter import *

#TK window setup
tk = Tk()
tk.title("Calculator")
tk.geometry('600x600')
tk.configure(bg="pink")
equation = "yes"

#Frame for the equation input
frame1 = Frame(tk, highlightbackground="blue", highlightthickness=1,width=600, height=80, bd= 0)
frame1.pack()
frame1.pack_propagate(False)

equation_area = Label(frame1, text="Equation here", font=("Times", 50)) #text needs to be edited to equation variable
equation_area.pack()

#frame for the buttons
buttons_frame = Frame(tk, highlightbackground="blue", highlightthickness=1, width=360, height=520, bd=0)
buttons_frame.pack(side="left")

#frame for the operation signs
operation_frame = Frame(tk, highlightbackground="blue", highlightthickness=1, width=240, height=520, bd=0)
operation_frame.pack(side="right")

#buttons 1-9
button1 = Button(buttons_frame, text="1", width=16, height = 7)
button2 = Button(buttons_frame, text="2", width=16, height = 7)
button3 = Button(buttons_frame, text="3", width=16, height = 7)
button4 = Button(buttons_frame, text="4", width=16, height = 7)
button5 = Button(buttons_frame, text="5", width=16, height = 7)
button6 = Button(buttons_frame, text="6", width=16, height = 7)
button7 = Button(buttons_frame, text="7", width=16, height = 7)
button8 = Button(buttons_frame, text="8", width=16, height = 7)
button9 = Button(buttons_frame, text="9", width=16, height = 7)
button0 = Button(buttons_frame, text="0", width=16, height = 7)




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





