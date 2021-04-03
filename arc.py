from tkinter import ttk
from tkinter import Tk
from ttkthemes import ThemedTk
# from tkinter import ttk
# from tkinter.ttk import *
from math import *

main = ThemedTk(theme="arc")
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
    end = len(calcs.get())
    calcs.insert(end, "(")
def parentheseclose():
    #
    print(")")
    end = len(calcs.get())
    calcs.insert(end, ")")
def one():
    #
    print("1")
    end = len(calcs.get())
    calcs.insert(end, "1")
def two():
    #
    print("2")
    end = len(calcs.get())
    calcs.insert(end, "2")
def three():
    #
    print("3")
    end = len(calcs.get())
    calcs.insert(end, "3")
def four():
    #
    print("4")
    end = len(calcs.get())
    calcs.insert(end, "4")
def five():
    #
    print("5")
    end = len(calcs.get())
    calcs.insert(end, "5")
def six():
    #
    print("6")
    end = len(calcs.get())
    calcs.insert(end, "6")
def seven():
    #
    print("7")
    end = len(calcs.get())
    calcs.insert(end, "7")
def eight():
    #
    print("8")
    end = len(calcs.get())
    calcs.insert(end, "8")
def nine():
    #
    print("9")
    end = len(calcs.get())
    calcs.insert(end, "9")
def zero():
    #
    print("0")
    end = len(calcs.get())
    calcs.insert(end, "0")
def clear():
    #
    print("AC")
    end = len(calcs.get())
    calcs.delete(0, end)
def delchar():
    calc_todel = calcs.get()
    calc = calc_todel[:-1]
    #---replace the text of the entry---
    #print(calc)
    # calcs.config(text=calc)
    end = len(calcs.get())
    calcs.delete(0, end)
    calcs.insert(0, calc)
    #-----------------------------------
#---
def div():
    #
    print("/")
    end = len(calcs.get())
    calcs.insert(end, "/")
def mod():
    #
    print("%")
    end = len(calcs.get())
    calcs.insert(end, "%")
def multi():
    #
    print("*")
    end = len(calcs.get())
    calcs.insert(end, "*")
def minu():
    #
    print("-")
    end = len(calcs.get())
    calcs.insert(end, "-")
def addnum():
    #
    print("+")
    end = len(calcs.get())
    calcs.insert(end, "+")
def execute():
    calc = calcs.get()
    try:
        calc = eval(calc)
        end = len(calcs.get())
        calcs.delete(0, end)
        calcs.insert(end, calc)
    except:
        end = len(calcs.get())
        calcs.delete(0, end)
        calcs.insert(end, "ERROR")

#entry
calcs = ttk.Entry(main, width = 10)
calcs.grid(column = 1, row = 0, sticky='nesw', columnspan=4)
#buttons
#(
parentheseopenb = ttk.Button(main, text="(", command=parentheseopen)
parentheseopenb.grid(column=1, row=5, sticky='nesw')
#)
parenthesecloseb = ttk.Button(main, text=")", command=parentheseclose)
parenthesecloseb.grid(column=3, row=5, sticky='nesw')
#1
oneb = ttk.Button(main, text="1", command=one)
oneb.grid(column=1, row=2, sticky='nesw')
#2
twob = ttk.Button(main, text="2", command=two)
twob.grid(column=2, row=2, sticky='nesw')
#3
threeb = ttk.Button(main, text="3", command=three)
threeb.grid(column=3, row=2, sticky='nesw')
#4
fourb = ttk.Button(main, text="4", command=four)
fourb.grid(column=1, row=3, sticky='nesw')
#5
fiveb = ttk.Button(main, text="5", command=five)
fiveb.grid(column=2, row=3, sticky='nesw')
#6
sixb = ttk.Button(main, text="6", command=six)
sixb.grid(column=3, row=3, sticky='nesw')
#7
sevenb = ttk.Button(main, text="7", command=seven)
sevenb.grid(column=1, row=4, sticky='nesw')
#8
eightb = ttk.Button(main, text="8", command=eight)
eightb.grid(column=2, row=4, sticky='nesw')
#9
nineb = ttk.Button(main, text="9", command=nine)
nineb.grid(column=3, row=4, sticky='nesw')
#0
zerob = ttk.Button(main, text="0", command=zero)
zerob.grid(column=2, row=5, sticky='nesw')
#+
plusb = ttk.Button(main, text="+", command=addnum)
plusb.grid(column=4, row=2, sticky='nesw')
#-
minusb = ttk.Button(main, text="-", command=minu)
minusb.grid(column=4, row=3, sticky='nesw')
#*
multiplyb = ttk.Button(main, text="*", command=multi)
multiplyb.grid(column=4, row=4, sticky='nesw')
#/
divb = ttk.Button(main, text="/", command=div)
divb.grid(column=4, row=5, sticky='nesw')
#%
modb = ttk.Button(main, text="mod", command=mod)
modb.grid(column=4, row=1, sticky='nesw')
#DEL
clearb = ttk.Button(main, text="DEL", command=delchar)
clearb.grid(column=3, row=1, sticky='nesw')
#AC
clearb = ttk.Button(main, text="AC", command=clear)
clearb.grid(column=2, row=1, sticky='nesw')
#EXE button
clearb = ttk.Button(main, text="EXE", command=execute)
clearb.grid(column=1, row=1, sticky='nesw')

main.mainloop()