from tkinter import *
from tkinter.ttk import *
from math import *

root = Tk()
root.resizable(width = 0, height = 0)
root.title("MibiCalc")
def parentheseopen():
    #
    print("(")
    calcs.insert(END, "(")
def parentheseclose():
    #
    print(")")
    calcs.insert(END, ")")
def one():
    #
    print("1")
    calcs.insert(END, "1")
def two():
    #
    print("2")
    calcs.insert(END, "2")
def three():
    #
    print("3")
    calcs.insert(END, "3")
def four():
    #
    print("4")
    calcs.insert(END, "4")
def five():
    #
    print("5")
    calcs.insert(END, "5")
def six():
    #
    print("6")
    calcs.insert(END, "6")
def seven():
    #
    print("7")
    calcs.insert(END, "7")
def eight():
    #
    print("8")
    calcs.insert(END, "8")
def nine():
    #
    print("9")
    calcs.insert(END, "9")
def zero():
    #
    print("0")
    calcs.insert(END, "0")
def clear():
    #
    print("AC")
    calcs.delete(0, END)
#---
def div():
    #
    print("/")
    calcs.insert(END, "/")
def mod():
    #
    print("%")
    calcs.insert(END, "%")
def multi():
    #
    print("*")
    calcs.insert(END, "*")
def minu():
    #
    print("-")
    calcs.insert(END, "-")
def addnum():
    #
    print("+")
    calcs.insert(END, "+")
def execute():
    calc = calcs.get()
    try:
        calc = eval(calc)
        calcs.delete(0, END)
        calcs.insert(END, calc)
    except:
        calcs.delete(0, END)
        calcs.insert(END, "ERROR")

#entry
calcs = Entry(root, width = 10)
calcs.grid(column = 2, row = 1)
#buttons
#(
parentheseopenb = Button(root, text="(", command=parentheseopen)
parentheseopenb.grid(column=1, row=5)
#)
parenthesecloseb = Button(root, text=")", command=parentheseclose)
parenthesecloseb.grid(column=3, row=5)
#1
oneb = Button(root, text="1", command=one)
oneb.grid(column=1, row=2)
#2
twob = Button(root, text="2", command=two)
twob.grid(column=2, row=2)
#3
threeb = Button(root, text="3", command=three)
threeb.grid(column=3, row=2)
#4
fourb = Button(root, text="4", command=four)
fourb.grid(column=1, row=3)
#5
fiveb = Button(root, text="5", command=five)
fiveb.grid(column=2, row=3)
#6
sixb = Button(root, text="6", command=six)
sixb.grid(column=3, row=3)
#7
sevenb = Button(root, text="7", command=seven)
sevenb.grid(column=1, row=4)
#8
eightb = Button(root, text="8", command=eight)
eightb.grid(column=2, row=4)
#9
nineb = Button(root, text="9", command=nine)
nineb.grid(column=3, row=4)
#0
zerob = Button(root, text="0", command=zero)
zerob.grid(column=2, row=5)
#+
plusb = Button(root, text="+", command=addnum)
plusb.grid(column=4, row=2)
#-
minusb = Button(root, text="-", command=minu)
minusb.grid(column=4, row=3)
#*
multiplyb = Button(root, text="*", command=multi)
multiplyb.grid(column=4, row=4)
#/
divb = Button(root, text="/", command=div)
divb.grid(column=4, row=5)
#%
modb = Button(root, text="mod", command=mod)
modb.grid(column=4, row=1)
#AC
clearb = Button(root, text="AC", command=clear)
clearb.grid(column=3, row=1)
#EXE button
clearb = Button(root, text="EXE", command=execute)
clearb.grid(column=1, row=1)

root.mainloop()