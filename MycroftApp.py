from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
from datetime import datetime, date
import os, subprocess, fileinput, subprocess

root = Tk()

root.title('Mycroft Skill Maker')
root.geometry("1125x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
##Sets up the main frame size and which direction it sticks to 
frame_canvas = Frame(root, width=800, height = 500)
frame_canvas.grid(sticky="E")

frame_canvas.grid_propagate(False)

canvas = Canvas(frame_canvas, width=1800, height=500, bg="white")

##Creates scroll buttons for the main canvas 
vsb = Scrollbar(frame_canvas, orient="horizontal", command=canvas.xview)
vsb.grid(row=0, column=1, sticky='n')
canvas.configure(xscrollcommand=vsb.set)
canvas.config(scrollregion=canvas.bbox("all"))

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

## Adjusts where a block will be placed according to other blocks 
#
# 260 is set as default as thats the size of the largest block. It is then adjusted based on each blocks input
point_adjustor = 0 
def point_mover(size_variant):
	global point_adjustor
	point_adjustor = point_adjustor + 260 + size_variant
	return 

## Is and elif statement block tally
#
# This is to allow statement blocks to get the current position of the statement and adjust accordingly to fit into correct slots 
statement_tally = 0 
def statement_block_tally(option):
	global statement_tally
	if option == 0: 
		statement_tally = statement_tally - 1
		return
	elif option == 1:
		statement_tally = statement_tally + 1
		return 

argument_point_adjustor = 0  
argument_block_tally = 0

## A point adjustor for Arguments 
#
# Option 0 the coordinates of where the argument block is placed is dependant on the current position of a Statement block and adjusts accordingly. Every 3 blocks the location resets
# Option 1 is for deleting of statement blocks
# Option 2 is for deleting argument blocks
def argument_point_mover(option):
	global argument_point_adjustor
	global argument_block_tally
	if option == 0:
		if statement_tally == 1 and argument_point_adjustor == 0 or argument_block_tally % 3 == 0:
			argument_point_adjustor = point_adjustor - 308 
			argument_block_tally = argument_block_tally + 1
			return
		else:
			argument_point_adjustor = argument_point_adjustor + 60 
			argument_block_tally = argument_block_tally + 1
			return	
	elif option == 1:		
		argument_point_adjustor = 0
		return
	elif option == 2:
		argument_point_adjustor = argument_point_adjustor - 60 
		argument_block_tally = argument_block_tally - 1
		return


## Finds a line and repleaces a specific part of it
def line_editor(line_to_edit, what_to_edit, the_edit):
	for import_line in fileinput.FileInput(folder_path.name, inplace=1):
		if line_to_edit in import_line:
			import_line = import_line.replace(what_to_edit,the_edit)
		print(import_line, end='')
	
## Replaces a line with a new line
def line_replece(to_replace, replacement):
	for function_line in fileinput.FileInput(folder_path.name, inplace=1):
		if to_replace in function_line:
			function_line = function_line.replace(function_line,replacement)
		print(function_line, end='')

## Finds a line and adds something to it or after it 
def line_addition(what_to_find, what_to_add):		
	for import_line in fileinput.FileInput(folder_path.name, inplace=1):
		if what_to_find in import_line:
			import_line = import_line.replace(import_line,import_line+what_to_add)
		print(import_line, end='')

## Deletes a line/specific part of a line
def line_deletion(delete_this):
	for function_line in fileinput.FileInput(folder_path.name, inplace=1):
		if delete_this in function_line:
			function_line = function_line.replace(function_line,'')
		print(function_line, end='')

date_variable_number = 0
def date_variable_counter(increase_number):
	global date_variable_number
	date_variable_number = date_variable_number + increase_number

and_or_var_number = 0
def and_or_counter(number_variation):
	global and_or_var_number
	and_or_var_number = and_or_var_number + number_variation

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
t1 = Frame(notebook, width=200, height=500)
t2 = Frame(notebook, width=200, height=500)
t3 = Frame(notebook, width=200, height=500)
t4 = Frame(notebook, width=200, height=500)
t5 = Frame(notebook, width=200, height=500)
t6 = Frame(root,width=1000, height=100)
t7 = Frame(root,width=125 , height= 100 )


# Creates the side tabs
notebook.add(t1, text='Imports       ')
notebook.add(t2, text='Functions    ')
notebook.add(t3, text='Argument    ')
notebook.add(t4, text='Response    ')
notebook.add(t5, text='Extension    ')


## Sets the specified UI position in the Y axis 
notebook.grid(column = 0, row = 0, sticky="W")
## The side tabs are chaned into canvases allowing shapes to be created on them. The canvas size and colour are set and tabs are assigned.
t1_canvas = Canvas(t1, width=200, height=500, bg='red')
t2_canvas = Canvas(t2, width=200, height=500, bg='yellow')
t3_canvas = Canvas(t3, width=200, height=500, bg='green')
t4_canvas = Canvas(t4, width=200, height=500, bg='#c313c3')
t5_canvas = Canvas(t5, width=200, height=500, bg='orange')
t6_canvas = Canvas(t6, width=1000, height=100, bg='blue')
t7_canvas = Canvas(t7, width=125, height=100, bg='white')

t1_canvas.grid(column = 0)
t2_canvas.grid(column = 0)
t3_canvas.grid(column = 0)
t4_canvas.grid(column = 0)
t5_canvas.grid(column = 0)
t6.grid(row=2, sticky="ES")
t6_canvas.grid(row = 2)
t7_canvas.grid(row=2, sticky="W")
t7.grid(row=2, sticky="W")

## The points represent the x and y axis of the canvas and each 2 points a point where the line stops.
## Eg if you take the first 6 points [20, 20, 20, 100, 100, 100]. This means the line starts at 20, 20 and goes to 20, 100 and from that point it turns to 100, 100 to make another point there
t1_block1 = PhotoImage(file="images/Imports/ImportDateTime.png")
## shape is created by taking the pre-established points and specifying the shape's border and inside colour as well as border width.
t1_shape1 = t1_canvas.create_image(100, 50, image = t1_block1)

t2_block1 = PhotoImage(file="images/Functions/GetCurrentTime.png")
t2_shape1 = t2_canvas.create_image(100, 50, image = t2_block1)

t2_block2 = PhotoImage(file="images/Functions/GetCurrentDate.png")
t2_shape2 = t2_canvas.create_image(100, 150, image = t2_block2)

t2_block3 = PhotoImage(file="images/Functions/GetCurrentDateTime.png")
t2_shape3 = t2_canvas.create_image(100, 250, image = t2_block3)

t3_row1_block1 = PhotoImage(file="images/Argument/Diamond/CurrentTimeDiamond.png")
t3_row1_shape1 = t3_canvas.create_image(50, 50, image = t3_row1_block1)

t3_row1_block2 = PhotoImage(file="images/Argument/Diamond/CurrentDateDiamond.png")
t3_row1_shape2 = t3_canvas.create_image(50, 100, image = t3_row1_block2)

t3_row1_block3 = PhotoImage(file="images/Argument/Diamond/CurrentDateAndTimeDiamond.png")
t3_row1_shape3 = t3_canvas.create_image(50, 150, image = t3_row1_block3)

t3_row2_block1 = PhotoImage(file="images/Argument/Pentagon/EqualToPentagon.png")
t3_row2_shape1 = t3_canvas.create_image(100, 50, image = t3_row2_block1)

t3_row2_block2 = PhotoImage(file="images/Argument/Pentagon/IsEqualToPentagon.png")
t3_row2_shape2 = t3_canvas.create_image(100, 100, image = t3_row2_block2)

t3_row2_block3 = PhotoImage(file="images/Argument/Pentagon/LessThanPentagon.png")
t3_row2_shape3 = t3_canvas.create_image(100, 150, image = t3_row2_block3)

t3_row2_block4 = PhotoImage(file="images/Argument/Pentagon/GreaterThanPentagon.png")
t3_row2_shape4 = t3_canvas.create_image(100, 200, image = t3_row2_block4)

t3_row2_block5 = PhotoImage(file="images/Argument/Pentagon/PlusPentagon.png")
t3_row2_shape5 = t3_canvas.create_image(100, 250, image = t3_row2_block5)

t3_row2_block6 = PhotoImage(file="images/Argument/Pentagon/MinusPentagon.png")
t3_row2_shape6 = t3_canvas.create_image(100, 300, image = t3_row2_block6)

t3_row2_block7 = PhotoImage(file="images/Argument/Pentagon/NotEqualToPentagon.png")
t3_row2_shape7 = t3_canvas.create_image(100, 350, image = t3_row2_block7)

t3_row3_block1 = PhotoImage(file="images/Argument/Hexagon/UserSetTimeHexagon.png")
t3_row3_shape1 = t3_canvas.create_image(150, 50, image = t3_row3_block1)

t3_row3_block2 = PhotoImage(file="images/Argument/Hexagon/UserSetDateHexagon.png")
t3_row3_shape2 = t3_canvas.create_image(150, 100, image = t3_row3_block2)

t3_row3_block3 = PhotoImage(file="images/Argument/Hexagon/UserSetDateAndTimeHexagon.png")
t3_row3_shape3 = t3_canvas.create_image(150, 150, image = t3_row3_block3)

t4_block1 = PhotoImage(file="images/Response/CustomResponseSentence.png")
t4_shape1 = t4_canvas.create_image(100, 50, image = t4_block1)

t4_block2 = PhotoImage(file="images/Response/CustomResponseOpenBrowser.png")
t4_shape2 = t4_canvas.create_image(100, 150, image = t4_block2)

t5_block1 = PhotoImage(file="images/Extensions/AndExtension.png")
t5_shape1 = t5_canvas.create_image(100, 50, image = t5_block1)

t5_block2 = PhotoImage(file="images/Extensions/OrExtension.png")
t5_shape2 = t5_canvas.create_image(100, 150, image = t5_block2)

t6_block1 = PhotoImage(file="images/Statement/IfStatement.png")
t6_shape1 = t6_canvas.create_image(150, 50, image = t6_block1)

t6_block2 = PhotoImage(file="images/Statement/ElIfStatement.png")
t6_shape2 = t6_canvas.create_image(420, 50, image = t6_block2)

t6_block3 = PhotoImage(file="images/Statement/ElseStatement.png")
t6_shape3 = t6_canvas.create_image(605, 50, image = t6_block3)

t6_block4 = PhotoImage(file="images/Statement/EmptyStatement.png")
t6_shape4 = t6_canvas.create_image(800, 50, image = t6_block4)

t7_overlay = PhotoImage(file="images/Statement.png")
t7_canvas.create_image(62, 50, image = t7_overlay)

canvas.grid(row = 0, column = 0, columnspan = 8, rowspan = 8, stick='NE')




def t1_button1_code(self):

	global t1_shape1_on_canvas

	t1_points1_on_canvas = [70+point_adjustor, 250]
	t1_shape1_on_canvas = canvas.create_image(t1_points1_on_canvas, image = t1_block1)

	line_addition('from mycroft import MycroftSkill, intent_file_handler','from adapt.intent import IntentBuilder \nfrom datetime import datetime, date\n')

	point_mover(-180)

t1_canvas.tag_bind(t1_shape1, "<Button-1>", t1_button1_code)

def t1_button1_removal(self):
	
	line_deletion('from adapt.intent import IntentBuilder')
	line_deletion('import datetime')

	canvas.delete(t1_shape1_on_canvas)

	point_mover(-340)

t1_canvas.tag_bind(t1_shape1, "<Button-3>", t1_button1_removal)

def t2_button1_code(self):

	global t2_shape1_on_canvas

	t2_points1_on_canvas = [70+point_adjustor, 250]
	t2_shape1_on_canvas = canvas.create_image(t2_points1_on_canvas, image = t2_block1)

	line_addition('self.speak_dialog(', '        now = datetime.now().time()\n        #ifstatement\n')

	point_mover(-171)

t2_canvas.tag_bind(t2_shape1, "<Button-1>", t2_button1_code)

def t2_button1_removal(self):
	
	line_deletion('now = datetime.now().time()')
	line_deletion('#ifstatement')

	canvas.delete(t2_shape1_on_canvas)

	point_mover(-349)

t2_canvas.tag_bind(t2_shape1, "<Button-3>", t2_button1_removal)

def t2_button2_code(self):

	global t2_shape2_on_canvas

	t2_points2_on_canvas = [70+point_adjustor, 250]
	t2_shape2_on_canvas = canvas.create_image(t2_points2_on_canvas, image = t2_block2)

	line_addition('self.speak_dialog(', '        CurrentDate = date.today()\n        #dateprep\n        #ifstatement\n')

	point_mover(-171)
t2_canvas.tag_bind(t2_shape2, "<Button-1>", t2_button2_code)	

def t2_button2_removal(self):
	
	line_deletion('CurrentDate = date.today()')
	line_deletion('#dateprep')
	line_deletion('#ifstatement')

	canvas.delete(t2_shape2_on_canvas)
	point_mover(-349)

t2_canvas.tag_bind(t2_shape2, "<Button-3>", t2_button2_removal)

def t2_button3_code(self):

	global t2_shape3_on_canvas

	t2_points3_on_canvas = [70+point_adjustor, 250]
	t2_shape3_on_canvas = canvas.create_image(t2_points3_on_canvas, image = t2_block3)

	line_addition('self.speak_dialog(', '        CurrentDate = date.today()\n        now = datetime.now().time()\n        #dateprep\n        #ifstatement\n')

	point_mover(-171)
t2_canvas.tag_bind(t2_shape3, "<Button-1>", t2_button3_code)	

def t2_button3_removal(self):
	
	line_deletion('CurrentDate = date.today()')
	line_deletion('now = datetime.now().time()')
	line_deletion('#dateprep')
	line_deletion('#ifstatement')

	canvas.delete(t2_shape3_on_canvas)
	point_mover(-349)

t2_canvas.tag_bind(t2_shape3, "<Button-3>", t2_button3_removal)

def t3_row1_button1_code(self):

	argument_point_mover(0)

	global t3_row1_shape1_on_canvas

	t3_row1_points1_on_canvas = [150+argument_point_adjustor, 250]
	t3_row1_shape1_on_canvas = canvas.create_image(t3_row1_points1_on_canvas, image = t3_row1_block1)

	line_to_edit = 'variablename symbol userinput:'
	what_to_edit ='variablename symbol userinput:'
	the_edit = 'now.hour symbol user_input_hour and now.minute symbol user_input_minute:'
	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row1_shape1, "<Button-1>", t3_row1_button1_code)

