from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from datetime import datetime
import os, subprocess, fileinput, subprocess

root = Tk()

root.title('Mycroft Skill Maker')
root.geometry("1000x500")

##Sets up the main canvas size and colour
canvas = Canvas(root, width=800, height=500, bg="white")

## Function to open a window allowing the user to select a file when called.
def select_file_button():
	global folder_path
	## The file is then open in a+ (appending and reading mode). The selecter window allows the user to see just .py files or all filses 
	folder_path = filedialog.askopenfile(mode = "a+",title="Select Your New Skill __init__ File", filetypes=(("Python Files", "*.py"), ("All Files", "*.*")))

## Function to open a command prompt with a loaded Mycroft questionare when called.
def new_project_button():
	## The button activates the command prompt, goes to the specified folder and activates Mycroft's skill create feature, " mycroft-msk create"
	os.system("gnome-terminal -e 'bash -c \"cd ..; cd mycroft-core; mycroft-msk create; exec bash\"'")

## Function to open the README in the applcation when called
def help_button():
	opener = "open" if sys.platform == "dawrin" else "xdg-open"
	subprocess.call([opener, "README"])

point_adjustor = 0 
def point_mover():
	global point_adjustor
	point_adjustor = point_adjustor + 80
	return 

def line_editor(line_to_edit, what_to_edit, the_edit):
	for import_line in fileinput.FileInput(folder_path.name, inplace=1):
		if line_to_edit in import_line:
			import_line = import_line.replace(what_to_edit,the_edit)
		print(import_line, end='')
	

def line_replece(to_replace, replacement):
	for function_line in fileinput.FileInput(folder_path.name, inplace=1):
		if to_replace in function_line:
			#When the wanted line is found it clears the line, then reprents it with the added string
			function_line = function_line.replace(function_line,replacement)
		print(function_line, end='')

def line_addition(what_to_find, what_to_add):		
	for import_line in fileinput.FileInput(folder_path.name, inplace=1):
		if what_to_find in import_line:
			import_line = import_line.replace(import_line,import_line+what_to_add)
		print(import_line, end='')

def line_deletion(delete_this):
	for function_line in fileinput.FileInput(folder_path.name, inplace=1):
		if delete_this in function_line:
			function_line = function_line.replace(function_line,'')
		print(function_line, end='')

## Sets up the TKinter menu
menu = Menu(root)
root.config(menu=menu)

## Creates a submenu for multiple buttons to be hidden in it 
subMenu = Menu(menu)

## Label which gives the option a name in menu
menu.add_cascade(label="Settings", menu=subMenu)
# Create a button in the submenu called New Project and sets new_project_button as the code to be executed
subMenu.add_command(label="New Project", command= new_project_button)
## Function the button executes when clicked
subMenu.add_command(label="Select File", command= select_file_button)
subMenu.add_command(label="Exit", command= root.quit)
menu.add_command(label="Help", command= help_button)
 
style = ttk.Style(root)

## Configures the notebook style and set the tab (North, South, East, West)
style.configure('lefttab.TNotebook', tabposition='w')

## Sets the theme and side of the tab buttons
style.theme_settings("default", {"TNotebook.Tab": {"configure": {"padding": [20, 40]}}})

# The notebook style is set and assigned to a variable name 
notebook = ttk.Notebook(root, style='lefttab.TNotebook' )

## Tab frame created and assigned a variable name  
t1 = Frame(notebook)
t2 = Frame(notebook)
t3 = Frame(notebook)
t4 = Frame(notebook)
t5 = Frame(notebook)
# Creates the side tabs
notebook.add(t1, text='Imports     ')
notebook.add(t2, text='Functions  ')
notebook.add(t3, text='Endings     ')
notebook.add(t4, text='Input         ')
notebook.add(t5, text='Statement')
## Sets the specified UI position in the Y axis 
notebook.grid(column = 0)
## The side tabs are chaned into canvases allowing shapes to be created on them. The canvas size and colour are set and tabs are assigned.
t1_canvas = Canvas(t1, width=200, height=500, bg='red')
t2_canvas = Canvas(t2, width=200, height=500, bg='blue')
t3_canvas = Canvas(t3, width=200, height=500, bg='green')
t4_canvas = Canvas(t4, width=200, height=500, bg='purple')
t5_canvas = Canvas(t5, width=200, height=500, bg='yellow')
## The points represent the x and y axis of the canvas and each 2 points a point where the line stops.
## Eg if you take the first 6 points [20, 20, 20, 100, 100, 100]. This means the line starts at 20, 20 and goes to 20, 100 and from that point it turns to 100, 100 to make another point there
t1_points1 = [20+point_adjustor, 20, 20+point_adjustor, 100, 100+point_adjustor, 100, 100+point_adjustor, 80, 120+point_adjustor, 80, 120+point_adjustor, 40, 100+point_adjustor, 40, 100+point_adjustor, 20 ]
## shape is created by taking the pre-established points and specifying the shape's border and inside colour as well as border width.
t1_shape1 = t1_canvas.create_polygon(t1_points1, outline='#000', fill='#7e2530', width=2)
t1_canvas.grid(column = 0)

