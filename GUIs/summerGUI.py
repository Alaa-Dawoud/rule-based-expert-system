from datetime import datetime
date = datetime.now()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Weather Expert System")


# check if it sunny
l_sunny = Label(root, text=" is it sunny ? ")
l_sunny.grid(row=1, column=0)
# check if it humid  
l_humid = Label(root, text=" is it humid ? ")
l_humid.grid_forget()

# check if it is fresh air
l_fresh_air = Label(root, text=" is it fresh air ? ")
l_fresh_air.grid_forget()


# state for each condition set default to false
# b1 for sunny sky b2 for humid b3 for fresh air
b1 = IntVar()
b1.set(0)
b2 = IntVar()
b2.set(0)
b3 = IntVar()
b3.set(0)


# Radio buttons for first condition sunny
#q1r1 question 1 radio button 1 and so on
q1r1 = Radiobutton(root, text='yes', variable=b1, value=1, command=lambda: apply_condition1(b1.get()))
q1r1.grid(row=1, column=2, padx=20)
q1r2 = Radiobutton(root, text='no', variable=b1, value=0, command=lambda: apply_condition1(b1.get()))
q1r2.grid(row=1, column=3, padx=20)
# Radio buttons for second condition humid
q2r1 = Radiobutton(root, text='yes', variable=b2, value=1, command=lambda: apply_condition2(b2.get()))
q2r1.grid_forget()
q2r2 = Radiobutton(root, text='no', variable=b2, value=0, command=lambda: apply_condition2(b2.get()))
q2r2.grid_forget()
# Radio buttons for third condition fresh air
q3r1 = Radiobutton(root, text='yes', variable=b3, value=1, command=lambda: apply_condition3(b3.get()))
q3r1.grid_forget()
q3r2 = Radiobutton(root, text='no', variable=b3, value=0, command=lambda: apply_condition3(b3.get()))
q2r2.grid_forget()

def apply_condition1(b1_value):
    
    if b1_value: 
        messagebox.showinfo("Answer", "you should take umbrella , and weaer sun glasses to protect you eyes, and it's better to wear white clothes.")
        if date.weekday() == 4  or date.weekday == 5:
            messagebox.showinfo("Answer", "forget about what i say let's go to the beach.")
    elif not b1_value:
        #remove q1
        l_sunny.grid_forget()
        q1r1.grid_forget()
        q1r2.grid_forget()
        # add q2
        l_humid.grid(row=1, column=0)
        q2r1.grid(row=1, column=2, padx=20)
        q2r2.grid(row=1, column=3, padx=20)

def apply_condition2(b2_value):        
    if b2_value:
        
        messagebox.showinfo("Answer", " you should avoid being in crowd places .")
    if not b2_value:
        #remove q2
        l_humid.grid_forget()
        q2r1.grid_forget()
        q2r2.grid_forget()
        # add q3
        l_fresh_air.grid(row=1, column=0)
        q3r1.grid(row=1, column=2, padx=20)
        q3r2.grid(row=1, column=3, padx=20)
def apply_condition3(b3_value):
    if b3_value and (date.weekday == 4 or date.weekday == 5):
        messagebox.showinfo("Answer", "what about going to the park ? ")
    else:
        messagebox.showinfo("Answer", "you are ok with whatever you wear.")

root.mainloop()