def t3_row1_button1_removal(self):
	
	argument_point_mover(2)

	line_to_edit = 'now.hour symbol user_input_hour and now.minute symbol user_input_minute:'
	what_to_edit ='now.hour symbol user_input_hour and now.minute symbol user_input_minute:'
	the_edit = 'variablename symbol userinput'
	line_editor(line_to_edit, what_to_edit, the_edit)

	canvas.delete(t3_row1_shape1_on_canvas)

t3_canvas.tag_bind(t3_row1_shape1, "<Button-3>", t3_row1_button1_removal)

def t3_row1_button2_code(self):

	argument_point_mover(0)

	global t3_row1_shape2_on_canvas

	t3_row1_points2_on_canvas = [150+argument_point_adjustor, 250]
	t3_row1_shape2_on_canvas = canvas.create_image(t3_row1_points2_on_canvas, image = t3_row1_block2)

	line_editor('variablename symbol userinput:', 'variablename', 'CurrentDate')

t3_canvas.tag_bind(t3_row1_shape2, "<Button-1>", t3_row1_button2_code)

def t3_row1_button2_removal(self):
	
	argument_point_mover(2)

	line_editor('CurrentDate symbol userinput', 'CurrentDate', 'variablename')

	canvas.delete(t3_row1_shape2_on_canvas)

