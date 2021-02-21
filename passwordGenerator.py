import random

from tkinter import *
from tkinter import ttk


listCode = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k",
            "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v",
            "W", "w", "X", "x", "Y", "y", "Z", "z", " ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#",
            "$", "%", "^", "&", "*", "(" ,")", "'", '"', "-", "_", "+", "=", "[", "]", "{", "}", ":", ";", ",", ".", "<", ">", "?", "/", "~", "`"]

def generate(lenth):
    password = ''
    for i in range(lenth):
        code = random.randint(0, 92)
        password += listCode[code]
    return password

def typePsd(): #generats password
    txtPassword.config(state = "normal")
    txtPassword.delete('1.0', END)
    txtPassword.insert(INSERT, str(generate(scale.get()))) #set string
    txtPassword.config(state = "disabled")

window = Tk()
window.title("Password Generator") #title
window.geometry("280x150")



lbl1 = Label(window, text= 'Password generator', font= "Consolas 10 bold") #text

lbl2 = Label(window, text = "change lenth of password:")

scale = Scale(window, from_ = 4, to = 20, orient=HORIZONTAL) #set password lenth
scale.set(8)

btnGenerate = Button(window, text ="Generate", bg="lightGray", command = typePsd) #button (activates generation

txtPassword = Text(window, bg = "lightGray", bd="3", height = "1", width = "20")
txtPassword.config(state = "disabled")

lbl1.pack()
lbl2.pack()
scale.pack()
btnGenerate.pack()
txtPassword.pack(pady = 5)
window.mainloop()
