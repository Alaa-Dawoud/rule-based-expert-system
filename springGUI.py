from datetime import datetime
date = datetime.now()

from tkinter import *

root = Tk()
root.title("Weather Expert System")
Label(root, text="hello to weather expert system").grid(row=0, column=0)


# check if it clear sky
Label(root, text=" is it clear sky ? ").grid(row=1, column=0)

# check if it warmer  
Label(root, text=" is it warmer than normal ? ").grid(row=2, column=0)

# state for each condition set default to false
# b1 for clear sky b2 for warmer
b1 = IntVar()
b1.set(0)
b2 = IntVar()
b2.set(0)

# Radio buttons for first condition clear sky
Radiobutton(root, text='yes', variable=b1, value=1, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=1, column=2, padx=20)
Radiobutton(root, text='no', variable=b1, value=0, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=1, column=3, padx=20)

# Radio buttons for second condition warmer
Radiobutton(root, text='yes', variable=b2, value=1, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=2, column=2, padx=20)
Radiobutton(root, text='no', variable=b2, value=0, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=2, column=3, padx=20)


def apply_conditions(b1_value, b2_value):

    condition = Entry(root, width=100)
    condition.grid(row=5, column=0, columnspan=5, padx=20)

    if (b1_value and b2_value) or b2_value:
        condition.insert(0, "Wear light cloths/have a cold shower.")
        if date.weekday == 4 or date.weekday == 5:
            condition.insert(0, "Go to the beach")
    elif b1_value:
        condition.insert(0, "Have a walk to the work.")
        if date.weekday == 4 or date.weekday == 5:
            condition.insert(0, "Fly a kite!")
    else:
        condition.insert(0, "what about going to the country?")
        
root.mainloop()