t3_canvas.tag_bind(t3_row1_shape2, "<Button-3>", t3_row1_button2_removal)


def t3_row1_button3_code(self):

	argument_point_mover(0)

	global t3_row1_shape3_on_canvas	

	t3_row1_points3_on_canvas = [150+argument_point_adjustor, 250]
	t3_row1_shape3_on_canvas = canvas.create_image(t3_row1_points3_on_canvas, image = t3_row1_block3)

	line_to_edit = 'variablename symbol userinput:'
	what_to_edit ='variablename'
	the_edit = 'now.hour symbol user_input_hour and now.minute symbol user_input_minute and CurrentDate'
	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row1_shape3, "<Button-1>", t3_row1_button3_code)

def t3_row1_button3_removal(self):
	
	argument_point_mover(2)

	line_to_edit = 'now.hour symbol user_input_hour and now.minute symbol user_input_minute and CurrentDate'
	what_to_edit ='now.hour symbol user_input_hour and now.minute symbol user_input_minute and CurrentDate'
	the_edit = 'variablename'
	line_editor(line_to_edit, what_to_edit, the_edit)

	canvas.delete(t3_row1_shape3_on_canvas)

t3_canvas.tag_bind(t3_row1_shape3, "<Button-3>", t3_row1_button3_removal)

