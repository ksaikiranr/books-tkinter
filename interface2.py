from tkinter import  ttk
from tkinter import *
import db1

DBName = "student"
tableName = "bookstore"

db1.connectD(DBName, tableName)
# populate db if needed
# db1.insertD(DBName,tableName,'RainBow',"Blue man",'2000','ISBN001')
# db1.insertD(DBName,tableName,'Cooking',"Candy man",'2001','ISBN002')
# db1.insertD(DBName,tableName,"Python programming","Ross",'2007','ISBN003')
# db1.insertD(DBName,tableName,"Animals life",'Vikram','2008','ISBN004')
# db1.insertD(DBName,tableName,"Human life",'Manohar','2009','ISBN005')


# initialise
root = Tk()
root.title("BookStore")
root.geometry("600x500+300+200")
#root.resizable(0, 0)  # Disable resize


# functions
def itemSelected(event):
	selected = list(displayList.get(displayList.curselection()))
	clearEntires()  # Clear all entires
	title.insert(END, selected[0])  # Title added
	author.insert(END, selected[1])  # Author added
	year.insert(END, selected[2])  # Year added
	isbn.insert(END, selected[3])  # isbn added


def clearEntires():
	title.delete(0, END)
	author.delete(0, END)
	year.delete(0, END)
	isbn.delete(0, END)


def viewAll():
	rows = db1.fetchD(DBName, tableName)
	displayList.delete(0, END)  # Empty the list before adding
	for row in rows:
		displayList.insert(rows.index(row), row)

def searchBook():
	rows = db1.searchD(DBName, tableName, isbn.get())
	displayList.delete(0, END)
	for row in rows:
		displayList.insert(rows.index(row), row)


def addBook():
	db1.insertD(DBName, tableName, title.get(), author.get(), year.get(), isbn.get())
	ind = (displayList.get(0,END)).count
	row = (title.get(), author.get(), year.get(), isbn.get())
	displayList.insert(ind,row)

def updateBook():
	db1.updateD(DBName, tableName, title.get(), author.get(), year.get(), isbn.get())


def deleteBook():
	db1.deleteDRow(DBName, tableName, title.get(), author.get(), year.get(), isbn.get())


def closeBook():
	root.quit()
	root.destroy()
	exit()

#Entries
entriesFrame = LabelFrame(root, text='Book Store Entries')
entriesFrame.grid(column=0, row=0, padx=8, pady=8)
#styles
labelsPadx = 8
labelsPady = 8
#title
titleL  = Label(entriesFrame,text='Title',font=15).grid(row=1,column=1,sticky=W,padx=labelsPadx,pady=labelsPady)
title   = Entry(entriesFrame,font=15)
title.grid(row=1,column=2,sticky=E,padx=labelsPadx,pady=labelsPady)
#author
authorL = Label(entriesFrame,text='Author',font=15).grid(row=1,column=3,sticky=W,padx=labelsPadx,pady=labelsPady)
author  = Entry(entriesFrame,font=15)
author.grid(row=1,column=4,sticky=W,padx=labelsPadx,pady=labelsPady)
#year
yearL = Label(entriesFrame,text='Year',font=15).grid(row=2,column=1,sticky=W,padx=labelsPadx,pady=labelsPady)
year = Entry(entriesFrame,font=15)
year.grid(row=2,column=2,sticky=E,padx=labelsPadx,pady=labelsPady)
#isbn
isbnL = Label(entriesFrame,text='ISBN',font=15).grid(row=2,column=3,sticky=W,padx=labelsPadx,pady=labelsPady)
isbn = Entry(entriesFrame,font=15)
isbn.grid(row=2,column=4,sticky=W,padx=labelsPadx,pady=labelsPady)


#Listbox
listBoxFrame = LabelFrame(root, text='Books Catalogue',width=40,height=30)
listBoxFrame.grid(row=4,column=0,padx=8,pady=8,sticky=W)
displayList = Listbox(listBoxFrame,width=40,height=20)
viewAll()
displayList.grid(row=5,column=0,sticky=E,padx=labelsPady,pady=labelsPady)
#select event
displayList.bind("<<ListboxSelect>>",itemSelected)



#Scrollbar
listScrollBar = Scrollbar(listBoxFrame,orient=VERTICAL)
displayList.configure(yscrollcommand=listScrollBar.set)
listScrollBar.configure(command=displayList.yview)
listScrollBar.grid(row=5,column=11,padx=0,pady=0,sticky=N+S)

#Buttons
buttonPadx = 8
buttonPady = 5
buttonsFrame = LabelFrame(root, text='Options',height=30)
buttonsFrame.grid(row=4,column=0,padx=8,pady=8,sticky=E)
viewAll = Button(buttonsFrame,text="View all",command=viewAll,font=15,width=15).grid(row=4,column=0,sticky=W,padx=buttonPadx,pady=buttonPady)

searchEntry = Button(buttonsFrame,text="Search Entry",command=searchBook,font=15,width=15).grid(row=5,sticky=W,padx=buttonPadx,pady=buttonPady)

addEntry = Button(buttonsFrame,text="Add Entry",command=addBook,font=15,width=15).grid(row=6,sticky=W,padx=buttonPadx,pady=buttonPady)

updateSelected = Button(buttonsFrame,text="Update Selected",command=updateBook,font=15,width=15).grid(row=7,sticky=W,padx=buttonPadx,pady=buttonPady)

deleteSelected = Button(buttonsFrame,text="Delete Selected",command=deleteBook,font=15,width=15).grid(row=8,sticky=W,padx=buttonPadx,pady=buttonPady)

clearValues = Button(buttonsFrame,text="Clear Entries",command=clearEntires,font=15,width=15).grid(row=9,sticky=W,padx=buttonPadx,pady=buttonPady)

closeAll = Button(buttonsFrame,text="Close",command=closeBook,font=15,width=15).grid(row=10,padx=buttonPadx,sticky=W,pady=buttonPady)


root.mainloop()