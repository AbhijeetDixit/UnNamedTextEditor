import sys
import Tkinter
import tkMessageBox
import tkFileDialog
from MenuFactory import *
import ttk

class Editor(object):
	"""docstring for Editor"""
	def __init__(self, fileName):
		self.currentFile = fileName
		self.rootWindow = Tkinter.Tk()
		self.rootWindow.tk.eval('package require Tix')
		self.rootWindow.bind('<Configure>', self.resize)
		self.rootWindow.bind_all

	def resize(self, event):
		w,h = self.rootWindow.winfo_width(), self.rootWindow.winfo_height()
		hb = self.bottomFrame.winfo_height()
		ht = self.topFrame.winfo_height()
		self.middleFrame.config(width=w, height=h-hb-ht)
		self.text.config(width=w, height=h-hb-ht)
		pass

	def addWidgetsNRun(self):
		self.textVar = Tkinter.StringVar()
		# Adding a mainFrame that contains all other widgets
		self.mainFrame = Tkinter.Frame(self.rootWindow)
		self.mainFrame.grid(row=0, column=0)

		# Adding a top and bottom frame for menu and text area
		# respectively
		self.middleFrame = Tkinter.Frame(self.rootWindow)
		self.middleFrame.grid(row=1, column=0)

		self.topFrame = Tkinter.Frame(self.rootWindow)
		#self.topFrame.pack(side=Tkinter.TOP)
		self.topFrame.grid(row=0, column=0)

		self.bottomFrame = Tkinter.Frame(self.rootWindow, bd=1)
		#self.bottomFrame.pack(side=Tkinter.BOTTOM)
		self.bottomFrame.grid(row=2, column=0)

		self.tabControl = ttk.Notebook(self.middleFrame)
		self.tab1 = ttk.Frame(self.tabControl)
		self.tabControl.add(self.tab1, text='unsaved')

		# Adding scrollbars
		self.VScrollBar = Tkinter.Scrollbar(self.tab1)
		self.VScrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

		self.HScrollBar = Tkinter.Scrollbar(self.tab1,orient=Tkinter.HORIZONTAL)
		self.HScrollBar.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)

		# Adding a text area where all the text goes
		self.text = Tkinter.Text(self.tab1,undo=True,bd=1)
		self.text.insert(Tkinter.INSERT,"")
		self.text.pack()

		# Attaching scrollbars to Text
		self.text.config(yscrollcommand=self.VScrollBar.set)
		self.VScrollBar.config(command=self.text.yview)
		self.text.config(xscrollcommand=self.HScrollBar.set)
		self.HScrollBar.config(command=self.text.xview)

		self.tabControl.pack(expand=1, fill='both')

		self.statusLabel = Tkinter.Label(self.bottomFrame, bd=1, anchor=Tkinter.E, textvariable=self.textVar, font=('ariel',12,'normal'))
		self.statusLabel.grid(row=0,column=0,sticky=Tkinter.W)
		self.textVar.set('Ln 0,Col 0')

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