def t3_row2_button1_code(self):

	argument_point_mover(0)

	global t3_row2_shape1_on_canvas	

	t3_row2_points1_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape1_on_canvas = canvas.create_image(t3_row2_points1_on_canvas, image = t3_row2_block1)

	line_editor('symbol', 'symbol', '==')

t3_canvas.tag_bind(t3_row2_shape1, "<Button-1>", t3_row2_button1_code)

def t3_row2_button1_removal(self):
	
	argument_point_mover(2)

	line_editor('==', '==', 'symbol')

	canvas.delete(t3_row2_shape1_on_canvas)

t3_canvas.tag_bind(t3_row2_shape1, "<Button-3>", t3_row2_button1_removal)

def t3_row2_button2_code(self):

	argument_point_mover(0)

	global t3_row2_shape2_on_canvas	

	t3_row2_points2_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape2_on_canvas = canvas.create_image(t3_row2_points2_on_canvas, image = t3_row2_block2)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '='

	line_editor('symbol', 'symbol', '=')


t3_canvas.tag_bind(t3_row2_shape2, "<Button-1>", t3_row2_button2_code)

def t3_row2_button2_removal(self):
	
	argument_point_mover(2)

	line_editor('=', '=', 'symbol')

	canvas.delete(t3_row2_shape2_on_canvas)

t3_canvas.tag_bind(t3_row2_shape2, "<Button-3>", t3_row2_button2_removal)

def t3_row2_button3_code(self):

	argument_point_mover(0)

	global t3_row2_shape3_on_canvas

	t3_row2_points3_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape3_on_canvas = canvas.create_image(t3_row2_points3_on_canvas, image = t3_row2_block3)

	line_editor('symbol', 'symbol', '<')


t3_canvas.tag_bind(t3_row2_shape3, "<Button-1>", t3_row2_button3_code)

def t3_row2_button3_removal(self):
	
	argument_point_mover(2)

	line_editor('<', '<', 'symbol')

	canvas.delete(t3_row2_shape3_on_canvas)

t3_canvas.tag_bind(t3_row2_shape3, "<Button-3>", t3_row2_button3_removal)

def t3_row2_button4_code(self):

	argument_point_mover(0)

	global t3_row2_shape4_on_canvas

	t3_row2_points4_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape4_on_canvas = canvas.create_image(t3_row2_points4_on_canvas, image = t3_row2_block4)

	line_editor('symbol', 'symbol', '>')


