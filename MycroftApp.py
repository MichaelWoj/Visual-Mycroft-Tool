import tkinter as tk
from tkinter import * 
from tkinter import ttk
import os, subprocess

root = Tk()

root.title('Mycroft Skill Maker')
root.configure(background = "white")
root.minsize(1000, 500)

style = ttk.Style(root)

style.configure('lefttab.TNotebook', tabposition='ws')
style.theme_settings("default", {"TNotebook.Tab": {"configure": {"padding": [30, 30]}}})
notebook = ttk.Notebook(root, style='lefttab.TNotebook')

f1 = tk.Frame(notebook, bg='red', width=400, height=500)
f2 = tk.Frame(notebook, bg='blue', width=400, height=500)
f3 = tk.Frame(notebook, bg='green', width=400, height=500)
f4 = tk.Frame(notebook, bg='yellow', width=400, height=500)
f5 = tk.Frame(notebook, bg='purple', width=400, height=500)

notebook.add(f1, text='Frame 1')
notebook.add(f2, text='Frame 2')
notebook.add(f3, text='Frame 3')
notebook.add(f4, text='Frame 4')
notebook.add(f5, text='Frame 5')
notebook.pack()


root.mainloop()