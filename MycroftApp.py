from tkinter import * 
from tkinter import ttk
from tkinter import filedialog
from tkinter import simpledialog
from datetime import datetime, date
import os, subprocess, fileinput, subprocess

root = Tk()

root.title('Mycroft Skill Maker')
root.geometry("1125x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
##Sets up the main canvas size and colour
frame_canvas = Frame(root, width=800, height = 500)
frame_canvas.grid(sticky="E")
#frame_canvas.columnconfigure(0, weight=1)
#frame_canvas.rowconfigure(0, weight=1)
frame_canvas.grid_propagate(False)

canvas = Canvas(frame_canvas, width=1800, height=500, bg="white")

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

point_adjustor = 0 
def point_mover(size_variant):
	global point_adjustor
	point_adjustor = point_adjustor + 260 + size_variant
	return 

statement_tally = 0 
def statement_block_tally():
	global statement_tally
	statement_tally = statement_tally + 1
	return 

argument_point_adjustor = 0  
argument_block_tally = 0
def argument_point_mover():
	global argument_point_adjustor
	global argument_block_tally
	if statement_tally == 1 and argument_point_adjustor == 0 or argument_block_tally % 3 == 0:
		argument_point_adjustor = point_adjustor - 308 
		argument_block_tally = argument_block_tally + 1
	else:
		argument_point_adjustor = argument_point_adjustor + 60 
		argument_block_tally = argument_block_tally + 1
	return	

def argument_point_remover():
	argument_point_adjustor = argument_point_adjustor - 60 
	argument_block_tally = argument_block_tally - 1
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
t1 = Frame(notebook, width=200, height=500)
t2 = Frame(notebook, width=200, height=500)
t3 = Frame(notebook, width=200, height=500)
t4 = Frame(notebook, width=200, height=500)
t5 = Frame(root,width=1000, height=100, bg='blue')
t5.grid(row=2, sticky="ES")
t6 = Frame(root,width=125 , height= 100 )
t6.grid(row=2, sticky="W")



#t6_bg = PhotoImage(file="images/Statement.png")
# Creates the side tabs
notebook.add(t1, text='Imports       ')
notebook.add(t2, text='Functions    ')
notebook.add(t3, text='Argument    ')
notebook.add(t4, text='Response    ')

#notebook.add(t6, text='Statement ')
## Sets the specified UI position in the Y axis 
notebook.grid(column = 0, row = 0, sticky="W")
## The side tabs are chaned into canvases allowing shapes to be created on them. The canvas size and colour are set and tabs are assigned.
t1_canvas = Canvas(t1, width=200, height=500, bg='red')
t2_canvas = Canvas(t2, width=200, height=500, bg='yellow')
t3_canvas = Canvas(t3, width=200, height=500, bg='green')
t4_canvas = Canvas(t4, width=200, height=500, bg='#c313c3')
t5_canvas = Canvas(t5, width=1000, height=100, bg='blue')
t6_canvas = Canvas(t6, width=125, height=100, bg='white')
t6_canvas.grid(row=2, sticky="W")
#t6_canvas = Canvas(t6, width=1200, height=50, bg='blue')
## The points represent the x and y axis of the canvas and each 2 points a point where the line stops.
## Eg if you take the first 6 points [20, 20, 20, 100, 100, 100]. This means the line starts at 20, 20 and goes to 20, 100 and from that point it turns to 100, 100 to make another point there
t1_block1 = PhotoImage(file="images/Imports/ImportDateTime.png")
## shape is created by taking the pre-established points and specifying the shape's border and inside colour as well as border width.
t1_shape1 = t1_canvas.create_image(100, 50, image = t1_block1)
t1_canvas.grid(column = 0)

t2_block1 = PhotoImage(file="images/Functions/GetCurrentTime.png")
t2_shape1 = t2_canvas.create_image(100, 50, image = t2_block1)
t2_canvas.grid(column = 0)

t2_block2 = PhotoImage(file="images/Functions/GetCurrentDate.png")
t2_shape2 = t2_canvas.create_image(100, 150, image = t2_block2)
t2_canvas.grid(column = 0)

t3_row1_block1 = PhotoImage(file="images/Argument/Diamond/CurrentTimeDiamond.png")
t3_row1_shape1 = t3_canvas.create_image(50, 50, image = t3_row1_block1)
t3_canvas.grid(column = 0)

t3_row1_block2 = PhotoImage(file="images/Argument/Diamond/CurrentDateDiamond.png")
t3_row1_shape2 = t3_canvas.create_image(50, 100, image = t3_row1_block2)
t3_canvas.grid(column = 0)

t3_row1_block3 = PhotoImage(file="images/Argument/Diamond/CurrentDateAndTimeDiamond.png")
t3_row1_shape3 = t3_canvas.create_image(50, 150, image = t3_row1_block3)
t3_canvas.grid(column = 0)

t3_row2_block1 = PhotoImage(file="images/Argument/Pentagon/EqualToPentagon.png")
t3_row2_shape1 = t3_canvas.create_image(100, 50, image = t3_row2_block1)
t3_canvas.grid(column = 0)

t3_row2_block2 = PhotoImage(file="images/Argument/Pentagon/IsEqualToPentagon.png")
t3_row2_shape2 = t3_canvas.create_image(100, 100, image = t3_row2_block2)
t3_canvas.grid(column = 0)

t3_row2_block3 = PhotoImage(file="images/Argument/Pentagon/LessThanPentagon.png")
t3_row2_shape3 = t3_canvas.create_image(100, 150, image = t3_row2_block3)
t3_canvas.grid(column = 0)

t3_row2_block4 = PhotoImage(file="images/Argument/Pentagon/GreaterThanPentagon.png")
t3_row2_shape4 = t3_canvas.create_image(100, 200, image = t3_row2_block4)
t3_canvas.grid(column = 0)

t3_row2_block5 = PhotoImage(file="images/Argument/Pentagon/PlusPentagon.png")
t3_row2_shape5 = t3_canvas.create_image(100, 250, image = t3_row2_block5)
t3_canvas.grid(column = 0)

t3_row2_block6 = PhotoImage(file="images/Argument/Pentagon/MinusPentagon.png")
t3_row2_shape6 = t3_canvas.create_image(100, 300, image = t3_row2_block6)
t3_canvas.grid(column = 0)

t3_row2_block7 = PhotoImage(file="images/Argument/Pentagon/NotEqualToPentagon.png")
t3_row2_shape7 = t3_canvas.create_image(100, 350, image = t3_row2_block7)
t3_canvas.grid(column = 0)

t3_row3_block1 = PhotoImage(file="images/Argument/Hexagon/UserSetTimeHexagon.png")
t3_row3_shape1 = t3_canvas.create_image(150, 50, image = t3_row3_block1)
t3_canvas.grid(column = 0)

t3_row3_block2 = PhotoImage(file="images/Argument/Hexagon/UserSetDateHexagon.png")
t3_row3_shape2 = t3_canvas.create_image(150, 100, image = t3_row3_block2)
t3_canvas.grid(column = 0)

t3_row3_block3 = PhotoImage(file="images/Argument/Hexagon/UserSetDateAndTimeHexagon.png")
t3_row3_shape3 = t3_canvas.create_image(150, 150, image = t3_row3_block3)
t3_canvas.grid(column = 0)

t4_block1 = PhotoImage(file="images/Response/CustomResponseSentence.png")
t4_shape1 = t4_canvas.create_image(100, 50, image = t4_block1)
t4_canvas.grid(column = 0)

t4_block2 = PhotoImage(file="images/Response/CustomResponseOpenBrowser.png")
t4_shape2 = t4_canvas.create_image(100, 150, image = t4_block2)
t4_canvas.grid(column = 0)

t5_block1 = PhotoImage(file="images/Statement/IfStatement.png")
t5_shape1 = t5_canvas.create_image(150, 50, image = t5_block1)
t5_canvas.grid(row = 2)

t5_block2 = PhotoImage(file="images/Statement/ElIfStatement.png")
t5_shape2 = t5_canvas.create_image(420, 50, image = t5_block2)
t5_canvas.grid(row = 2)

t5_block3 = PhotoImage(file="images/Statement/ElseStatement.png")
t5_shape3 = t5_canvas.create_image(605, 50, image = t5_block3)
t5_canvas.grid(row = 2)

t6_overlay = PhotoImage(file="images/Statement.png")
t6_canvas.create_image(62, 50, image = t6_overlay)
t6.grid(row=2, sticky="W")

canvas.grid(row = 0, column = 0, columnspan = 8, rowspan = 8, stick='NE')

def t1_button1_code(self):

	global t1_shape1_on_canvas

	t1_points1_on_canvas = [70+point_adjustor, 250]
	t1_shape1_on_canvas = canvas.create_image(t1_points1_on_canvas, image = t1_block1)

	what_to_find = 'from mycroft import MycroftSkill, intent_file_handler'
	what_to_add = 'from adapt.intent import IntentBuilder \nfrom datetime import datetime, date\n'

	line_addition(what_to_find,what_to_add)

	size_variant = -180
	point_mover(size_variant)
t1_canvas.tag_bind(t1_shape1, "<Button-1>", t1_button1_code)

def t1_button1_removal(self):
	
	delete_this ='from adapt.intent import IntentBuilder'
	line_deletion(delete_this)
	
	delete_this ='import datetime'
	line_deletion(delete_this)

	canvas.delete(t1_shape1_on_canvas)
	size_variant = -340
	point_mover(size_variant)
t1_canvas.tag_bind(t1_shape1, "<Button-3>", t1_button1_removal)

def t2_button1_code(self):

	global t2_shape1_on_canvas

	t2_points1_on_canvas = [70+point_adjustor, 250]
	t2_shape1_on_canvas = canvas.create_image(t2_points1_on_canvas, image = t2_block1)

	what_to_find = 'self.speak_dialog('
	what_to_add = '        now = datetime.now().time()\n        #ifstatement\n'
	line_addition(what_to_find, what_to_add)

	size_variant = -171
	point_mover(size_variant)
t2_canvas.tag_bind(t2_shape1, "<Button-1>", t2_button1_code)

def t2_button1_removal(self):
	
	delete_this ='now = datetime.now().time()'
	line_deletion(delete_this)
	
	delete_this ='#ifstatement'
	line_deletion(delete_this)

	canvas.delete(t2_shape1_on_canvas)
	size_variant = -349
	point_mover(size_variant)
t2_canvas.tag_bind(t2_shape1, "<Button-3>", t2_button1_removal)

def t2_button2_code(self):

	global t2_shape2_on_canvas

	t2_points2_on_canvas = [70+point_adjustor, 250]
	t2_shape2_on_canvas = canvas.create_image(t2_points2_on_canvas, image = t2_block2)

	what_to_find = 'self.speak_dialog('
	what_to_add = '        CurrentDate = date.today()\n        #dateprep\n        #ifstatement\n'
	line_addition(what_to_find, what_to_add)

	size_variant = -171
	point_mover(size_variant)
t2_canvas.tag_bind(t2_shape2, "<Button-1>", t2_button2_code)	

def t2_button2_removal(self):
	
	delete_this ='CurrentDate = date.today()'
	line_deletion(delete_this)
	
	delete_this ='#dateprep'
	line_deletion(delete_this)

	delete_this ='#ifstatement'
	line_deletion(delete_this)

	canvas.delete(t2_shape2_on_canvas)
	size_variant = -349
	point_mover(size_variant)
t2_canvas.tag_bind(t2_shape2, "<Button-3>", t2_button2_removal)

def t3_row1_button1_code(self):

	argument_point_mover()

	global t3_row1_shape1_on_canvas

	t3_row1_points1_on_canvas = [150+argument_point_adjustor, 250]
	t3_row1_shape1_on_canvas = canvas.create_image(t3_row1_points1_on_canvas, image = t3_row1_block1)

	line_to_edit = 'if variablename symbol userinput:'
	what_to_edit ='variablename symbol userinput:'
	the_edit = 'now.hour symbol user_input_hour and now.minute symbol user_input_minute:'
	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row1_shape1, "<Button-1>", t3_row1_button1_code)

