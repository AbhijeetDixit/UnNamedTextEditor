import sys
import Tkinter
import tkMessageBox
import tkFileDialog
from MenuFactory import *

class Editor(object):
	"""docstring for Editor"""
	def __init__(self, fileName):
		self.currentFile = fileName
		self.rootWindow = Tkinter.Tk()
		self.rootWindow.tk.eval('package require Tix')
		self.rootWindow.bind('<Configure>', self.root_resize)
		#self.rootWindow.bind_all
		self.rootWindow.attributes('-zoomed', True)

	def root_resize(self, event):
		w,h = self.rootWindow.winfo_width()-100, self.rootWindow.winfo_height() - 100
		self.text.config(width=w, height=h)
		pass

	def addWidgetsNRun(self):
		self.textVar = Tkinter.StringVar()
		# Adding a mainFrame that contains all other widgets
		self.mainFrame = Tkinter.Frame(self.rootWindow)
		self.mainFrame.pack()

		# Adding a top and bottom frame for menu and text area
		# respectively
		self.middleFrame = Tkinter.Frame(self.rootWindow)
		self.middleFrame.pack()

		self.topFrame = Tkinter.Frame(self.rootWindow)
		self.topFrame.pack(side=Tkinter.TOP)

		self.bottomFrame = Tkinter.Frame(self.rootWindow, bd=1)
		self.bottomFrame.pack(side=Tkinter.BOTTOM)

		# Adding scrollbars
		self.VScrollBar = Tkinter.Scrollbar(self.middleFrame)
		self.VScrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

		self.HScrollBar = Tkinter.Scrollbar(self.middleFrame,orient=Tkinter.HORIZONTAL)
		self.HScrollBar.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)

		# Adding a text area where all the text goes
		self.text = Tkinter.Text(self.middleFrame,undo=True,bd=1)
		self.text.insert(Tkinter.INSERT,"")
		self.text.pack(expand=1, fill=Tkinter.BOTH)

		# Attaching scrollbars to Text
		self.text.config(yscrollcommand=self.VScrollBar.set)
		self.VScrollBar.config(command=self.text.yview)
		self.text.config(xscrollcommand=self.HScrollBar.set)
		self.HScrollBar.config(command=self.text.xview)

		self.statusLabel = Tkinter.Label(self.bottomFrame, bd=1, anchor=Tkinter.E, textvariable=self.textVar, font=('ariel',12,'normal'))
		self.statusLabel.grid(row=0,column=0,sticky=Tkinter.W)
		self.textVar.set('Ln 0,Col 0')

		# Instantiating a createmenu class and creating menu
		self.createmenu = createMenu()
		self.menuBar = Tkinter.Menu(self.topFrame)
		self.filemenu = self.createmenu.createM(0, self.rootWindow, self.menuBar, self.text)
		self.editmenu = self.createmenu.createM(1, self.rootWindow, self.menuBar, self.text)
		self.formatmenu = self.createmenu.createM(2, self.rootWindow, self.menuBar, self.text)
		self.viewmenu = self.createmenu.createM(3, self.rootWindow, self.menuBar, self.text)
		self.helpmenu = self.createmenu.createM(4, self.rootWindow, self.menuBar, self.text)
		self.menuBar.add_cascade(label='File',menu=self.filemenu)
		self.menuBar.add_cascade(label='Edit',menu=self.editmenu)
		self.menuBar.add_cascade(label='Format',menu=self.formatmenu)
		self.menuBar.add_cascade(label='View',menu=self.viewmenu)
		self.menuBar.add_cascade(label='Help',menu=self.helpmenu)
		self.rootWindow.config(menu=self.menuBar)
		self.rootWindow.mainloop()



if __name__ == '__main__':
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "Untitled"
	editorInstance = Editor(filename)
	editorInstance.addWidgetsNRun()