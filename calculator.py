from tkinter import *


first_input = 0
second_input = 0
action = "none"


def backspace():
    input2.delete(len(input2.get())-1, END)

def clear():
    input2.delete(0,END)

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

def to_the_power():
    global first_input
    global action
    first_input = int(input2.get() or 0)
    action = "exponent"
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
    elif action == "exponent":
        input2.insert(0,first_input ** second_input)


def insert_one():
    input2.insert(END,1)

def insert_two():
    input2.insert(END,2)

def insert_three():
    input2.insert(END,3)

def insert_four():
    input2.insert(END,4)

def insert_five():
    input2.insert(END,5)

def insert_six():
    input2.insert(END,6)

def insert_seven():
    input2.insert(END,7)

def insert_eight():
    input2.insert(END,8)

def insert_nine():
    input2.insert(END,9)

def insert_zero():
    input2.insert(END,0)

def insert_period():
    input2.insert(END,".")


    
    

    
    

# addition(input("enter a number: ") or 0, input("enter another number: ") or 0)
window = Tk()
# window.geometry("500x500")
window.title("Calculator")
window.config(background="black")



input2 = Entry(window, 
            font=("Comic Sans", 15), justify=RIGHT)
input2.grid(row=0, column=0, columnspan=5)


# input1 = Entry(window, 
#             font=("Comic Sans", 10))
# input1.grid(row=0, column=1)

bk = Button(window, 
                text = "BK", 
                command=backspace, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=1, column=0, sticky='nesw')

ce = Button(window, 
                text = "CE", 
                command=clear, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=1, column=1, sticky='nesw')

plus = Button(window, 
                text = "+", 
                command=addition, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=2, column=0, sticky='nesw')


minus = Button(window, 
                text = "-", 
                command=subtraction, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=2, column=1,sticky='nesw')

times = Button(window, 
                text = "x", 
                command=multiplication, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=3,column=0,sticky='nesw')

divide = Button(window, 
                text = "÷", 
                command=division, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=3, column=1,sticky='nesw')

equal = Button(window, 
                text = "=", 
                command=perform_action, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=4, column=0,columnspan=2 ,sticky='nesw')

one = Button(window, 
                text = "1", 
                command=insert_one, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=1, column=2,sticky='nesw')

two = Button(window, 
                text = "2", 
                command=insert_two, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=1, column=3,sticky='nesw')

three = Button(window, 
                text = "3", 
                command=insert_three, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=1, column=4,sticky='nesw')
            
four = Button(window, 
                text = "4", 
                command=insert_four, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=2, column=2,sticky='nesw')

five = Button(window, 
                text = "5", 
                command=insert_five, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=2, column=3,sticky='nesw')

six = Button(window, 
                text = "6", 
                command=insert_six, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=2, column=4,sticky='nesw')

seven = Button(window, 
                text = "7", 
                command=insert_seven, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=3, column=2,sticky='nesw')
        
eight = Button(window, 
                text = "8", 
                command=insert_eight, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=3, column=3,sticky='nesw')

nine = Button(window, 
                text = "9", 
                command=insert_nine, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=3, column=4,sticky='nesw')

zero= Button(window, 
                text = "0", 
                command=insert_zero, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=4, column=3,sticky='nesw')

period = Button(window, 
                text = ".", 
                command=insert_period, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=4, column=4,sticky='nesw')

exponent = Button(window, 
                text = "^", 
                command=to_the_power, 
                font=("Comic Sans", 12), 
                fg="white",
                bg="gray",
                activebackground="gray",
                activeforeground="white").grid(row=4, column=2,sticky='nesw')
window.mainloop()