def t3_row1_button1_removal(self):
	
	argument_point_remover()

	line_to_edit = 'if now.hour symbol user_input_hour and now.minute symbol user_input_minute:'
	what_to_edit ='now.hour symbol user_input_hour and now.minute symbol user_input_minute:'
	the_edit = 'variablename symbol userinput'
	line_editor(line_to_edit, what_to_edit, the_edit)

	canvas.delete(t3_row1_shape1_on_canvas)
t3_canvas.tag_bind(t3_row1_shape1, "<Button-3>", t3_row1_button1_removal)

def t3_row1_button2_code(self):

	argument_point_mover()

	t3_row1_points2_on_canvas = [150+argument_point_adjustor, 250]
	t3_row1_shape2_on_canvas = canvas.create_image(t3_row1_points2_on_canvas, image = t3_row1_block2)

	line_to_edit = 'if variablename symbol userinput:'
	what_to_edit ='variablename'
	the_edit = 'CurrentDate'
	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row1_shape2, "<Button-1>", t3_row1_button2_code)

def t3_row1_button3_code(self):

	argument_point_mover()

	t3_row1_points3_on_canvas = [150+argument_point_adjustor, 250]
	t3_row1_shape3_on_canvas = canvas.create_image(t3_row1_points3_on_canvas, image = t3_row1_block3)

	line_to_edit = 'if variablename symbol userinput:'
	what_to_edit ='variablename'
	the_edit = 'now.hour symbol user_input_hour and now.minute symbol user_input_minute and CurrentDate'
	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row1_shape3, "<Button-1>", t3_row1_button3_code)

