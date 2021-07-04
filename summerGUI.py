from datetime import datetime
date = datetime.now()

from tkinter import *

root = Tk()
root.title("Weather Expert System")
Label(root, text="hello to weather expert system").grid(row=0, column=0)



# check if it sunny
Label(root, text=" is it sunny ? ").grid(row=1, column=0)
# check if it humid  
Label(root, text=" is it humid ? ").grid(row=2, column=0)
# check if it is fresh air
Label(root, text=" is it fresh air ? ").grid(row=3, column=0)

# state for each condition set default to false
# b1 for sunny sky b2 for humid b3 for fresh air
b1 = IntVar()
b1.set(0)
b2 = IntVar()
b2.set(0)
b3 = IntVar()
b3.set(0)


# Radio buttons for first condition sunny
Radiobutton(root, text='yes', variable=b1, value=1, command=lambda: apply_conditions(b1.get(), b2.get(), b3.get())).grid(row=1, column=2, padx=20)
Radiobutton(root, text='no', variable=b1, value=0, command=lambda: apply_conditions(b1.get(), b2.get(), b3.get())).grid(row=1, column=3, padx=20)
# Radio buttons for second condition humid
Radiobutton(root, text='yes', variable=b2, value=1, command=lambda: apply_conditions(b1.get(), b2.get(), b3.get())).grid(row=2, column=2, padx=20)
Radiobutton(root, text='no', variable=b2, value=0, command=lambda: apply_conditions(b1.get(), b2.get(), b3.get())).grid(row=2, column=3, padx=20)
# Radio buttons for third condition fresh air
Radiobutton(root, text='yes', variable=b3, value=1, command=lambda: apply_conditions(b1.get(), b2.get(), b3.get())).grid(row=3, column=2, padx=20)
Radiobutton(root, text='no', variable=b3, value=0, command=lambda: apply_conditions(b1.get(), b2.get(), b3.get())).grid(row=3, column=3, padx=20)

def apply_conditions(b1_value, b2_value, b3_value):

    condition = Entry(root, width=100)
    condition.grid(row=5, column=0, columnspan=5, padx=20)

    if b1_value: 
        condition.insert(0, "you should take umbrella , and weaer sun glasses to protect you eyes, and it's better to wear white clothes.")
        if date.weekday() == 4  or date.weekday == 5:
            condition.insert(0, "forget about what i say let's go to the beach.")

    elif b2_value:
        condition.insert(0, " you should avoid being in crowd places .")

    elif b3_value and (date.weekday == 4 or date.weekday == 5):
        condition.insert(0, "what about going to the park ? ")
    else:
        condition.insert(0, "you are ok with whatever you wear.")

root.mainloop()