t2_points1 = [20, 20, 20, 40, 40, 40, 40, 80, 20, 80, 20, 100, 100, 100, 100, 80, 120, 60, 100, 40, 100, 20]
t2_shape1 = t2_canvas.create_polygon(t2_points1, outline='#000', fill='#003153', width=2)
t2_canvas.grid(column = 0)

t2_points2 = [20, 120, 20, 140, 40, 160, 20, 180, 20, 200, 100, 200, 100, 180, 120, 160, 100, 140, 100, 120]
t2_shape2 = t2_canvas.create_polygon(t2_points2, outline='#000', fill='#003153', width=2)
t2_canvas.grid(column = 0)

t3_points1 = [20, 20, 20, 40, 40, 60, 20, 80, 20, 100, 100, 100, 100, 20]
t3_shape1 = t3_canvas.create_polygon(t3_points1, outline='#000', fill='#00630d', width=2)
t3_canvas.grid(column = 0)
## Function with code assigned for the first button

t4_points1 = [20, 20, 20, 40, 40, 60, 20, 80, 20, 100, 100, 100, 100, 20]
t4_shape1 = t4_canvas.create_polygon(t4_points1, outline='#000', fill='#7d12c4', width=2)
t4_canvas.grid(column = 0)

t5_points1 = [20, 20, 20, 40, 40, 40, 40, 80, 20, 80, 20, 100, 100, 100, 100, 80, 120, 60, 100, 40, 100, 20]
t5_shape1 = t5_canvas.create_polygon(t5_points1, outline='#000', fill='#a6a005', width=2)
t5_canvas.grid(column = 0)

t5_points2 = [20, 120, 20, 140, 40, 160, 20, 180, 20, 200, 100, 200, 100, 180, 120, 160, 100, 140, 100, 120]
t5_shape2 = t5_canvas.create_polygon(t5_points2, outline='#000', fill='#00630d', width=2)
t5_canvas.grid(column = 0)

canvas.grid(row = 0, column = 1, columnspan = 8, rowspan = 8 )

def t1_button1_code(self):

	global t1_shape1_on_canvas

	## The buttons shape is reproduced on the main canvas 
	t1_points1_on_canvas = [20+point_adjustor, 20, 20+point_adjustor, 100, 100+point_adjustor, 100, 100+point_adjustor, 80, 120+point_adjustor, 80, 120+point_adjustor, 40, 100+point_adjustor, 40, 100+point_adjustor, 20 ]
	t1_shape1_on_canvas = canvas.create_polygon(t1_points1_on_canvas, outline='#000', fill='#7e2530', width=2)

	what_to_find = 'from mycroft import MycroftSkill, intent_file_handler'
	what_to_add = 'from adapt.intent import IntentBuilder \nfrom datetime import datetime\n'

	line_addition(what_to_find,what_to_add)
# When the left mouse button is clicked on the shape it executes t1_button1_code 
	point_mover()
t1_canvas.tag_bind(t1_shape1, "<Button-1>", t1_button1_code)

def t1_button_shape1_removal(self):
	
	delete_this ='from adapt.intent import IntentBuilder'
	line_deletion(delete_this)
	
	delete_this ='import datetime'
	line_deletion(delete_this)

	canvas.delete(t1_shape1_on_canvas)

t1_canvas.tag_bind(t1_shape1, "<Button-3>", t1_button_shape1_removal)

