from tkinter import *


def addition(a=0,b=0):
    print(int(input2.get() or 0)+int(int(input1.get() or 0)))
    # print(type(input2.get()))
    
def subtraction(a=0, b=0):
    print(int(input2.get() or 0)-int(int(input1.get() or 0)))

def multiplication(a=0, b=0):
    print(int(input2.get() or 0)*int(int(input1.get() or 0)))

def division(a=0, b=0):
    print(int(input2.get() or 0)/int(int(input1.get() or 1)))

def clear():
    input2.delete(0, END)
    input1.delete(0, END)

# addition(input("enter a number: ") or 0, input("enter another number: ") or 0)
window = Tk()
# window.geometry("500x500")
window.title("GUI :)")
window.config(background="black")



input2 = Entry(window, 
            font=("Comic Sans", 10))
input2.grid(row=0, column=0)


input1 = Entry(window, 
            font=("Comic Sans", 10))
input1.grid(row=0, column=1)

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
                command=clear, 
                font=("Comic Sans", 15), 
                fg="blue",
                bg="black",
                activebackground="black",
                activeforeground="white").grid(row=3, column=0,columnspan=2 ,sticky='nesw')

window.mainloop()