t3_canvas.tag_bind(t3_row2_shape4, "<Button-1>", t3_row2_button4_code)

def t3_row2_button4_removal(self):
	
	argument_point_mover(2)

	line_editor('>', '>', 'symbol')

	canvas.delete(t3_row2_shape4_on_canvas)

t3_canvas.tag_bind(t3_row2_shape4, "<Button-3>", t3_row2_button4_removal)

def t3_row2_button5_code(self):

	argument_point_mover(0)

	global t3_row2_shape5_on_canvas

	t3_row2_points5_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape5_on_canvas = canvas.create_image(t3_row2_points5_on_canvas, image = t3_row2_block5)

	line_editor('symbol', 'symbol', '+')


t3_canvas.tag_bind(t3_row2_shape5, "<Button-1>", t3_row2_button5_code)

def t3_row2_button5_removal(self):
	
	argument_point_mover(2)

	line_editor('+', '+', 'symbol')

	canvas.delete(t3_row2_shape5_on_canvas)

t3_canvas.tag_bind(t3_row2_shape5, "<Button-3>", t3_row2_button5_removal)

def t3_row2_button6_code(self):

	argument_point_mover(0)

	global t3_row2_shape6_on_canvas

	t3_row2_points6_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape6_on_canvas = canvas.create_image(t3_row2_points6_on_canvas, image = t3_row2_block6)

	line_editor('symbol', 'symbol', '-')


t3_canvas.tag_bind(t3_row2_shape6, "<Button-1>", t3_row2_button6_code)

def t3_row2_button6_removal(self):
	
	argument_point_mover(2)

	line_editor('-', '-', 'symbol')

	canvas.delete(t3_row2_shape6_on_canvas)

t3_canvas.tag_bind(t3_row2_shape6, "<Button-3>", t3_row2_button6_removal)

def t3_row2_button7_code(self):

	argument_point_mover(0)

	global t3_row2_shape7_on_canvas

	t3_row2_points7_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape7_on_canvas = canvas.create_image(t3_row2_points7_on_canvas, image = t3_row2_block7)

	line_editor('symbol', 'symbol', '!=')

t3_canvas.tag_bind(t3_row2_shape7, "<Button-1>", t3_row2_button7_code)

def t3_row2_button7_removal(self):
	
	argument_point_mover(2)

	line_editor('!=', '!=', 'symbol')

	canvas.delete(t3_row2_shape7_on_canvas)

t3_canvas.tag_bind(t3_row2_shape7, "<Button-3>", t3_row2_button7_removal)

def t3_row3_button1_code(self):

	global t3_row3_shape1_on_canvas
	global t3_row3_shape1_user_input_hour
	global t3_row3_shape1_user_input_minute


	t3_row3_shape1_user_input = simpledialog.askstring("Time Input","Please enter time in HH:MM format")

	if t3_row3_shape1_user_input is None:
		return

	else:
		if t3_row3_shape1_user_input is '':
			messagebox.showerror(title='No input', message='No input was given')
			return

		t3_row3_shape1_user_input_hour,t3_row3_shape1_user_input_minute = t3_row3_shape1_user_input.split(':')

		if t3_row3_shape1_user_input_hour.isnumeric() == False:
			messagebox.showerror(title="Incorrect Hour", message="Hour field contains non numerical characters")
			return 	

		elif t3_row3_shape1_user_input_minute.isnumeric() == False:
			messagebox.showerror(title="Incorrect Minute", message="Minute field contains non numerical characters")
			return

		else: 
	
			argument_point_mover(0)

			t3_row3_points1_on_canvas = [150+argument_point_adjustor, 250]
			t3_row3_shape1_on_canvas = canvas.create_image(t3_row3_points1_on_canvas, image = t3_row3_block1)

			t3_row3_shape1_user_input_hour,t3_row3_shape1_user_input_minute = t3_row3_shape1_user_input.split(':')
			line_editor('user_input_hour', 'user_input_hour', t3_row3_shape1_user_input_hour)
			line_editor('user_input_minute', 'user_input_minute', t3_row3_shape1_user_input_minute)

t3_canvas.tag_bind(t3_row3_shape1, "<Button-1>", t3_row3_button1_code)

def t3_row3_button1_removal(self):
	
	argument_point_mover(2)

	line_editor(t3_row3_shape1_user_input_hour, t3_row3_shape1_user_input_hour, 'user_input_hour')
	line_editor(t3_row3_shape1_user_input_minute, t3_row3_shape1_user_input_minute, 'user_input_minute')

	canvas.delete(t3_row3_shape1_on_canvas)

t3_canvas.tag_bind(t3_row3_shape1, "<Button-3>", t3_row3_button1_removal)

