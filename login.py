from tkinter import *
from tkinter import messagebox

lgn = Tk()
lgn.title("Login")  # for title of th dialogue box
lgn.geometry("650x400")  # size of the dialogue box
lgn.config(bg="grey")  # colour of the dialogue box
lgn.resizable(False, False)
'''This code is used to disable the resizable option,
we can't able adjust the size of the dialogue box'''


def login():  # This is def function used display the message box
    user = txtlbl.get()
    pwd = txtlbl1.get()
    if user == 'Vanideve11' and pwd == '9847':
        messagebox.showinfo("Note", "Success")
    elif user != 'Vanideve11':
        messagebox.showinfo("Note", "Your username is incorrect")
    elif pwd != '9847':
        messagebox.showinfo("Note", "Your Password is incorrect")
    else:
        messagebox.showinfo("Note", "Incorrect")


def show_and_hide():
    # This def function is used to display the interior work of the dialogue box
    if txtlbl1['show'] == '*':
        txtlbl1['show'] = ''
    else:
        txtlbl1['show'] = '*'


e1_frame = Frame(lgn, bg="grey")
e1_frame.pack(side=TOP, fill=X)

lbl = Label(e1_frame, text="welcome to Python language", font=("Eras Demi ITC", 20, "bold"), bg="grey", fg="black")
lbl.grid(row=0, columnspan=3, padx=50, pady=10)

lbl2 = Label(e1_frame, text="Username", font=("times", 16), bg="grey", fg="black")
lbl2.grid(row=2, column=0, padx=10, pady=50)
txtlbl = Entry(e1_frame, font=("times", 16), bg="white", fg="black")
txtlbl.grid(row=2, column=1, padx=10, pady=10)

lbl3 = Label(e1_frame, text="Password", font=("times", 16), bg="grey", fg="black")
lbl3.grid(row=3, column=0, padx=10, pady=10)
txtlbl1 = Entry(e1_frame, show="*", font=("times", 16), bg="white", fg="black")
txtlbl1.grid(row=3, column=1, padx=10, pady=10)

checkBox_showPassword = Checkbutton(e1_frame, text="show", bg='grey', fg='black',
                                    font=('Times', 12), command=show_and_hide)
checkBox_showPassword.grid(row=3, column=2, padx=0, pady=0, sticky="e")

btn = Button(e1_frame, text="Submit", width=10, font=("Times", 16, "bold"), bg="yellow", fg="black", command=login)
btn.grid(row=5, column=1, padx=30, pady=10, sticky="e")

lgn.mainloop()