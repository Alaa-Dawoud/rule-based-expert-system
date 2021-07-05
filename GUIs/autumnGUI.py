
from tkinter import *
from tkinter import messagebox

root = Tk()
bg_color = "#a5ccc0"
win_width = root.winfo_screenwidth()
win_height = root.winfo_screenheight()
root.geometry("600x400+450+150")
root.title("Weather Expert System")
root.option_add('*Font','Aria 20')
root.config(bg=bg_color)


main_frame = Frame()
main_frame.pack(padx=win_width/2-600, pady=150)



# check if it windy
l_windy = Label(main_frame, text=" is it windy ? ")
l_windy.grid(row=1, column=0)

# check if it rainy  
l_rainy = Label(main_frame, text=" is it rainy ? ")
l_rainy.grid_forget()

# state for each condition set default to false
# b1 for windy b2 for rainy
b1 = IntVar()
b1.set(0)
b2 = IntVar()
b2.set(0)

# Radio buttons for first condition windy
q1r1 = Radiobutton(main_frame, text='yes', variable=b1, value=1, command=lambda: apply_condition1(b1.get()), bg=bg_color)
q1r1.grid(row=1, column=2)
q1r2 = Radiobutton(main_frame, text='no', variable=b1, value=0, command=lambda: apply_condition1(b1.get()), bg=bg_color)
q1r2.grid(row=1, column=3)

# Radio buttons for second condition rainy
q2r1 = Radiobutton(main_frame, text='yes', variable=b2, value=1, command=lambda: apply_condition2(b2.get()), bg=bg_color)
q2r1.grid_forget()
q2r2 = Radiobutton(main_frame, text='no', variable=b2, value=0, command=lambda: apply_condition2(b2.get()), bg=bg_color)
q2r2.grid_forget()


def apply_condition1(b1_value):

    if b1_value:
        messagebox.showinfo("Answer", "you should wear pullover.")
    elif not b1_value:
        #remove q1
        l_windy.grid_forget()
        q1r1.grid_forget()
        q1r2.grid_forget()
        #add q2
        l_rainy.grid(row=1, column=0)
        q2r1.grid(row=1, column=2)
        q2r2.grid(row=1, column=3)
def apply_condition2(b2_value):
    if b2_value:
        messagebox.showinfo("Answer", "your should wear a jacket and take umberella if u go out.")
    elif not b2_value:
        messagebox.showinfo("Answer", "you are ok with whatever you wear.")

root.mainloop()