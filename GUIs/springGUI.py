
from datetime import datetime
date = datetime.now()

from tkinter import *
from tkinter import messagebox

root = Tk()
bg_color = "#25D366"
win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()
root.geometry("800x400+150+150")
root.title("Weather Expert System")
root.option_add('*Font','Aria 20')
root.config(bg=bg_color)


main_frame = Frame()
main_frame.pack(padx=win_width/2-600, pady=150)


# check if it clear sky
l_sky = Label(main_frame, text=" is it clear sky ? ")
l_sky.grid(row=1, column=0)

# check if it warmer  
l_warm = Label(main_frame, text=" is it warmer than normal ? ")
l_warm.grid_forget()

# state for each condition set default to false
# b1 for clear sky b2 for warmer
b1 = IntVar()
b1.set(0)
b2 = IntVar()
b2.set(0)

# Radio buttons for first condition clear sky
q1r1 = Radiobutton(main_frame, text='yes', variable=b1, value=1, command=lambda: apply_condition1(b1.get()), bg=bg_color)
q1r1.grid(row=1, column=2)
q1r2 = Radiobutton(main_frame, text='no', variable=b1, value=0, command=lambda: apply_condition1(b1.get()), bg=bg_color)
q1r2.grid(row=1, column=3)

# Radio buttons for second condition warmer
q2r1 = Radiobutton(main_frame, text='yes', variable=b2, value=1, command=lambda: apply_condition2(b2.get()), bg=bg_color)
q2r1.grid_forget()
q2r2 = Radiobutton(main_frame, text='no', variable=b2, value=0, command=lambda: apply_condition2(b2.get()), bg=bg_color)
q2r2.grid_forget()


def apply_condition1(b1_value):

    if b1_value:
        messagebox.showinfo("Answer", "Wear light cloths/have a cold shower.")
        if date.weekday == 4 or date.weekday == 5:
            messagebox.showinfo("Answer", "Go to the beach")
    elif not b1_value:
        flag_question = False
        #remove q1
        l_sky.grid_forget()
        q1r1.grid_forget()
        q1r2.grid_forget()
        #show q2
        l_warm.grid(row=1, column=0)
        q2r1.grid(row=1, column=2)
        q2r2.grid(row=1, column=3)
        
def apply_condition2(b2_value):
    if b2_value and not(date.weekday == 4 or date.weekday == 5):
        messagebox.showinfo("Answer", "Have a walk to the work.")
    elif b2_value and (date.weekday == 4 or date.weekday == 5):
            messagebox.showinfo("Answer", "Fly a kite!")
    elif not b2_value:
        messagebox.showinfo("Answer", "what about going to the country?")
        
root.mainloop()