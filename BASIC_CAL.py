from tkinter import *
from PIL import Image, ImageTk
from math import*
root=Tk()
root.title("Simple Calculator")
root.iconbitmap("img/app_pic.ico")
root.config(bg="#5B5A5E")
def button_equal():
     second_number=e.get()
     e.delete(0,END)
     if math=="addition":
      second_number=float(second_number)
      resluts=str(second_number+f_number)
      e.insert(0,resluts)
     elif math=="Subtraction":
      second_number=float(second_number)
      resluts=str(float(f_number-second_number))
      e.insert(0,resluts)
     elif math=="Multiplication":
       second_number=float(second_number)
       resluts=str(float(f_number)*second_number)
       e.insert(0,resluts)
     elif math=="Division":
       second_number=float(second_number)
       resluts=str(float(f_number)/second_number)
       e.insert(0,resluts)    
     
def button_click(number):
  current=e.get()
  e.delete(0,END)
  e.insert(0,str(current)+str(number))
 
def button_clear():
    e.delete(0,END) 
def button_add():
  global f_number
  global math
  first_number=e.get()
  math="addition"
  f_number=float(first_number)
  e.delete(0,END)
def button_sub():
    global f_number
    global math
    first_number = e.get()
    if first_number == "":#This if statement is to allow a minus sign (allow entering -(number))
        e.insert(0, "-")
    else:
        math = "Subtraction"
        f_number = float(first_number)
        e.delete(0, END)
def button_mul():
  global f_number
  global math
  first_number=e.get()
  math="Multiplication"
  f_number=float(first_number)
  e.delete(0,END)
def button_div():
    global f_number
    global math
    first_number=e.get()
    math="Division"
    f_number=float(first_number)
    e.delete(0,END)
def button_sqrt():
    current = e.get()
    try:
        result = sqrt(float(current))
        e.delete(0, END)
        e.insert(0, str(result))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")
def button_square():
    current=e.get()
    try:
       result=float(current)*float(current)
       e.delete(0, END)
       e.insert(0, str(result))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")
def button_fact():
    current=e.get()
    try:
      result=factorial(int(current))
      e.delete(0, END)
      e.insert(0, str(result))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")
def button_percentage():
    current = e.get()
    try:
        result = float(current) / 100
        e.delete(0, END)
        e.insert(0, str(result))
    except ValueError:
        e.delete(0, END)
        e.insert(0, "Error")

# creating an entry widget 
e= Entry(root, font=("Arial", 20), bd=5, insertwidth=2, width=33, borderwidth=3)
e.grid(row=0, column=0, columnspan=4)

#creating the buttons
btn1 = Button(root, text="1", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(1))
btn2 = Button(root, text="2", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(2))
btn3 = Button(root, text="3", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(3))
btn4 = Button(root, text="4", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(4))
btn5 = Button(root, text="5", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(5))
btn6 = Button(root, text="6", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(6))
btn7 = Button(root, text="7", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(7))
btn8 = Button(root, text="8", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(8))
btn9 = Button(root, text="9", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(9))
btn0 = Button(root, text="0", bg="#4CAF50", fg="white", padx=55, pady=30, command=lambda: button_click(0))
#operations buttons
equal_btn = Button(root, text="=", bg="#FF9800", fg="white", padx=54, pady=30, command=button_equal)
clr_btn = Button(root, text="AC", bg="#FF9800", fg="white", padx=50, pady=30, command=button_clear)
addition_btn = Button(root, text="+", bg="#FF9800", fg="white", padx=53, pady=30, command=button_add)
subtraction_btn = Button(root, text="-", bg="#FF9800", fg="white", padx=55, pady=30, command=button_sub)
multiplication_btn = Button(root, text="X", bg="#FF9800", fg="white", padx=54, pady=30, command=button_mul)
division_btn = Button(root, text="/", bg="#FF9800", fg="white", padx=55, pady=30, command=button_div)
back_space_btn = Button(root, text="<", bg="#FF9800", fg="white", padx=55, pady=30, command=button_div)
sqrt_btn = Button(root, text="\u221A", bg="#FF9800", fg="white", padx=55, pady=30, command=button_sqrt)
square_btn = Button(root, text="X\u00B2", bg="#FF9800", fg="white", padx=52, pady=30, command=button_square)
factorial_btn = Button(root, text="X!", bg="#FF9800", fg="white", padx=52, pady=30, command=button_fact)
percentage_btn = Button(root, text="%", bg="#FF9800", fg="white", padx=52, pady=30, command=button_percentage)
#putting the buttons on the screen
btn1.grid(row=1,column=0,pady=2)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=3,column=0,pady=2)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btn0.grid(row=5,column=1)
equal_btn.grid(row=5,column=2)
clr_btn.grid(row=5,column=0)
addition_btn.grid(row=1,column=3)
subtraction_btn.grid(row=2,column=3)
multiplication_btn.grid(row=3,column=3)
division_btn.grid(row=5,column=3)
sqrt_btn.grid(row=6, column=0)
square_btn.grid(row=6, column=1)
factorial_btn.grid(row=6, column=2)
percentage_btn.grid(row=6, column=3)


root.mainloop()