def t3_row2_button1_code(self):

	argument_point_mover()

	t3_row2_points1_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape1_on_canvas = canvas.create_image(t3_row2_points1_on_canvas, image = t3_row2_block1)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '=='

	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row2_shape1, "<Button-1>", t3_row2_button1_code)

def t3_row2_button2_code(self):

	argument_point_mover()

	t3_row2_points2_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape2_on_canvas = canvas.create_image(t3_row2_points2_on_canvas, image = t3_row2_block2)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '='

	line_editor(line_to_edit, what_to_edit, the_edit)


t3_canvas.tag_bind(t3_row2_shape2, "<Button-1>", t3_row2_button2_code)

def t3_row2_button3_code(self):

	argument_point_mover()

	t3_row2_points3_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape3_on_canvas = canvas.create_image(t3_row2_points3_on_canvas, image = t3_row2_block3)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '<'

	line_editor(line_to_edit, what_to_edit, the_edit)


t3_canvas.tag_bind(t3_row2_shape3, "<Button-1>", t3_row2_button3_code)

def t3_row2_button4_code(self):

	argument_point_mover()

	t3_row2_points4_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape4_on_canvas = canvas.create_image(t3_row2_points4_on_canvas, image = t3_row2_block4)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '>'

	line_editor(line_to_edit, what_to_edit, the_edit)


