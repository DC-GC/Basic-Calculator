from tkinter import *
first_input = 0
action = "none"
window = Tk()

def backspace():
    entry.delete()
def clear():
    entry.remove_all()
def addition():
    global first_input
    global action
    first_input = float(entry.get_value() or 0)
    action = "addition"
    entry.remove_all()

def subtraction():
    global first_input
    global action
    first_input = float(entry.get_value() or 0)
    action = "subtraction"
    entry.remove_all()

def multiplication():
    global first_input
    global action
    first_input = float(entry.get_value() or 0)
    action = "multiplication"
    entry.remove_all()

def division():
    global first_input
    global action
    first_input = float(entry.get_value() or 0)
    action = "division"
    entry.remove_all()


def perform_action():
    global action
    global first_input
    second_input = float(entry.get_value() or 0)
    const = 0
    entry.remove_all()
    if action == "addition":
        entry.change_value(first_input+second_input)
        action = "none"
    elif action == "subtraction":
        entry.change_value(first_input-second_input)
        action = "none"
    elif action == "multiplication":
        entry.change_value(first_input*second_input)
        action = "none"
    elif action == "division":
        entry.change_value(first_input/second_input)
        action = "none"
    elif action == "exponent":
        entry.change_value(first_input**second_input)
        action = "none"

def to_the_power():
    global first_input
    global action
    first_input = float(entry.get_value() or 0)
    action = "exponent"
    entry.remove_all()  

def insert_one():
    entry.change_value(1)
def insert_two():
    entry.change_value(2)
def insert_three():
    entry.change_value(3)
def insert_four():
    entry.change_value(4)
def insert_five():
    entry.change_value(5)
def insert_six():
    entry.change_value(6)
def insert_seven():
    entry.change_value(7)
def insert_eight():
    entry.change_value(8)
def insert_nine():
    entry.change_value(9)
def insert_zero():
    entry.change_value(0)
def insert_period():
    entry.change_value(".")


    

class button:
    def __init__(self, text, row, column,columnspan, function):
        self.main =  Button(window, 
                text = text,
                command=function,  
                font=("Comic Sans", 12), 
                fg="white",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=row, column=column, columnspan=columnspan,sticky='nesw')


class entrybox:
    def __init__(self, row, column, columnspan):
        self.main = Entry(window, 
                        font=("Comic Sans", 15), justify=RIGHT)
        self.main.grid(row=row, column=column, columnspan=columnspan)
    def get_value(self):
        return self.main.get()
    def change_value(self,value):
        self.main.insert(END,value)
    def delete(self):
        self.main.delete(len(self.main.get())-1, END)
    def remove_all(self):
        self.main.delete(0,END)
    



        
bk = button("BK", 1,0,1,backspace)
ce = button("CE", 1,1,1,clear)
add = button("+", 2,0,1,addition)
sub = button("-", 2,1,1,subtraction)
mul = button("x", 3,0,1,multiplication)
div = button("÷", 3,1,1,division)
equal = button("=", 4,0,2,perform_action)
one = button("1", 1,2,1,insert_one)
two = button("2", 1,3,1,insert_two)
three = button("3", 1,4,1,insert_three)
four = button("4", 2,2,1,insert_four)
five = button("5", 2,3,1,insert_five)
six = button("6", 2,4,1,insert_six)
seven = button("7", 3,2,1,insert_seven)
eight = button("8", 3,3,1,insert_eight)
nine = button("9", 3,4,1,insert_nine)
exponent = button("^", 4,2,1,to_the_power)
zero = button("0", 4,3,1,insert_zero)
period = button(".", 4,4,1,insert_period)



entry = entrybox(0,0,5)




window.mainloop()