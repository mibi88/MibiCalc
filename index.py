from tkinter import *
# from tkinter import ttk
# from tkinter.ttk import *
from math import *

main = Tk()
# main.resizable(width = 0, height = 0)
main.title("MibiCalc")
main.rowconfigure(0, weight=1)
main.rowconfigure(1, weight=1)
main.columnconfigure(1, weight=1)
main.rowconfigure(2, weight=1)
main.columnconfigure(2, weight=1)
main.rowconfigure(3, weight=1)
main.columnconfigure(3, weight=1)
main.rowconfigure(4, weight=1)
main.columnconfigure(4, weight=1)
main.rowconfigure(5, weight=1)
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
def delchar():
    calc_todel = calcs.get()
    calc = calc_todel[:-1]
    #---replace the text of the entry---
    #print(calc)
    # calcs.config(text=calc)
    calcs.delete(0, END)
    calcs.insert(0, calc)
    #-----------------------------------
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
calcs = Entry(main, width = 10)
calcs.grid(column = 1, row = 0, sticky='nesw', columnspan=4)
#buttons
#(
parentheseopenb = Button(main, text="(", command=parentheseopen)
parentheseopenb.grid(column=1, row=5, sticky='nesw')
#)
parenthesecloseb = Button(main, text=")", command=parentheseclose)
parenthesecloseb.grid(column=3, row=5, sticky='nesw')
#1
oneb = Button(main, text="1", command=one)
oneb.grid(column=1, row=2, sticky='nesw')
#2
twob = Button(main, text="2", command=two)
twob.grid(column=2, row=2, sticky='nesw')
#3
threeb = Button(main, text="3", command=three)
threeb.grid(column=3, row=2, sticky='nesw')
#4
fourb = Button(main, text="4", command=four)
fourb.grid(column=1, row=3, sticky='nesw')
#5
fiveb = Button(main, text="5", command=five)
fiveb.grid(column=2, row=3, sticky='nesw')
#6
sixb = Button(main, text="6", command=six)
sixb.grid(column=3, row=3, sticky='nesw')
#7
sevenb = Button(main, text="7", command=seven)
sevenb.grid(column=1, row=4, sticky='nesw')
#8
eightb = Button(main, text="8", command=eight)
eightb.grid(column=2, row=4, sticky='nesw')
#9
nineb = Button(main, text="9", command=nine)
nineb.grid(column=3, row=4, sticky='nesw')
#0
zerob = Button(main, text="0", command=zero)
zerob.grid(column=2, row=5, sticky='nesw')
#+
plusb = Button(main, text="+", command=addnum)
plusb.grid(column=4, row=2, sticky='nesw')
#-
minusb = Button(main, text="-", command=minu)
minusb.grid(column=4, row=3, sticky='nesw')
#*
multiplyb = Button(main, text="*", command=multi)
multiplyb.grid(column=4, row=4, sticky='nesw')
#/
divb = Button(main, text="/", command=div)
divb.grid(column=4, row=5, sticky='nesw')
#%
modb = Button(main, text="mod", command=mod)
modb.grid(column=4, row=1, sticky='nesw')
#DEL
clearb = Button(main, text="DEL", background = "#fadd02", activebackground = "#f7e979", command=delchar)
clearb.grid(column=3, row=1, sticky='nesw')
#AC
clearb = Button(main, text="AC", background = "#fadd02", activebackground = "#f7e979", command=clear)
clearb.grid(column=2, row=1, sticky='nesw')
#EXE button
clearb = Button(main, text="EXE", background = "#fadd02", activebackground = "#f7e979", command=execute)
clearb.grid(column=1, row=1, sticky='nesw')

main.mainloop()