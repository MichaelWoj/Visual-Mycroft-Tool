import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
import os, subprocess

root = tk.Tk()

root.title('Mycroft Skill Maker')
root.geometry("1000x500")

canvas = Canvas(root, width=800, height=500, bg="white")

def select_file_button():
	global folder_path
	filename = filedialog.askopenfile(title="Select Your New Skill __init__ File", filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))
	#openfile = open(filename, 'a')
	#folder_path.set(filename)
	#print(filename)

def new_project_button():
	os.system("gnome-terminal -e 'bash -c \"cd ..; cd mycroft-core; mycroft-msk create; exec bash\"'")

def clear_all():
	canvas.delete("all")

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Settings", menu=subMenu)
subMenu.add_command(label="Save")
subMenu.add_command(label="New Project", command= new_project_button)
subMenu.add_command(label="Select File", command= select_file_button)
subMenu.add_command(label="Help")
subMenu.add_command(label="Exit", command= root.quit)
menu.add_command(label="Clear All", command= clear_all)
#menu.add_command(label="Undo", command= canvas.)
#menu.add_command(label="Redo", command= canvas.)

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='w')
style.theme_settings("default", {"TNotebook.Tab": {"configure": {"padding": [30, 40]}}})
notebook = ttk.Notebook(root, style='lefttab.TNotebook', width=200, height=500 )

t1 = tk.Frame(notebook, bg='red')
t2 = tk.Frame(notebook, bg='blue')
t3 = tk.Frame(notebook, bg='green')
t4 = tk.Frame(notebook, bg='yellow')
t5 = tk.Frame(notebook, bg='purple')

notebook.add(t1, text='Tab 1')
notebook.add(t2, text='Tab 2')
notebook.add(t3, text='Tab 3')
notebook.add(t4, text='Tab 4')
notebook.add(t5, text='Tab 5')
notebook.grid(column = 0)

t1_canvas = Canvas(t1, width=200, height=500, bg='red')
t2_canvas = Canvas(t2, width=200, height=500, bg='blue')
t3_canvas = Canvas(t3, width=200, height=500)
t4_canvas = Canvas(t4, width=200, height=500)
t5_canvas = Canvas(t5, width=200, height=500)

def callback(event):
	draw(event.x, event.y)

def draw(x, y):
	canvas.coords(circle, x-20, y-20, x+20, y+20)

def t1_shape1_code():
	openfile = open(filename, 'a')
	print("Hello there")
	openfile.close()	

canvas.bind('<Motion>', callback)

circle = canvas.create_oval(20, 20, 100, 100)
canvas.grid(row =0, column = 1)

t1_points1 = [20, 20, 20, 100, 100, 100, 100, 80, 120, 80, 120, 40, 100, 40, 100, 20 ]
t1_shape1 = t1_canvas.create_polygon(t1_points1, outline='#000', fill='#7e2530', width=2)
t1_canvas.grid(column = 1)

t2_points1 = [20, 20, 20, 40, 40, 40, 40, 80, 20, 80, 20, 100, 100, 100, 100, 80, 120, 60, 100, 40, 100, 20]
t2_shape1 = t2_canvas.create_polygon(t2_points1, outline='#000', fill='#003153', width=2)
t2_canvas.grid(column = 1)

t2_points2 = [20, 120, 20, 140, 40, 160, 20, 180, 20, 200, 100, 200, 100, 180, 120, 160, 100, 140, 100, 120]
t2_shape2 = t2_canvas.create_polygon(t2_points2, outline='#000', fill='#003153', width=2)
t2_canvas.grid(column = 1)


root.mainloop()