def t2_button1_code(self):

	t2_points1 = [20+point_adjustor, 20, 20+point_adjustor, 40, 40+point_adjustor, 40, 40+point_adjustor, 80, 20+point_adjustor, 80, 20+point_adjustor, 100, 100+point_adjustor, 100, 100+point_adjustor, 80, 120+point_adjustor, 60, 100+point_adjustor, 40, 100+point_adjustor, 20]
	canvas.create_polygon(t2_points1, outline='#000', fill='#003153', width=2)

	t2_points1 = [20+point_adjustor, 20, 20+point_adjustor, 40, 40+point_adjustor, 40, 40+point_adjustor, 80, 20+point_adjustor, 80, 20+point_adjustor, 100, 100+point_adjustor, 100, 100+point_adjustor, 80, 120+point_adjustor, 60, 100+point_adjustor, 40, 100+point_adjustor, 20]
	canvas.create_polygon(t2_points1, outline='#000', fill='#003153', width=2)

	what_to_find = '(self, message):'
	what_to_add = '        now = datetime.now().time()\n        #ifstatement\n'
	line_addition(what_to_find, what_to_add)

	line_to_edit = 'self.speak_dialog'
	what_to_edit =')'
	the_edit = '+ now.strftime(" %Y-%m-%d %H:%M:%S"))'
	line_editor(line_to_edit, what_to_edit, the_edit)

	what_to_find = 'now.strftime(" %Y-%m-%d %H:%M:%S"))'
	what_to_add = '        #elsestatement\n'
	line_addition(what_to_find, what_to_add)

	point_mover()
t2_canvas.tag_bind(t2_shape1, "<Button-1>", t2_button1_code)

def t2_button2_code(self):
	canvas.create_polygon(t2_points2, outline='#000', fill='#003153', width=2)
t2_canvas.tag_bind(t2_shape2, "<Button-1>", t2_button2_code)

def t3_button1_code(self):
	t3_points1 = [20+point_adjustor, 20, 20+point_adjustor, 40, 40+point_adjustor, 60, 20+point_adjustor, 80, 20+point_adjustor, 100, 100+point_adjustor, 100, 100+point_adjustor, 20]
	canvas.create_polygon(t3_points1, outline='#000', fill='#00630d', width=2)

	what_to_find = 'now.strftime(" %Y-%m-%d %H:%M:%S"))'
	what_to_add = '\n    def stop(self):\n        pass\n'

	line_addition(what_to_find, what_to_add)

	point_mover()
t3_canvas.tag_bind(t3_shape1, "<Button-1>", t3_button1_code)

def t4_button1_code(self):
	canvas.create_polygon(t4_points1, outline='#000', fill='#7d12c4', width=2)

	to_replace = '#ifstatement'
	replacement = '        if variablename symbol userinput:\n'

	line_replece(to_replace,replacement)

	what_to_find = 'if variablename symbol userinput'
	what_to_add = '    '

	line_addition(what_to_find,what_to_add)

t4_canvas.tag_bind(t4_shape1, "<Button-1>", t4_button1_code)

def t5_button1_code(self):
	canvas.create_polygon(t5_points1, outline='#000', fill='#a6a005', width=2)

	line_to_edit = 'if variablename symbol userinput:'
	what_to_edit ='variablename symbol userinput:'
	the_edit = 'now.hour symbol user_input_hour and now.minute symbol user_input_minute:'

	line_editor(line_to_edit, what_to_edit, the_edit)
t5_canvas.tag_bind(t5_shape1, "<Button-1>", t5_button1_code)

def t5_button2_code(self):
	canvas.create_polygon(t5_points2, outline='#000', fill='#a6a005', width=2)

	user_inp = simpledialog.askstring("Time Input","Please enter time in HH:MM format")

	user_input_hour,user_input_minute = user_inp.split(':')

	if user_input_hour  is None:
		print ('Incorrect hour value')
		return 	

	elif user_input_minute is None:
		print ('Incorrect minute vlaue')
		return

	else: 

		line_to_edit = 'user_input_hour'
		what_to_edit ='user_input_hour'
		the_edit = user_input_hour

		line_editor(line_to_edit, what_to_edit, the_edit)

		line_to_edit = 'user_input_minute'
		what_to_edit ='user_input_minute'
		the_edit = user_input_minute

		line_editor(line_to_edit, what_to_edit, the_edit)
		
t5_canvas.tag_bind(t5_shape2, "<Button-1>", t5_button2_code)


root.mainloop()	