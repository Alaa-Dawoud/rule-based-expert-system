
from tkinter import *

root = Tk()
root.title("Weather Expert System")
Label(root, text="hello to weather expert system").grid(row=0, column=0)


# check if it windy
Label(root, text=" is it windy ? ").grid(row=1, column=0)

# check if it rainy  
Label(root, text=" is it rainy ? ").grid(row=2, column=0)

# state for each condition set default to false
# b1 for windy b2 for rainy
b1 = IntVar()
b1.set(0)
b2 = IntVar()
b2.set(0)

# Radio buttons for first condition windy
Radiobutton(root, text='yes', variable=b1, value=1, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=1, column=2, padx=20)
Radiobutton(root, text='no', variable=b1, value=0, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=1, column=3, padx=20)

# Radio buttons for second condition rainy
Radiobutton(root, text='yes', variable=b2, value=1, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=2, column=2, padx=20)
Radiobutton(root, text='no', variable=b2, value=0, command=lambda: apply_conditions(b1.get(), b2.get())).grid(row=2, column=3, padx=20)


def apply_conditions(b1_value, b2_value):

    condition = Entry(root, width=100)
    condition.grid(row=5, column=0, columnspan=5, padx=20)

    if b1_value and b2_value: 
        condition.insert(0, "you don't have to go out")
    elif b1_value:
        condition.insert(0, "you should wear pullover.")
    elif b2_value:
        condition.insert(0, "your should wear a jacket and take umberella if u go out.")
    else:
        condition.insert(0, "you are ok with whatever you wear.")

root.mainloop()