t3_canvas.tag_bind(t3_row2_shape4, "<Button-1>", t3_row2_button4_code)

def t3_row2_button5_code(self):

	argument_point_mover()

	t3_row2_points5_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape5_on_canvas = canvas.create_image(t3_row2_points5_on_canvas, image = t3_row2_block5)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '+'

	line_editor(line_to_edit, what_to_edit, the_edit)


t3_canvas.tag_bind(t3_row2_shape5, "<Button-1>", t3_row2_button5_code)

def t3_row2_button6_code(self):

	argument_point_mover()

	t3_row2_points6_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape6_on_canvas = canvas.create_image(t3_row2_points6_on_canvas, image = t3_row2_block6)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '-'

	line_editor(line_to_edit, what_to_edit, the_edit)


t3_canvas.tag_bind(t3_row2_shape6, "<Button-1>", t3_row2_button6_code)

def t3_row2_button7_code(self):

	argument_point_mover()

	t3_row2_points7_on_canvas = [150+argument_point_adjustor, 250]
	t3_row2_shape7_on_canvas = canvas.create_image(t3_row2_points7_on_canvas, image = t3_row2_block7)

	line_to_edit = 'symbol'
	what_to_edit ='symbol'
	the_edit = '!='

	line_editor(line_to_edit, what_to_edit, the_edit)


t3_canvas.tag_bind(t3_row2_shape7, "<Button-1>", t3_row2_button7_code)

def t3_row3_button1_code(self):

	argument_point_mover()

	t3_points_on_canvas = [150+argument_point_adjustor, 250]
	t3_shape1_on_canvas = canvas.create_image(t3_points_on_canvas, image = t3_row3_block1)

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

