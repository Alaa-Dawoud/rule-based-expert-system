from datetime import datetime
date = datetime.now()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Weather Expert System")


# check if it snowy
l_snowy = Label(root, text=" is it snowy ? ")
l_snowy.grid(row=1, column=0)

# check if it rainy  
l_rainy = Label(root, text=" is it rainy ? ")
l_rainy.grid_forget()

# state for each condition set default to false
# b1 for snowy b2 for rainy
b1 = IntVar()
b1.set(0)
b2 = IntVar()
b2.set(0)

# Radio buttons for first condition snowy
q1r1 = Radiobutton(root, text='yes', variable=b1, value=1, command=lambda: apply_condition1(b1.get()))
q1r1.grid(row=1, column=2, padx=20)
q1r2 = Radiobutton(root, text='no', variable=b1, value=0, command=lambda: apply_condition1(b1.get()))
q1r2.grid(row=1, column=3, padx=20)

# Radio buttons for second condition rainy
q2r1 = Radiobutton(root, text='yes', variable=b2, value=1, command=lambda: apply_condition2(b2.get()))
q2r1.grid_forget()
q2r2 = Radiobutton(root, text='no', variable=b2, value=0, command=lambda: apply_condition2(b2.get()))
q2r2.grid_forget()


def apply_condition1(b1_value):

    if b1_value: 
        messagebox.showinfo("Answer", "your should wear gloves and boot")
    elif not b1_value:
        #remove q1
        l_snowy.grid_forget()
        q1r1.grid_forget()
        q1r2.grid_forget()
        #add q2
        l_rainy.grid(row=1, column=0)
        q2r1.grid(row=1, column=2, padx=20)
        q2r2.grid(row=1, column=3, padx=20)
def apply_condition2(b2_value):
    if b2_value:
        messagebox.showinfo("Answer", "your should wear a jacket and take umberella if u go out.")
    elif not b2_value:
        messagebox.showinfo("Answer", "you are ok with any thing you wear.")
    
    elif b2_value and (date.weekday == 4 or date.weekday == 5):
        messagebox.showinfo("Answer", "don't forget it's holiday spend it in warm areas.")

root.mainloop()