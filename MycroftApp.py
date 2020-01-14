from tkinter import * 
import shlex, subprocess

root = Tk()
root.title('Mycroft Skill Maker')

subprocess.call(['cd', ' ..'], shell=True)
subprocess.call('cd /home/michal/mycroft-core', shell=True)
subprocess.call('start-mycroft.sh cli', shell=True)

root.mainloop()