t3_canvas.tag_bind(t3_row3_shape1, "<Button-1>", t3_row3_button1_code)

def t3_row3_button2_code(self):

	argument_point_mover()

	t3_points_on_canvas = [150+argument_point_adjustor, 250]
	t3_shape1_on_canvas = canvas.create_image(t3_points_on_canvas, image = t3_row3_block1)

	to_replace = '#dateprep'
	replacement = '        user_input_date = "DayMonthYear"\n        InputDate = datetime.strptime(user_input_date, "%d-%m-%Y")\n        InputDate = InputDate.date()\n'

	line_replece(to_replace,replacement)

	user_input_date = simpledialog.askstring("Date Input","Please enter the date in a DD-MM-YYYY format")

	line_to_edit = 'user_input_date = "DayMonthYear"'
	what_to_edit ='DayMonthYear'
	the_edit = user_input_date

	line_editor(line_to_edit, what_to_edit, the_edit)

	line_to_edit = 'userinput'
	what_to_edit ='userinput'
	the_edit = 'InputDate'

	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row3_shape2, "<Button-1>", t3_row3_button2_code)

def t3_row3_button3_code(self):

	argument_point_mover()

	t3_points3_on_canvas = [150+argument_point_adjustor, 250]
	t3_shape3_on_canvas = canvas.create_image(t3_points3_on_canvas, image = t3_row3_block3)

	user_input_time = simpledialog.askstring("Time Input","Please enter time in HH:MM format")

	user_input_hour,user_input_minute = user_input_time.split(':')

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

	to_replace = '#dateprep'
	replacement = '        user_input_date = "DayMonthYear"\n        InputDate = datetime.strptime(user_input_date, "%d-%m-%Y")\n        InputDate = InputDate.date()\n'

	line_replece(to_replace,replacement)

	user_input_date = simpledialog.askstring("Date Input","Please enter the date in a DD-MM-YYYY format")

	line_to_edit = 'user_input_date = "DayMonthYear"'
	what_to_edit ='DayMonthYear'
	the_edit = user_input_date

	line_editor(line_to_edit, what_to_edit, the_edit)

	line_to_edit = 'userinput'
	what_to_edit ='userinput'
	the_edit = 'InputDate'

	line_editor(line_to_edit, what_to_edit, the_edit)

t3_canvas.tag_bind(t3_row3_shape3, "<Button-1>", t3_row3_button3_code)

def t4_button1_code(self):
	
	t4_points1_on_canvas = [70+point_adjustor, 250]
	t4_shape1_on_canvas = canvas.create_image(t4_points1_on_canvas, image = t4_block1)

	user_inp = simpledialog.askstring("Sentance Response","Please enter your dialog")

	to_replace = '#response'
	replacement = '           self.speak_dialog("DialogResponse")\n'

	line_replece(to_replace,replacement)

	what_to_find = 'self.speak_dialog("DialogResponse")'
	what_to_add = '           #response\n'

	line_addition(what_to_find,what_to_add)


	line_to_edit = 'self.speak_dialog("DialogResponse")'
	what_to_edit ='DialogResponse'
	the_edit = user_inp

	line_editor(line_to_edit, what_to_edit, the_edit)

	size_variant = -171
	point_mover(size_variant)
t4_canvas.tag_bind(t4_shape1, "<Button-1>", t4_button1_code)

def t4_button2_code(self):
	t4_points_on_canvas = [70+point_adjustor, 250]
	t4_shape2_on_canvas = canvas.create_image(t4_points_on_canvas, image = t4_block2)

	user_inp = simpledialog.askstring("Sentance Response","Please enter the website url (include https//www.)")

	if user_inp  == "":
		user_inp = 'https://www.google.com' 

	what_to_find = 'from mycroft import MycroftSkill, intent_file_handler'
	what_to_add = 'import webbrowser\n'

	line_addition(what_to_find,what_to_add)

	to_replace = '#response'
	replacement = '           webbrowser.open("https://www.google.com", new=2)\n'

	line_replece(to_replace,replacement)

	line_to_edit = 'webbrowser.open("https://www.google.com", new=2)'
	what_to_edit ='https://www.google.com'
	the_edit = user_inp

	line_editor(line_to_edit, what_to_edit, the_edit)

	what_to_find = 'webbrowser.open("'
	what_to_add = '           #response\n'

	line_addition(what_to_find,what_to_add)


	size_variant = -171
	point_mover(size_variant)
