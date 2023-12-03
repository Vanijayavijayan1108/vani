from tkinter import *

grd=Tk()
grd.geometry("1000x500")
grd.title("Grade")
grd.config(bg = "grey")

def grade():

    m1 = int(m1ety.get())
    m2 = int(m2ety.get())
    m3 = int(m3ety.get())

    total = m1 + m2 + m3
    t_ety.delete(0, END)
    t_ety.insert(0, total)

    average = total/3
    Avgety.delete(0, END)
    Avgety.insert(0, average)

    if m1 >= 35 and m2 >= 35 and m3 >= 35:
        rtlsety.delete(0, END)
        rtlsety.insert(0, "Pass")

        if average >= 90 and average <=100:
            grdety.delete(0, END)
            grdety.insert(0, "Distinction")

        elif average >= 80 and average < 90:
            grdety.delete(0, END)
            grdety.insert(0, "A grade")

        elif average >= 70 and average < 80:
            grdety.delete(0, END)
            grdety.insert(0, "B grade")

        elif average >= 60 and average < 70:
            grdety.delete(0, END)
            grdety.insert(0, "C grade")

        else:
            grdety.delete(0, END)
            grdety.insert(0, "D grade")

    else:
        rtlsety.delete(0, END)
        rtlsety.insert(0, "Fail")
        grdety.delete(0, END)
        grdety.insert(0, "No grade")

frame = Frame(grd, bg = "grey")
frame.pack(side = TOP, fill = X)

lbl1 = Label(frame, text = "Your Grade!",font = ("Verdana", 20, "bold"), bg = "grey", fg = "black")
lbl1.grid(row = 0, columnspan = 4, padx = 10, pady = 50)

namelbl = Label(frame, text = "Student Name",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
namelbl.grid(row = 1, column = 0, padx = 10, pady = 10)
name_ety = Entry(frame, font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
name_ety.grid(row = 1, column = 1, padx = 10, pady = 10)

m1lbl  = Label(frame, text = "Subject 1",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
m1lbl.grid(row = 2, column = 0, padx = 10, pady = 10)
m1ety = Entry(frame,font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
m1ety.grid(row = 2, column = 1, padx = 10, pady = 10)

m2lbl = Label(frame, text = "Subject 2",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
m2lbl.grid(row = 3, column = 0, padx = 10, pady = 10)
m2ety = Entry(frame, font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
m2ety.grid(row = 3, column = 1, padx = 10, pady = 10)

m3lbl = Label(frame, text = "Subject 3",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
m3lbl.grid(row = 4, column = 0, padx = 10, pady = 10)
m3ety = Entry(frame, font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
m3ety.grid(row = 4, column = 1, padx = 10, pady = 10)

t_lbl = Label(frame, text = "Total",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
t_lbl.grid(row = 1, column = 2, padx = 10, pady = 10)
t_ety = Entry(frame, font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
t_ety.grid(row = 1, column = 3, padx = 10, pady = 10)

Avglbl = Label(frame, text = "Average",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
Avglbl.grid(row = 2, column = 2, padx = 10, pady = 10)
Avgety = Entry(frame,font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
Avgety.grid(row = 2, column = 3, padx = 10, pady = 10)

rtlslbl = Label(frame, text = "Result",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
rtlslbl.grid(row = 3, column = 2, padx = 10, pady = 10)
rtlsety = Entry(frame, font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
rtlsety.grid(row = 3, column = 3, padx = 10, pady = 10)

grdlbl = Label(frame, text = "Grade",font = ("Verdana", 16, "bold"), bg = "grey", fg = "black")
grdlbl.grid(row = 4, column = 2, padx = 10, pady = 10)
grdety = Entry(frame, font = ("Verdana", 16, "bold"), bg = "white", fg = "black")
grdety.grid(row = 4, column = 3, padx = 10, pady = 10)

btn = Button(frame, text = "Submit", command = grade, bg = "yellow", fg = "black",font = ("Verdana", 18, "bold"))
btn.grid(row = 5, column = 3, padx = 10, pady = 20)

grd.mainloop()