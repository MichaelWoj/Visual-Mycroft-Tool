import tkinter as tk
from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
import os, subprocess, fileinput

root = tk.Tk()

##Sets up the UI window of the app

root.title('Mycroft Skill Maker')
root.geometry("1000x500")

canvas = Canvas(root, width=800, height=500, bg="white")

def select_file_button():
	global folder_path
	## Opens a window allowing the user to select a file.
	## The file is then open in a+ (appending and reading mode). The selecter window allows the user to see just .py files or all filses 
	folder_path = filedialog.askopenfile(mode = "a+",title="Select Your New Skill __init__ File", filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))

def new_project_button():
	## The button activates the command prompt, goes to the specified folder and activates Mycroft's skill create feature, " mycroft-msk create"
	os.system("gnome-terminal -e 'bash -c \"cd ..; cd mycroft-core; mycroft-msk create; exec bash\"'")

def clear_all():
	canvas.delete("all")


## Sets up the TKinter menu
menu = Menu(root)
root.config(menu=menu)


subMenu = Menu(menu)

## Creates a submenu for multiple buttons to be hidden in it 
menu.add_cascade(label="Settings", menu=subMenu)
subMenu.add_command(label="Save")

## Create a button in the submenu called New Project and sets new_project_button as the code to be executed
subMenu.add_command(label="New Project", command= new_project_button)
subMenu.add_command(label="Select File", command= select_file_button)
subMenu.add_command(label="Help")
subMenu.add_command(label="Exit", command= root.quit)
menu.add_command(label="Clear All", command= clear_all)
#menu.add_command(label="Undo", command= folder_path.edit_undo)
#menu.add_command(label="Redo", command= folder_path.edit.redo)

 
style = ttk.Style(root)

## Configures the notebook style and set the tab position to West
style.configure('lefttab.TNotebook', tabposition='w')

## Sets the theme and side of the tab buttons
style.theme_settings("default", {"TNotebook.Tab": {"configure": {"padding": [30, 40]}}})

## The notebook style is set and assigned to a variable name 
notebook = ttk.Notebook(root, style='lefttab.TNotebook' )

## Tab frame created 
t1 = tk.Frame(notebook)
t2 = tk.Frame(notebook)
t3 = tk.Frame(notebook)

## Creates the side tabs
notebook.add(t1, text='Start')
notebook.add(t2, text='Middle')
notebook.add(t3, text='Ending ')
## Sets all of the side tab location to column 0 
notebook.grid(column = 0)
## The side tabs are chaned into canvases allowing shapes to be created on them. The canvas size and colour are set and tabs are assigned.
t1_canvas = Canvas(t1, width=200, height=500, bg='red')
t2_canvas = Canvas(t2, width=200, height=500, bg='blue')
t3_canvas = Canvas(t3, width=200, height=500, bg='green')

## The points represent the x and y axis of the canvas and each 2 points a point where the line stops.
## Eg if you take the first 6 points [20, 20, 20, 100, 100, 100]. This means the line starts at 20, 20 and goes to 20, 100 and from that point it turns to 100, 100 to make another point there
t1_points1 = [20, 20, 20, 100, 100, 100, 100, 80, 120, 80, 120, 40, 100, 40, 100, 20 ]
## shape is created by taking the pre-established points and specifying the shape's border and inside colour as well as border width.
t1_shape1 = t1_canvas.create_polygon(t1_points1, outline='#000', fill='#7e2530', width=2)
t1_canvas.grid(column = 1)

t2_points1 = [20, 20, 20, 40, 40, 40, 40, 80, 20, 80, 20, 100, 100, 100, 100, 80, 120, 60, 100, 40, 100, 20]
t2_shape1 = t2_canvas.create_polygon(t2_points1, outline='#000', fill='#003153', width=2)
t2_canvas.grid(column = 1)

#t2_points2 = [20, 120, 20, 140, 40, 160, 20, 180, 20, 200, 100, 200, 100, 180, 120, 160, 100, 140, 100, 120]

t3_points1 = [20, 20, 20, 40, 40, 60, 20, 80, 20, 100, 100, 100, 100, 20]
t3_shape1 = t3_canvas.create_polygon(t3_points1, outline='#000', fill='#00630d', width=2)
t3_canvas.grid(column = 1)


def t1_button1_code(self):

	## The buttonstton shape is reproduced on the main canvas 
	canvas.create_polygon(t1_points1, outline='#000', fill='#7e2530', width=2)
	canvas.grid(row= 0, column = 2)

	for import_line in fileinput.FileInput(folder_path.name, inplace=1):
		if 'from mycroft import MycroftSkill, intent_file_handler' in import_line:
			import_line = import_line.replace(import_line,import_line+'from adapt.intent import IntentBuilder \nimport datetime ')
		print(import_line, end='')


## When the left mouse button is clicked on the shape it executes t1_button1_code
t1_canvas.tag_bind(t1_shape1, "<Button-1>", t1_button1_code)

def t2_button1_code(self):

	canvas.create_polygon(t2_points1, outline='#000', fill='#003153', width=2)
	canvas.grid(row= 0, column = 3)

	for function_line in fileinput.FileInput(folder_path.name, inplace=1):
		if '(self, message):' in function_line:
			function_line = function_line.replace(function_line,function_line+'        now = datetime.datetime.now()\n')
		print(function_line, end='')

	for function_output_line in fileinput.FileInput(folder_path.name, inplace=1):
		if 'self.speak_dialog' in function_output_line:
				#print(function_output_line.replace(')', '', 1))
				function_output_line = function_output_line.replace(')','+ now.strftime(" %Y-%m-%d %H:%M:%S"))')
		print(function_output_line, end='')

t2_canvas.tag_bind(t2_shape1, "<Button-1>", t2_button1_code)

def t3_button1_code(self):

	canvas.create_polygon(t3_points1, outline='#000', fill='#00630d', width=2)
	canvas.grid(row= 0, column = 4)

	for ending_line in fileinput.FileInput(folder_path.name, inplace=1):
		if 'now.strftime(" %Y-%m-%d %H:%M:%S"))' in ending_line:
				ending_line = ending_line.replace(ending_line,ending_line+'\n    def stop(self):\n         pass')
		print(ending_line, end='')



t3_canvas.tag_bind(t3_shape1, "<Button-1>", t3_button1_code)

root.mainloop()