def t3_row3_button2_code(self):

	global t3_row3_shape2_on_canvas
	global t3_row3_shape2_user_input_date

	t3_row3_shape2_user_input_date = simpledialog.askstring("Date Input","Please enter the date in a DD-MM-YYYY format")

	if t3_row3_shape2_user_input_date is None:
		return

	else:
		if t3_row3_shape2_user_input_date is '':
			messagebox.showerror(title="Incorrect Date", message="No date was given")
			return		

		else:
			argument_point_mover(0)

			date_variable_counter(1)
			date_variable_number_str = str(date_variable_number)

			t3_row3_points2_on_canvas = [150+argument_point_adjustor, 250]
			t3_row3_shape2_on_canvas = canvas.create_image(t3_row3_points2_on_canvas, image = t3_row3_block1)

			to_replace = '#dateprep'
			replacement = '        user_input_date'+date_variable_number_str+' = "DayMonthYear"\n        InputDate'+date_variable_number_str+' = datetime.strptime(user_input_date'+date_variable_number_str+', "%d-%m-%Y")\n        InputDate'+date_variable_number_str+' = InputDate'+date_variable_number_str+'.date()\n        #dateprep\n'

			line_replece(to_replace,replacement)

			line_editor('user_input_date'+date_variable_number_str+' = "DayMonthYear"', 'DayMonthYear', t3_row3_shape2_user_input_date)
			line_editor('userinput', 'userinput', 'InputDate'+date_variable_number_str)

t3_canvas.tag_bind(t3_row3_shape2, "<Button-1>", t3_row3_button2_code)

def t3_row3_button2_removal(self):
	
	argument_point_mover(2)

	date_variable_counter(-1)
	date_variable_number_str = str(date_variable_number)	

	to_replace ='         user_input_date'+date_variable_number_str+' = "DayMonthYear"\n        InputDate'+date_variable_number_str+' = datetime.strptime(user_input_date'+date_variable_number_str+', "%d-%m-%Y")\n        InputDate'+date_variable_number_str+' = InputDate'+date_variable_number_str+'.date()\n'
	replacement = '#dateprep'
	line_replece(to_replace,replacement)

	line_editor(user_input_date, user_input_date, 'DayMonthYear')
	line_editor('InputDate'+date_variable_number_str, 'InputDate'+date_variable_number_str, 'userinput')	

	canvas.delete(t3_row3_shape2_on_canvas)

t3_canvas.tag_bind(t3_row3_shape2, "<Button-3>", t3_row3_button2_removal)

def t3_row3_button3_code(self):

	argument_point_mover(0)

	date_variable_counter(1)
	date_variable_number_str = str(date_variable_number)

	global t3_row3_shape3_on_canvas
	global t3_row3_shape3_user_input_minute
	global t3_row3_shape3_user_input_hour
	global t3_row3_shape3_user_input_date


	t3_row3_shape3_user_input_time = simpledialog.askstring("Time Input","Please enter time in HH:MM format")
	t3_row3_shape3_user_input_date = simpledialog.askstring("Date Input","Please enter the date in a DD-MM-YYYY format")
	
	if t3_row3_shape3_user_input_time or t3_row3_shape3_user_input_date is None:
		return

	else:
		if t3_row3_shape3_user_input_time is '':
			messagebox.showerror(title='No time input', message='No time input was given')
			return

		elif t3_row3_shape3_user_input_date is '':
			messagebox.showerror(title='No date input', message='No date input was given')
			return	

		t3_row3_shape3_user_input_hour,t3_row3_shape3_user_input_minute = t3_row3_shape3_user_input_time.split(':')

		if t3_row3_shape3_user_input_hour.isnumeric() == False:
			print ('Incorrect hour value')
			return 	

		elif t3_row3_shape3_user_input_minute.isnumeric() == False:
			print ('Incorrect minute value')
			return

		else: 

			t3_row3_points3_on_canvas = [150+argument_point_adjustor, 250]
			t3_row3_shape3_on_canvas = canvas.create_image(t3_row3_points3_on_canvas, image = t3_row3_block3)

			line_editor('user_input_hour', 'user_input_hour', t3_row3_shape3_user_input_hour)
			line_editor('user_input_minute', 'user_input_minute', t3_row3_shape3_user_input_minute)

			to_replace = '#dateprep'
			replacement = '        user_input_date'+date_variable_number_str+' = "DayMonthYear"\n        InputDate'+date_variable_number_str+' = datetime.strptime(user_input_date'+date_variable_number_str+', "%d-%m-%Y")\n        InputDate'+date_variable_number_str+' = InputDate'+date_variable_number_str+'.date()\n        #dateprep\n'

			line_replece(to_replace,replacement)

			line_editor('user_input_date'+date_variable_number_str+' = "DayMonthYear"', 'DayMonthYear', t3_row3_shape3_user_input_date)
			line_editor('userinput', 'userinput', 'InputDate'+date_variable_number_str)

t3_canvas.tag_bind(t3_row3_shape3, "<Button-1>", t3_row3_button3_code)


