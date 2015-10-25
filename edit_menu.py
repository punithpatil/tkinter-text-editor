from common_imports import *

class Edit():

	def popup(self, event):
		self.rightClick.post(event.x_root, event.y_root)
	
	def copy(self):
		sel = self.text.selection_get()
		self.clipboard = sel

	def cut(self):
		sel = self.text.selection_get()
		self.clipboard = sel
		self.text.delete(SEL_FIRST, SEL_LAST)
	
	def paste(self):
		self.text.insert(INSERT, self.clipboard)
	
	def selectAll(self):
		self.text.tag_add(SEL, "1.0", END)
		self.text.mark_set(0.0, END)
		self.text.see(INSERT)
	
	def __init__(self,text, root):
		self.clipboard = None
		self.text = text
		self.rightClick = Menu(root)
		
def main(root,text,menubar):

	objEdit = Edit(text, root)
	editmenu = Menu(menubar)
	editmenu.add_command(label="Copy", command=objEdit.copy)
	editmenu.add_command(label="Cut", command=objEdit.cut)
	editmenu.add_command(label="Paste", command=objEdit.paste)
	editmenu.add_command(label="Select All", command=objEdit.selectAll)
	menubar.add_cascade(label="Edit", menu=editmenu)
	
	objEdit.rightClick.add_command(label="Copy", command=objEdit.copy)
	objEdit.rightClick.add_command(label="Cut", command=objEdit.cut)
	objEdit.rightClick.add_command(label="Paste", command=objEdit.paste)
	objEdit.rightClick.add_separator()
	objEdit.rightClick.add_command(label="Select All", command=objEdit.selectAll)
	objEdit.rightClick.bind("<Control-q>", objEdit.selectAll)
	
	text.bind("<Button-3>", objEdit.popup)

	
	root.config(menu=menubar)

if __name__ == "__main__":
	print ("Please run 'main.py'")
