from tkinter import *

def clear_all():
    principal_field.delete(0, END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_field.delete(0,END)

    principal_field.focus_set()

def calculate_ci():
    try:
        principal = int(principal_field.get())
        rate = float(rate_field.get())
        time = int(time_field.get())

        CI = principal * (pow((1+rate/100),time))
        compound_field.delete(0, END)
        compound_field.insert(10, round(CI,2))
    except ValueError:
        compound_field.delete(0, END)
        compound_field.insert(10, "Invalid Input")


if __name__ == '__main__':
    root = Tk()
    root.configure(background='light blue')
    root.geometry('400x300')
    root.title("Compund Interest Calculator")

    label1 = Label(root, text = 'Principal Amount(Rs): ', fg='black', bg='red')
    label2 = Label(root, text = 'Rate(%): ', fg='black', bg='red')
    label3 = Label(root, text = 'Time(years): ',fg='black', bg='red')
    label4 = Label(root, text = 'Compound Interest: ', fg='black', bg='red')

    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=5, column=0, padx=10, pady=10)

    principal_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    compound_field = Entry(root)

    principal_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    compound_field.grid(row=5, column=1, padx=10, pady=10)

    btn1 = Button(root, text='Submit', bg='light green', fg='black', command = calculate_ci)
    btn2 = Button(root, text='Clear', bg='light green', fg='black', command = clear_all)
    btn1.grid(row=4, column=1, pady=10)
    btn2.grid(row=6, column=1, pady=10)

    root.mainloop()