def t3_row3_button3_removal(self):

	argument_point_mover(2)

	line_editor(t3_row3_shape3_user_input_hour, t3_row3_shape3_user_input_hour, 'user_input_hour')
	line_editor(t3_row3_shape3_user_input_minute, t3_row3_shape3_user_input_minute, 'user_input_minute')

	to_replace ='         user_input_date'+date_variable_number_str+' = "DayMonthYear"\n        InputDate'+date_variable_number_str+' = datetime.strptime(user_input_date'+date_variable_number_str+', "%d-%m-%Y")\n        InputDate'+date_variable_number_str+' = InputDate'+date_variable_number_str+'.date()\n'
	replacement = '#dateprep'
	line_replece(to_replace,replacement)

	line_editor(t3_row3_shape3_user_input_date, t3_row3_shape3_user_input_date, 'DayMonthYear')
	line_editor('InputDate'+date_variable_number_str, 'InputDate'+date_variable_number_str, 'userinput')	

	canvas.delete(t3_row3_shape3_on_canvas)

t3_canvas.tag_bind(t3_row3_shape3, "<Button-3>", t3_row3_button3_removal)

def t4_button1_code(self):
	
	global t4_shape1_on_canvas
	global t4_button1_user_input

	t4_button1_user_input = simpledialog.askstring("Sentance Response","Please enter your dialog")

	if t4_button1_user_input is None:
		return

	else:
		t4_points1_on_canvas = [70+point_adjustor, 250]
		t4_shape1_on_canvas = canvas.create_image(t4_points1_on_canvas, image = t4_block1)

		line_replece('#response','           self.speak_dialog("DialogResponse")\n')

		line_addition('self.speak_dialog("DialogResponse")','           #response\n')

		line_editor('self.speak_dialog("DialogResponse")', 'DialogResponse', t4_button1_user_input)

		point_mover(-171)

t4_canvas.tag_bind(t4_shape1, "<Button-1>", t4_button1_code)

def t4_button1_removal(self):
	
	line_deletion(t4_button1_user_input)
	line_deletion('self.speak_dialog("")')

	canvas.delete(t4_shape1_on_canvas)

	point_mover(-349)

t4_canvas.tag_bind(t4_shape1, "<Button-3>", t4_button1_removal)

def t4_button2_code(self):

	global t4_shape2_on_canvas
	global t4_button2_user_input

	t4_button2_user_input = simpledialog.askstring("Sentance Response","Please enter the website url (include https://)")

	if t4_button2_user_input is None:
		return

	else:
		t4_points_on_canvas = [70+point_adjustor, 250]
		t4_shape2_on_canvas = canvas.create_image(t4_points_on_canvas, image = t4_block2)

		if t4_button2_user_input  == "":
			t4_button2_user_input = 'https://' 
	
		line_addition('from mycroft import MycroftSkill, intent_file_handler','import webbrowser\n')
	
		line_replece('#response','           webbrowser.open("url", new=2)\n')

		line_editor('webbrowser.open("url", new=2)', 'url', t4_button2_user_input)

		line_addition('webbrowser.open("'+t4_button2_user_input+'"','           #response\n')

		point_mover(-171)
t4_canvas.tag_bind(t4_shape2, "<Button-1>", t4_button2_code)

def t4_button2_removal(self):
	
	line_deletion('import webbrowser')
	line_deletion('webbrowser.open("'+t4_button2_user_input+'", new=2)')

	canvas.delete(t4_shape2_on_canvas)

	point_mover(-349)

t4_canvas.tag_bind(t4_shape2, "<Button-3>", t4_button2_removal)

def t5_button1_code(self):

	global t5_shape1_on_canvas

	and_or_var_number_str = str(and_or_var_number)

	t5_points1_on_canvas = [70+point_adjustor, 250]
	t5_shape1_on_canvas = canvas.create_image(t5_points1_on_canvas, image = t5_block1)

	line_editor(': #AndOrExtension'+and_or_var_number_str, ': #AndOrExtension'+and_or_var_number_str, ' and #EmptyStatement:')

	point_mover(-173)
t5_canvas.tag_bind(t5_shape1, "<Button-1>", t5_button1_code)

def t5_button1_removal(self):
	
	and_or_var_number_str = str(and_or_var_number)

	line_editor('and #EmptyStatement:', 'and #EmptyStatement:', ': #AndOrExtension'+and_or_var_number_str)

	canvas.delete(t5_shape1_on_canvas)

	point_mover(-347)
t5_canvas.tag_bind(t5_shape1, "<Button-3>", t5_button1_removal)

def t5_button2_code(self):

	statement_block_tally(1)

	and_or_var_number_str = str(and_or_var_number)

	global t5_shape2_on_canvas

	t5_points2_on_canvas = [70+point_adjustor, 250]
	t5_shape2_on_canvas = canvas.create_image(t5_points2_on_canvas, image = t5_block2)

	line_editor(': #AndOrExtension'+and_or_var_number_str, ': #AndOrExtension'+and_or_var_number_str, ' or #EmptyStatement:')

	point_mover(-173)
