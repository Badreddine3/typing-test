import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog

from tkinter.messagebox import showinfo

import self as self

root = tk.Tk()
root.geometry('500x400')
root.resizable(False, False)
root.title('typing speed test')
start_button = ttk.Button(
    root,
    text='start',
    command=lambda: root.quit()
)
start_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
root.mainloop()

USER_INP = simpledialog.askstring(title="output",
                                  prompt="the text is")
