from tkinter import *

root = Tk()

root.title("My Title")

root.geometry("300x250")

but1 = Button(root)

but1["text"] = "Hello"

btn = Button(text="Hello",
             background="#555",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16")


def hello(event):
    print("Hello World!")

but1.bind("<Button-1>",hello)

but1.pack()

root.mainloop()