t5_canvas.tag_bind(t5_shape2, "<Button-1>", t5_button2_code)

def t5_button2_removal(self):
	
	and_or_var_number_str = str(and_or_var_number)

	line_editor('or #EmptyStatement:', 'or #EmptyStatement:', ': #AndOrExtension'+and_or_var_number_str)

	canvas.delete(t5_shape2_on_canvas)

	point_mover(-347)
t5_canvas.tag_bind(t5_shape2, "<Button-3>", t5_button2_removal)

def t6_button1_code(self):

	statement_block_tally(1)
	and_or_counter(1)

	and_or_var_number_str = str(and_or_var_number)

	global t6_shape1_on_canvas

	t6_points1_on_canvas = [150+point_adjustor, 250]
	t6_shape1_on_canvas = canvas.create_image(t6_points1_on_canvas, image = t6_block1)

	line_replece('#ifstatement','        if variablename symbol userinput: #AndOrExtension'+and_or_var_number_str+'\n')

	line_addition('if variablename symbol userinput','        #elsestatement\n')

	line_addition('        if variablename symbol userinput:','            #response\n')

	point_mover(-11)
t6_canvas.tag_bind(t6_shape1, "<Button-1>", t6_button1_code)

def t6_button1_removal(self):
	
	statement_block_tally(0)
	argument_point_mover(1)

	and_or_var_number_str = str(and_or_var_number)

	line_replece('if variablename symbol userinput: #AndOrExtension'+and_or_var_number_str,'        #ifstatement\n')

	and_or_counter(-1)

	line_deletion('#elsestatement')

	line_deletion('#response')

	canvas.delete(t6_shape1_on_canvas)

	point_mover(-509)
t6_canvas.tag_bind(t6_shape1, "<Button-3>", t6_button1_removal)

def t6_button2_code(self):

	statement_block_tally(1)
	and_or_counter(1)

	and_or_var_number_str = str(and_or_var_number)

	global t6_shape2_on_canvas

	t6_points_on_canvas = [150+point_adjustor, 250]
	t6_shape2_on_canvas = canvas.create_image(t6_points_on_canvas, image = t6_block2)

	line_deletion('#response')

	line_replece('#elsestatement','        elif variablename symbol userinput: #AndOrExtension'+and_or_var_number_str+'\n')

	line_addition('elif variablename symbol userinput','        #elsestatement\n')

	line_addition('elif variablename symbol userinput:','           #response\n')

	point_mover(-11)
t6_canvas.tag_bind(t6_shape2, "<Button-1>", t6_button2_code)

def t6_button2_removal(self):
	
	statement_block_tally(0)
	argument_point_mover(1)

	and_or_var_number_str = str(and_or_var_number)

	line_deletion('#response')

	line_replece('elif variablename symbol userinput: #AndOrExtension'+and_or_var_number_str,'        #response\n')

	and_or_counter(-1)

	canvas.delete(t6_shape2_on_canvas)

	point_mover(-509)
t6_canvas.tag_bind(t6_shape2, "<Button-3>", t6_button2_removal)

def t6_button3_code(self):

	statement_block_tally(1)

	global t6_shape3_on_canvas

	t6_points3_on_canvas = [70+point_adjustor, 250]
	t6_shape3_on_canvas = canvas.create_image(t6_points3_on_canvas, image = t6_block3)

	line_deletion('#response')	

	line_replece('#elsestatement','        else:\n')

	line_addition('else:','    #response')

	point_mover(-171)
t6_canvas.tag_bind(t6_shape3, "<Button-1>", t6_button3_code)

def t6_button3_removal(self):
	
	statement_block_tally(0)
	argument_point_mover(1)

	line_deletion('#response')

	line_replece('else:','       #response\n       #elsestatement\n')

	canvas.delete(t6_shape3_on_canvas)

	point_mover(-349)
t6_canvas.tag_bind(t6_shape3, "<Button-3>", t6_button3_removal)

def t6_button4_code(self):

	statement_block_tally(1)

	global t6_shape4_on_canvas

	t6_points_on_canvas = [150+point_adjustor, 250]
	t6_shape4_on_canvas = canvas.create_image(t6_points_on_canvas, image = t6_block4)

	line_editor('#EmptyStatement', '#EmptyStatement', 'variablename symbol userinput')

	point_mover(-11)
t6_canvas.tag_bind(t6_shape4, "<Button-1>", t6_button4_code)

def t6_button4_removal(self):
	
	statement_block_tally(0)
	argument_point_mover(1)

	line_editor('variablename symbol userinput', 'variablename symbol userinput', '#EmptyStatement')

	canvas.delete(t6_shape4_on_canvas)

	point_mover(-509)
t6_canvas.tag_bind(t6_shape4, "<Button-3>", t6_button4_removal)

root.mainloop()	