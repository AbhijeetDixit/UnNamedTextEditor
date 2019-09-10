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

	def addWidgetsNRun(self):
		textVar = Tkinter.StringVar()
		# Adding a mainFrame that contains all other widgets
		mainFrame = Tkinter.Frame(self.rootWindow)
		mainFrame.pack()

		# Adding a top and bottom frame for menu and text area
		# respectively
		middleFrame = Tkinter.Frame(self.rootWindow)
		middleFrame.pack()

		topFrame = Tkinter.Frame(self.rootWindow)
		topFrame.pack(side=Tkinter.TOP)

		bottomFrame = Tkinter.Frame(self.rootWindow, bd=1)
		bottomFrame.pack(side=Tkinter.BOTTOM)

		# Adding scrollbars
		VScrollBar = Tkinter.Scrollbar(middleFrame)
		VScrollBar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

		HScrollBar = Tkinter.Scrollbar(middleFrame,orient=Tkinter.HORIZONTAL)
		HScrollBar.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)

		# Adding a text area where all the text goes
		text = Tkinter.Text(middleFrame,undo=True,bd=1)
		text.insert(Tkinter.INSERT,"")
		text.pack()

		# Attaching scrollbars to Text
		text.config(yscrollcommand=VScrollBar.set)
		VScrollBar.config(command=text.yview)
		text.config(xscrollcommand=HScrollBar.set)
		HScrollBar.config(command=text.xview)

		statusLabel = Tkinter.Label(bottomFrame, bd=1, anchor=Tkinter.E, textvariable=textVar, font=('ariel',12,'normal'))
		statusLabel.grid(row=0,column=0,sticky=Tkinter.W)
		textVar.set('Ln 0,Col 0')

		# Instantiating a createmenu class and creating menu
		createmenu = createMenu()
		menuBar = Tkinter.Menu(topFrame)
		filemenu = createmenu.createM(0, self.rootWindow, menuBar, text)
		editmenu = createmenu.createM(1, self.rootWindow, menuBar, text)
		formatmenu = createmenu.createM(2, self.rootWindow, menuBar, text)
		viewmenu = createmenu.createM(3, self.rootWindow, menuBar, text)
		helpmenu = createmenu.createM(4, self.rootWindow, menuBar, text)
		menuBar.add_cascade(label='File',menu=filemenu)
		menuBar.add_cascade(label='Edit',menu=editmenu)
		menuBar.add_cascade(label='Format',menu=formatmenu)
		menuBar.add_cascade(label='View',menu=viewmenu)
		menuBar.add_cascade(label='Help',menu=helpmenu)
		self.rootWindow.config(menu=menuBar)
		self.rootWindow.mainloop()



if __name__ == '__main__':
	if len(sys.argv) > 1:
		filename = sys.argv[1]
	else:
		filename = "Untitled"
	editorInstance = Editor(filename)
	editorInstance.addWidgetsNRun()