import tkinter

# Intializing Screen
window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="Label", font=("Arial", 16, "bold"))
my_label.grid(row=0, column=0)

# Configure something
my_label.config(text="Test")


# Fucnction for buttons
def submit_button():
    my_label.config(text="Form Submmitted")
    button.config(text="Unavailable")


def change_label():
    my_label.config(text=input_field.get())


# Button
button = tkinter.Button(text="Submit", command=submit_button)
button.grid(row=1, column=1)

# Entry
input_field = tkinter.Entry(width=20)
input_field.grid(row=2, column=3)

# Button for entry
change_button = tkinter.Button(text="Change Label", command=change_label)
change_button.grid(row=0, column=2)


# Keeps window on screen
window.mainloop()