t4_canvas.tag_bind(t4_shape2, "<Button-1>", t4_button2_code)

def t5_button1_code(self):
	statement_block_tally()

	global t5_shape1_on_canvas

	t5_points1_on_canvas = [150+point_adjustor, 250]
	t5_shape1_on_canvas = canvas.create_image(t5_points1_on_canvas, image = t5_block1)

	to_replace = '#ifstatement'
	replacement = '        if variablename symbol userinput:\n'
	line_replece(to_replace,replacement)

	what_to_find = 'if variablename symbol userinput'
	what_to_add = '        #elsestatement'

	line_addition(what_to_find,what_to_add)

	what_to_find = '        if variablename symbol userinput:'
	what_to_add = '            #response\n'

	line_addition(what_to_find,what_to_add)
	size_variant = -11
	point_mover(size_variant)
t5_canvas.tag_bind(t5_shape1, "<Button-1>", t5_button1_code)

def t5_button1_removal(self):
	
	to_replace = 'if variablename symbol userinput:'
	replacement = '        #ifstatement\n'
	line_replece(to_replace,replacement)

	delete_this ='elsestatement'
	line_deletion(delete_this)

	delete_this ='#response'
	line_deletion(delete_this)

	canvas.delete(t5_shape1_on_canvas)
	size_variant = -509
	point_mover(size_variant)
t5_canvas.tag_bind(t5_shape1, "<Button-3>", t5_button1_removal)

def t5_button2_code(self):
	statement_block_tally()

	global t5_shape2_on_canvas

	t5_points_on_canvas = [150+point_adjustor, 250]
	t5_shape2_on_canvas = canvas.create_image(t5_points_on_canvas, image = t5_block2)
		
	delete_this ='#response'
	line_deletion(delete_this)

	to_replace = '#elsestatement'
	replacement = '        elif variablename symbol userinput:\n'
	line_replece(to_replace,replacement)

	what_to_find = 'elif variablename symbol userinput'
	what_to_add = '        #elsestatement'

	line_addition(what_to_find,what_to_add)

	what_to_find = 'elif variablename symbol userinput:'
	what_to_add = '           #response\n'

	line_addition(what_to_find,what_to_add)

	size_variant = -11
	point_mover(size_variant)
t5_canvas.tag_bind(t5_shape2, "<Button-1>", t5_button2_code)

def t5_button2_removal(self):
	
	delete_this ='#response'
	line_deletion(delete_this)

	to_replace = 'elif variablename symbol userinput:'
	replacement = '        #response\n'
	line_replece(to_replace,replacement)

	canvas.delete(t5_shape2_on_canvas)
	size_variant = -509
	point_mover(size_variant)
t5_canvas.tag_bind(t5_shape2, "<Button-3>", t5_button2_removal)

def t5_button3_code(self):
	statement_block_tally()

	global t5_shape3_on_canvas

	t5_points3_on_canvas = [70+point_adjustor, 250]
	t5_shape3_on_canvas = canvas.create_image(t5_points3_on_canvas, image = t5_block3)

	delete_this ='#response'
	line_deletion(delete_this)	

	to_replace = '#elsestatement'
	replacement = '        else:\n'
	line_replece(to_replace,replacement)

	what_to_find = 'else:'
	what_to_add = '    #response'

	line_addition(what_to_find,what_to_add)

	size_variant = -171
	point_mover(size_variant)
t5_canvas.tag_bind(t5_shape3, "<Button-1>", t5_button3_code)

def t5_button3_removal(self):
	
	delete_this ='#response'
	line_deletion(delete_this)

	to_replace = 'else:'
	replacement = '       #response\n       #elsestatement\n'
	line_replece(to_replace,replacement)

	canvas.delete(t5_shape3_on_canvas)
	size_variant = -509
	point_mover(size_variant)
t5_canvas.tag_bind(t5_shape3, "<Button-3>", t5_button3_removal)

root.mainloop()	