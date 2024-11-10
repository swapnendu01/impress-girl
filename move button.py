from tkinter import *
import random

def show_popup():
    popup = Toplevel(root)
    popup.title("popup")
    label = Label(popup, text="i like to you 😊❤️")
    label.pack(padx=20, pady=20)

def move_button(event):
    x = random.randint(0, 350)
    y = random.randint(0, 350)
    no_button.place(x=x, y=y)

root = Tk()
root.title("instagram:@python")
root.geometry("400x400")

question_label = Label(root, text="do you like me?")
question_label.pack(pady=20)

yes_button = Button(root, text="yes", command=show_popup)
yes_button.pack()

no_button = Button(root, text="no")
no_button.pack()


no_button.bind('<Enter>', move_button)

root.mainloop()