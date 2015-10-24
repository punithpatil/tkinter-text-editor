from common_imports import *

class Edit():

	def popup(event):
		rightClick.post(event.x_root, event.y_root)
	
	def copy(self):
		sel = self.text.selection_get()
		self.clipboard = sel

	def cut(self):
		sel = self.text.selection_get()
		self.clipboard = sel
		self.text.delete(SEL_FIRST, SEL_LAST)
	
	def paste(self):
		self.text.insert(INSERT, self.clipboard)
	
	def selectAll():
		self.text.tag_add(SEL, "1.0", END)
		self.text.mark_set(0.0, END)
		self.text.see(INSERT)
	
	def __init__(self,text):
		self.clipboard = None
		self.text = text
		
def main(root,text):
	objEdit = Edit(text)
	editmenu = Menu(menubar)
	editmenu.add_command(label="Copy", command=objEdit.copy)
	editmenu.add_command(label="Cut", command=objEdit.cut)
	editmenu.add_command(label="Paste", command=objEdit.paste)
	editmenu.add_command(label="Select All", command=objEdit.selectAll)
	menubar.add_cascade(label="Edit", menu=editmenu)
	
	rightClick = Menu(root, tearoff=0)
	rightClick.add_command(label="Copy", command=objEdit.copy)
	rightClick.add_command(label="Cut", command=objEdit.cut)
	rightClick.add_command(label="Paste", command=objEdit.paste)
	rightClick.add_separator()
	rightClick.add_command(label="Select All", command=objEdit.selectAll)
	
	text.bind("<Button-3>", objEdit.popup)
	
	root.config(menu=menubar)

if __name__ == "__main__":
	print ("Please run 'main.py'")
