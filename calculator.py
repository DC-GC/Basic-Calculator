from tkinter import *


first_input = 0
second_input = 0
action = "none"


def addition():
    global first_input
    global action
    first_input = int(input2.get() or 0)
    action = "addition"
    input2.delete(0, END)
    
    
    
def subtraction():
    global first_input
    global action
    first_input = int(input2.get() or 0)
    action = "subtraction"
    input2.delete(0, END)

def multiplication():
    global first_input
    global action
    first_input = int(input2.get() or 0)
    action = "multiplication"
    input2.delete(0, END)

def division():
    global first_input
    global action
    first_input = int(input2.get() or 0)
    action = "division"
    input2.delete(0, END)

def perform_action():
    global action
    global second_input
    second_input = int(input2.get() or 0)
    input2.delete(0, END)
    if action == "addition":
        input2.insert(0,first_input + second_input)
    elif action == "subtraction":
        input2.insert(0,first_input - second_input)
    elif action == "multiplication":
        input2.insert(0,first_input * second_input)
    elif action == "division":
        input2.insert(0,first_input / second_input)
    
    

    
    

# addition(input("enter a number: ") or 0, input("enter another number: ") or 0)
window = Tk()
# window.geometry("500x500")
window.title("Calculator")
window.config(background="black")



input2 = Entry(window, 
            font=("Comic Sans", 15))
input2.grid(row=0, column=0, columnspan=2)


# input1 = Entry(window, 
#             font=("Comic Sans", 10))
# input1.grid(row=0, column=1)

plus = Button(window, 
                text = "+", 
                command=addition, 
                font=("Comic Sans", 12), 
                fg="blue",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=1, column=0, sticky='nesw')


minus = Button(window, 
                text = "-", 
                command=subtraction, 
                font=("Comic Sans", 12), 
                fg="blue",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=1, column=1,sticky='nesw')

times = Button(window, 
                text = "x", 
                command=multiplication, 
                font=("Comic Sans", 12), 
                fg="blue",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=2,column=0,sticky='nesw')

divide = Button(window, 
                text = "÷", 
                command=division, 
                font=("Comic Sans", 12), 
                fg="blue",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=2, column=1,sticky='nesw')

equal = Button(window, 
                text = "=", 
                command=perform_action, 
                font=("Comic Sans", 15), 
                fg="blue",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=3, column=0,columnspan=2 ,sticky='nesw')

window.mainloop()