# calculator using Tkinter

from tkinter import *

statement = ""

def press(num):
	global statement
	statement = statement + str(num)
	equation.set(statement)

def equalpress():
	try:
		global statement
		total = str(eval(statement))
		equation.set(total)

	except:
		equation.set(" error ")
		statement = ""



def clear():
	global statement
	statement = ""
	equation.set("")

# Driver code
if __name__ == "__main__":

	root = Tk()
	root.configure(background="#ccc")
	root.title("Calculator")

	icon_photo = PhotoImage(file='img/calc_icon.png')
	root.iconphoto(False, icon_photo)
	root.geometry("270x300")

	equation = StringVar()

	statement_field = Entry(root, textvariable=equation, justify=RIGHT, selectborderwidth=0, font='Courier 15 bold', state=DISABLED)
	statement_field.pack(pady=20, ipady=10, ipadx=5)

	button1 = Button(root, text=' 1 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(1), height=1, width=7)
	button1.place(anchor=NW, relx=0.1, rely=0.33)

	button2 = Button(root, text=' 2 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(2), height=1, width=7)
	button2.place(anchor=NW, relx=0.33, rely=0.33)

	button3 = Button(root, text=' 3 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(3), height=1, width=7)
	button3.place(anchor=NW, relx=0.56, rely=0.33)

	button4 = Button(root, text=' 4 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(4), height=1, width=7)
	button4.place(anchor=NW, relx=0.1, rely=0.43)

	button5 = Button(root, text=' 5 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(5), height=1, width=7)
	button5.place(anchor=NW, relx=0.33, rely=0.43)

	button6 = Button(root, text=' 6 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(6), height=1, width=7)
	button6.place(anchor=NW, relx=0.56, rely=0.43)

	button7 = Button(root, text=' 7 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(7), height=1, width=7)
	button7.place(anchor=NW, relx=0.1, rely=0.53)

	button8 = Button(root, text=' 8 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(8), height=1, width=7)
	button8.place(anchor=NW, relx=0.33, rely=0.53)

	button9 = Button(root, text=' 9 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(9), height=1, width=7)
	button9.place(anchor=NW, relx=0.56, rely=0.53)

	button0 = Button(root, text=' 0 ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press(0), height=1, width=7)
	button0.place(anchor=NW, relx=0.1, rely=0.63)

	clear = Button(root, text='Clear', fg='#fff', bg='#2B2D2F', bd=1,
				   command=clear, height=1, width=7)
	clear.place(anchor=NW, relx=0.33, rely=0.63)

	plus = Button(root, text=' + ', fg='#fff', bg='#2B2D2F', bd=1,
				command=lambda: press("+"), height=1, width=4)
	plus.place(anchor=NW, relx=0.79, rely=0.33)

	minus = Button(root, text=' - ', fg='#fff', bg='#2B2D2F', bd=1,
				command=lambda: press("-"), height=1, width=4)
	minus.place(anchor=NW, relx=0.79, rely=0.43)

	multiply = Button(root, text=' * ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press("*"), height=1, width=4)
	multiply.place(anchor=NW, relx=0.79, rely=0.53)

	divide = Button(root, text=' / ', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press("/"), height=1, width=4)
	divide.place(anchor=NW, relx=0.79, rely=0.63)

	equal = Button(root, text=' = ', fg='#fff', bg='#2B2D2F', bd=1,
				command=equalpress, height=1, width=7)
	equal.place(anchor=NW, relx=0.56, rely=0.63)

	Decimal= Button(root, text='.', fg='#fff', bg='#2B2D2F', bd=1,
					command=lambda: press('.'), height=1, width=7)
	Decimal.place(anchor=NW, relx=0.1, rely=0.73)


	root.mainloop()
