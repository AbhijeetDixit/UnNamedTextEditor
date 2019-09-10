import Tkinter
import tkMessageBox
import tkFileDialog
import datetime
from FontSelector import *


def dCallback():
	""" This is a dummy callback. This is present till 
		all the callbacks are defined."""
	tkMessageBox.showinfo('info','Button Clicked')
	pass

class createMenu(object):

	class fileMenu(object):
		"""fileMenu is the class that creates a file Menu. This adds 
			all the callbacks for submenus"""

		def create(self,toplavelWindow,parentWindow,textareaWidget):
			""" Creating sub menus for File Menu"""
			self.toplavelWindow = toplavelWindow
			self.parentWindow = parentWindow
			self.textareaWidget = textareaWidget
			fileM = Tkinter.Menu(parentWindow,tearoff=0)
			fileM.add_command(label='New',command=self.newFileCallback)
			fileM.add_command(label='Open',command=self.openFileCallback)
			fileM.add_command(label='Save',command=self.saveFileCallback)
			fileM.add_command(label='Save As', command=self.saveAsFileCallback)
			fileM.add_separator()
			fileM.add_command(label='Exit', command=self.exitCallback)
			return fileM

		def askToSaveChanges(self):
			choice = tkMessageBox.askquestion("Warning","Do you want to save your changes?", type=tkMessageBox.YESNOCANCEL, default=tkMessageBox.YES)
			if choice == 'yes':
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = 'file.txt'
				options['parent'] = self.toplavelWindow
				options['title'] = 'Save'
				fp = tkFileDialog.asksaveasfile(mode='w', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('Info', 'No file selected, not saved')
				else:
					fp.write(self.textareaWidget.get("1.0", Tkinter.END))
					fp.close()
					tkMessageBox.showinfo('Info', 'Saved')
					self.textareaWidget.delete("1.0", Tkinter.END)
				pass
			elif choice == 'no':
				self.textareaWidget.delete("1.0", Tkinter.END)
				#tkMessageBox.showinfo('Info', 'You just lost your data')
			return choice

		def exitCallback(self):
			if self.textareaWidget.edit_modified():
				self.askToSaveChanges()
			self.toplavelWindow.quit()
			pass

		def newFileCallback(self):
			if self.textareaWidget.edit_modified():
				self.askToSaveChanges()
			else:
				self.textareaWidget.delete("1.0",Tkinter.END)
			self.textareaWidget.edit_modified(False)
			self.textareaWidget.edit_reset()
			pass

		def openFileCallback(self):
			if self.textareaWidget.edit_modified():
				choice = self.askToSaveChanges()
			else:
				choice = 'no'
			if choice == 'yes' or choice == 'no':
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = ''
				options['parent'] = self.toplavelWindow
				options['title'] = 'Open'
				fp = tkFileDialog.askopenfile(mode='r', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('info', 'Unable to open')
				else:
					readData = fp.read()
					self.textareaWidget.insert(Tkinter.INSERT, readData)
					self.textareaWidget.edit_modified(False)
					self.textareaWidget.edit_reset()
					fp.close()

		def saveFileCallback(self):
			if self.textareaWidget.edit_modified():
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = ''
				options['parent'] = self.toplavelWindow
				options['title'] = 'Open'
				fp = tkFileDialog.asksaveasfile(mode='w', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('info', 'Cannot open the named file')
				else:
					dataToSave = self.textareaWidget.get("1.0",Tkinter.END)
					fp.write(dataToSave)
					fp.close()
					self.textareaWidget.edit_modified(False)
					self.textareaWidget.edit_reset()

		def saveAsFileCallback(self):
			if self.textareaWidget.edit_modified():
				file_opt = options = {}
				options['defaultextension'] = '.txt'
				options['filetypes'] = [('all files', '.*'),('text files','.txt')]
				options['initialdir'] = 'C:\\'
				options['initialfile'] = ''
				options['parent'] = self.toplavelWindow
				options['title'] = 'Open'
				fp = tkFileDialog.asksaveasfile(mode='w', **file_opt)
				if fp is None:
					tkMessageBox.showinfo('info', 'Cannot open the named file')	
				else:
					dataToSave = self.textareaWidget.get("1.0",Tkinter.END)
					fp.write(dataToSave)
					fp.close()
					self.textareaWidget.edit_modified(False)
					self.textareaWidget.edit_reset()

	class editMenu(object):
	
		def create(self,toplavelWindow,parentWindow,textareaWidget):
			self.toplavelWindow = toplavelWindow
			self.parentWindow = parentWindow
			self.textareaWidget = textareaWidget
			self.entryData = Tkinter.StringVar()
			self.lineNumVar = Tkinter.IntVar()
			editM = Tkinter.Menu(parentWindow, tearoff=0)
			editM.add_command(label='Undo',command=self.undoCallback)
			editM.add_command(label='Redo',command=self.redoCallback)
			editM.add_separator()
			editM.add_command(label='Cut',command=self.cutCallback)
			editM.add_command(label='Copy',command=dCallback)
			editM.add_command(label='Paste',command=dCallback)
			editM.add_command(label='Delete',command=self.deleteCallback)
			editM.add_separator()
			editM.add_command(label='Find..',command=self.findCallback)
			editM.add_command(label='Find Next', command=dCallback)
			editM.add_command(label='Replace',command=dCallback)
			editM.add_command(label='Go to..',command=self.gotoCallback)
			editM.add_separator()
			editM.add_command(label='Select All',command=self.selectAllCallback)
			editM.add_command(label='Date/Time',command=self.dateTimeCallback)
			editM.entryconfig('Find Next',state='disabled')
			editM.entryconfig('Replace',state='disabled')
			return editM

		def dateTimeCallback(self):
			now = datetime.datetime.now()
			dateStr = str(now)
			self.textareaWidget.insert(Tkinter.INSERT,dateStr)
			pass

		def cutCallback(self):
			try:
				text = self.textareaWidget.get("sel.last")
				self.textareaWidget.delete("sel.first","sel.last")
			except Exception, e:
				raise e
			pass

		def deleteCallback(self):
			try:
				self.textareaWidget.delete("sel.first","sel.last")
			except Exception, e:
				raise e
			pass

		def undoCallback(self):
			try:
				self.textareaWidget.edit_undo()
			except Exception, e:
				raise e
			pass

		def redoCallback(self):
			try:
				self.textareaWidget.edit_redo()
			except Exception, e:
				raise e
			pass

		def findCallback(self):
			top = Tkinter.Toplevel()
			top.title('Find...')
			top.geometry('320x100')
			top.resizable(width=0, height=0)
			top.minsize(width=320, height=100)
			top.maxsize(width=320,height=100)

			label1 = Tkinter.Label(top,text="Enter Text: ")
			textEntry = Tkinter.Entry(top,textvariable=self.entryData)
			doneButton = Tkinter.Button(top,text='Find Next', command=self.doSearch)
			cancelButton = Tkinter.Button(top,text='Cancel', command=top.destroy)
			label1.grid(row=0,column=0,columnspan=1,padx=1,pady=2)
			textEntry.grid(row=0,column=1,columnspan=1,padx=1,pady=2)
			doneButton.grid(row=0,column=3,columnspan=1,sticky=Tkinter.E,padx=1,pady=2)
			cancelButton.grid(row=1,column=3,columnspan=1,sticky=Tkinter.E,padx=1,pady=2)
			var = Tkinter.IntVar()
			checkBox = Tkinter.Checkbutton(top,text='Match case',variable=var)
			checkBox.grid(row=3,column=0,padx=1,pady=2)
			var1 = Tkinter.IntVar()
			Tkinter.Radiobutton(top, text='up', variable=var1, value=1).grid(row=3,column=3,padx=1,pady=2)
			Tkinter.Radiobutton(top,text='down',variable=var1, value=2).grid(row=3,column=4,padx=1,pady=2)

		def doSearch(self):
			countVar = Tkinter.StringVar()
			pos = self.textareaWidget.search(self.entryData.get(), "1.0", stopindex="end", count=countVar)
			self.textareaWidget.tag_configure("search",background="green")
			self.textareaWidget.tag_add("search",pos, "%s + %sc"%(pos, countVar.get()))
			pass

		def gotoCallback(self):
			top = Tkinter.Toplevel()
			top.title('Go To..')
			top.geometry('320x50')
			top.resizable(width=0, height=0)
			top.minsize(width=320, height=100)
			top.maxsize(width=320,height=100)
			label1 = Tkinter.Label(top, text="Line Number: ")
			textEntry = Tkinter.Entry(top, textvariable=self.lineNumVar)
			button1 = Tkinter.Button(top, text="Go", command=self.gotoCb)
			button2 = Tkinter.Button(top, text="Cancel", command=top.destroy)
			label1.grid(row=0,column=0,columnspan=1,pady=1)
			textEntry.grid(row=0,column=1,columnspan=1)
			button1.grid(row=1,column=2,columnspan=1)
			button2.grid(row=1,column=3,columnspan=1)
			pass

		def gotoCb(self):
			self.textareaWidget.mark_set("insert","%d.0"%(self.lineNumVar.get()))
			pass

		def selectAllCallback(self):
			self.textareaWidget.tag_add(Tkinter.SEL,"1.0",Tkinter.END)
			pass

	class formatMenu(object):
		
		def create(self,toplavelWindow, parentWindow, textareaWidget):
			self.parentWindow = parentWindow
			formatM = Tkinter.Menu(parentWindow, tearoff=0)
			formatM.add_command(label='Word Wrap', command=dCallback)
			formatM.add_command(label='Font..', command=self.fontSelectCallback)
			return formatM

		def fontSelectCallback(self):
			print FontChooser(self.parentWindow).result
			pass
		
	class viewMenu(object):
	
		def create(self, toplavelWindow, parentWindow, textareaWidget):
			viewM = Tkinter.Menu(parentWindow, tearoff=0)
			viewM.add_command(label='Status Bar', command=dCallback)
			return viewM
		
	class helpMenu(object):
	
		def create(self,toplavelWindow, parentWindow, textareaWidget):
			helpM = Tkinter.Menu(parentWindow, tearoff=0)
			helpM.add_command(label='Show Help',command=self.showHelpCallback)
			helpM.add_separator()
			helpM.add_command(label='About this utility',command=self.aboutCallback)
			return helpM

		def showHelpCallback(self):
			tkMessageBox.showerror("Help","Currently the software is in development mode.\nNo help available.")
			pass

		def aboutCallback(self):
			tkMessageBox.showinfo("About Me","A simple notepad Utility.\nCreated using python 2.7\nBy - Abhijeet Dixit")
			pass

	def createM(self,mtype, toplavelWindow, parentWindow, textareaWidget):
		if mtype == 0:
			return self.fileMenu().create(toplavelWindow,parentWindow, textareaWidget)
		elif mtype == 1:
			return self.editMenu().create(toplavelWindow, parentWindow, textareaWidget)
		elif mtype == 2:
			return self.formatMenu().create(toplavelWindow, parentWindow, textareaWidget)
		elif mtype == 3:
			return self.viewMenu().create(toplavelWindow, parentWindow, textareaWidget)
		elif mtype == 4:
			return self.helpMenu().create(toplavelWindow, parentWindow, textareaWidget)
		pass