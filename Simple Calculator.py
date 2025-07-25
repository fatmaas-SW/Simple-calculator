from tkinter import *
root = Tk()
root.title("Simple calculator")
root.geometry("310x350")
root.resizable(width=False, height=False)
root.config(bg="black")
font1 = "Arial 20 bold"

def click(number):
    e.insert(END, number)

def clear():
    e.delete(0, END)

def equal():
    r = eval (e.get())
    clear()
    e.insert(END, r)

e = Entry(root, bd=10, width=18, font="Arial 22", bg="LightGray")
e.grid(row=0, column=0, columnspan=4, pady=(0, 5))

btn1 = Button(root, text="7", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(7))
btn1.grid(row=1, column=0)

btn2 = Button(root, text="8", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(8))
btn2.grid(row=1, column=1)

btn3 = Button(root, text="6", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(6))
btn3.grid(row=2, column=2)

btn4 = Button(root, text="4", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(4))
btn4.grid(row=2, column=0)

btn5 = Button(root, text="5", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(5))
btn5.grid(row=2, column=1)

btn6 = Button(root, text="3", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(3))
btn6.grid(row=3, column=2)

btn7 = Button(root, text="2", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(2))
btn7.grid(row=3, column=1)

btn8 = Button(root, text="1", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(1))
btn8.grid(row=3, column=0)

btn9 = Button(root, text="0", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(0))
btn9.grid(row=4, column=0)

btn10 = Button(root, text="9", font=font1, bg="grey", bd=10, height=1, width=3, command=lambda : click(9))
btn10.grid(row=1, column=2)

btn11 = Button(root, text=" C ", font=font1, bg="red", bd=10, height=1, width=3, command=clear)
btn11.grid(row=4, column=1)

btn12 = Button(root, text=" = ", font=font1, bg="yellow", bd=10, height=1, width=3, command=equal)
btn12.grid(row=4, column=2)

btn13 = Button(root, text=" + ", font=font1, bg="green", bd=10, height=1, width=3, command=lambda : click(" +"))
btn13.grid(row=1, column=3)

btn14 = Button(root, text=" - ", font=font1, bg="green", bd=10, height=1, width=3, command=lambda : click(" - "))
btn14.grid(row=2, column=3)

btn15 = Button(root, text=" x ", font=font1, bg="green", bd=10, height=1, width=3, command=lambda : click(" * "))
btn15.grid(row=3, column=3)

btn16 = Button(root, text=" ÷ ", font=font1, bg="green", bd=10, height=1, width=3, command=lambda : click(" / " ))
btn16.grid(row=4, column=3)

root.mainloop()