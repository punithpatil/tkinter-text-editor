from common_imports import *
from tkFileDialog import *
from tkMessageBox import *
from tkFont import Font
from ScrolledText import *
import file_menu
import edit_menu

root = Tk()

root.title("Text Editor-Untiltled")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

font = Font(family="Verdana", size=10)

text = ScrolledText(root, state='normal', height=400, width=400, wrap='word', font = font, pady=2, padx=3, undo=True)
text.pack(fill=Y, expand=1)
text.focus_set()

menubar = Menu(root)

file_menu.main(root,text,menubar)
edit_menu.main(root,text,menubar)

root.mainloop()
