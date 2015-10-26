from common_imports import *

class Edit():

	def popup(self, event):
		self.rightClick.post(event.x_root, event.y_root)
	
	def copy(self, *args):
		try:
			sel = self.text.selection_get()
			self.clipboard = sel
		except:
			pass

	def cut(self, *args):
		try:
			sel = self.text.selection_get()
			self.clipboard = sel
			self.text.delete(SEL_FIRST, SEL_LAST)
		except:
			pass
	
	def paste(self, *args):
		self.text.insert(INSERT, self.clipboard)
	
	def selectAll(self, *args):
		self.text.tag_add(SEL, "1.0", END)
		self.text.mark_set(0.0, END)
		self.text.see(INSERT)
	
	def undo(self, *args):
		try:
	 	   self.text.edit_undo()
	 	except:
			pass

 	def redo(self, *args):
 		try:
	 		self.text.edit_redo()
	 	except:
	 		pass 
	   
	def __init__(self,text, root):
		self.clipboard = ''
		self.text = text
		self.rightClick = Menu(root)
		
def main(root,text,menubar):

	objEdit = Edit(text, root)
	
	editmenu = Menu(menubar)
	editmenu.add_command(label="Copy", command=objEdit.copy, accelerator="Ctrl+C")
	editmenu.add_command(label="Cut", command=objEdit.cut, accelerator="Ctrl+X")
	editmenu.add_command(label="Paste", command=objEdit.paste, accelerator="Ctrl+V")
	editmenu.add_command(label="Undo", command=objEdit.undo, accelerator="Ctrl+Z")
	editmenu.add_command(label="Redo", command=objEdit.redo, accelerator="Ctrl+Y")
	editmenu.add_separator()
	editmenu.add_command(label="Select All", command=objEdit.selectAll, accelerator="Ctrl+A")
	menubar.add_cascade(label="Edit", menu=editmenu)

	root.bind_all("<Control-z>", objEdit.undo)
	root.bind_all("<Control-y>", objEdit.redo)
	
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
