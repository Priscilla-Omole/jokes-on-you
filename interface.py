from tkinter import *
from tkinter import ttk
import jokes

root = Tk()
root.title("Jokes Land")

frm = ttk.Frame(root, padding=10)
frm.grid()


ttk.Label(frm, text="Welcome to Jokes Land").grid(
    column=0, row=0, columnspan=2, pady=10)

joke_label = ttk.Label(frm, text=jokes.call_joke(), wraplength=300)
joke_label.grid(column=0, row=1, columnspan=2, pady=10)


def next_joke():
    joke_label.config(text=jokes.call_joke())

ttk.Button(frm, text="Next Joke", command=next_joke).grid(
    column=0, row=2, pady=10
)

ttk.Button(frm, text="Quit", command=root.destroy).grid(
    column=1, row=2, pady=10
)

root.mainloop()