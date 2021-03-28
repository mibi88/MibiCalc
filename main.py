from tkinter import *
from tkinter.ttk import *


class InsertNumber():
	def one():
		equation_entry.insert(END, "1")

	def two():
		equation_entry.insert(END, "2")

	def three():
		equation_entry.insert(END, "3")

	def four():
		equation_entry.insert(END, "4")

	def five():
		equation_entry.insert(END, "5")

	def six():
		equation_entry.insert(END, "6")

	def seven():
		equation_entry.insert(END, "7")

	def eight():
		equation_entry.insert(END, "8")

	def nine():
		equation_entry.insert(END, "9")

	def zero():
		equation_entry.insert(END, "0")


class InsertMathOperators():
	def open_parenthesis():
		equation_entry.insert(END, "(")

	def close_parenthesis():
		equation_entry.insert(END, ")")
	
	def division():
		equation_entry.insert(END, "/")

	def multiplication():
		equation_entry.insert(END, "*")

	def subtraction():
		equation_entry.insert(END, "-")

	def addition():
		equation_entry.insert(END, "+")
	
	def dot():
		equation_entry.insert(END, '.')
	
	def mod():
		equation_entry.insert(END, ' mod ')
	
	def backspace():
		equation_entry.delete(len(equation_entry.get())-1)


class Calculate:
	def AC():
		equation_entry.delete(0, END)

	def equal():
		total = equation_entry.get()
		
		try:
			if 'mod' in total:
				total = total.replace('mod', '%')
				total = eval(total)
				equation_entry.delete(0, END)
				equation_entry.insert(END, total)
			
			else:
				total = eval(total)
				equation_entry.delete(0, END)
				equation_entry.insert(END, total)
		
		
		except ZeroDivisionError:
			equation_entry.delete(0, END)
			equation_entry.insert(END, "Imposible to be divided")
		
		except:
			equation_entry.delete(0, END)
			equation_entry.insert(END, "Error")



root = Tk()
root.configure(background='#F6F5F4')
root.geometry('380x240')
root.title("MibiCalc")


equation_entry = Entry(root, font='Calibri 20')
equation_entry.place(x=5, y=5, width=370, height=50)


# Buttons style
equal_button_style = Style()
equal_button_style.configure('EB.TButton', foreground='#FFFFFF', background='#3584E4')

AC_button_style = Style()
AC_button_style.configure('AC.TButton', foreground='#FFFFFF', background='#FF6868')

default_button_style = Style()
default_button_style.configure('TButton', foreground='#000000', background='#F6F5F4')


# Number Buttons
one_button = Button(root, text="1", command=InsertNumber.one)
one_button.place(x=5, y=60, width=55, height=40)

two_button = Button(root, text="2", command=InsertNumber.two)
two_button.place(x=65, y=60, width=55, height=40)

three_button = Button(root, text="3", command=InsertNumber.three)
three_button.place(x=125, y=60, width=55, height=40)

four_button = Button(root, text="4", command=InsertNumber.four)
four_button.place(x=5, y=105, width=55, height=40)

five_button = Button(root, text="5", command=InsertNumber.five)
five_button.place(x=65, y=105, width=55, height=40)

six_button = Button(root, text="6", command=InsertNumber.six)
six_button.place(x=125, y=105, width=55, height=40)

seven_button = Button(root, text="7", command=InsertNumber.seven)
seven_button.place(x=5, y=150, width=55, height=40)

eight_button = Button(root, text="8", command=InsertNumber.eight)
eight_button.place(x=65, y=150, width=55, height=40)

nine_button = Button(root, text="9", command=InsertNumber.nine)
nine_button.place(x=125, y=150, width=55, height=40)

zero_button = Button(root, text="0", command=InsertNumber.zero)
zero_button.place(x=5, y=195, width=55, height=40 )


# Operator Buttons
backspace_button = Button(root, text='←', command=InsertMathOperators.backspace)
backspace_button.place(x=200, y=60, width=115, height=40)

open_parenthesis_button = Button(root, text="(", command=InsertMathOperators.open_parenthesis)
open_parenthesis_button.place(x=200, y=105, width=55, height=40)

close_parenthesis_button = Button(root, text=")", command=InsertMathOperators.close_parenthesis)
close_parenthesis_button.place(x=260, y=105, width=55, height=40)

plus_button = Button(root, text="+", command=InsertMathOperators.addition)
plus_button.place(x=200, y=150, width=55, height=40)

minus_button = Button(root, text="-", command=InsertMathOperators.subtraction)
minus_button.place(x=260, y=150, width=55, height=40)

multiply_button = Button(root, text="×", command=InsertMathOperators.multiplication)
multiply_button.place(x=200, y=195, width=55, height=40)

divide_button = Button(root, text="÷", command=InsertMathOperators.division)
divide_button.place(x=260, y=195, width=55, height=40)

dot_button = Button(root, text='.', command=InsertMathOperators.dot)
dot_button.place(x=65, y=195, width=55, height=40)

mod_button = Button(root, text='mod', command=InsertMathOperators.mod)
mod_button.place(x=125, y=195, width=55, height=40)


# Calculate Buttons
AC_button = Button(root, text="AC", command=Calculate.AC, style='AC.TButton')
AC_button.place(x=320, y=60, width=55, height=85)

equal_button = Button(root, text="=", command=Calculate.equal, style='EB.TButton')
equal_button.place(x=320, y=150, width=55, height=85)

	
root.mainloop()
