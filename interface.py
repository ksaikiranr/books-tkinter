from tkinter import  *
import db1

DBName = "student"
tableName = "bookstore"

db1.connectD(DBName,tableName)
#populate db if needed
#db1.insertD(DBName,tableName,'RainBow',"Blue man",'2000','ISBN001')
#db1.insertD(DBName,tableName,'Cooking',"Candy man",'2001','ISBN002')
#db1.insertD(DBName,tableName,"Python programming","Ross van dum",'2007','ISBN003')
#db1.insertD(DBName,tableName,"Animals life",'Vikram','2008','ISBN004')
#db1.insertD(DBName,tableName,"Human life",'Manohar','2009','ISBN005')


#initialise
root = Tk()
root.title("BookStore")
root.geometry("600x500+300+200")
root.resizable(0,0)						#Disable resize

#functions

def itemSelected(event):
	selected = list(displayList.get(displayList.curselection()))
	clearEntires()						#Clear all entires
	title.insert(END,selected[0])		#Title added
	author.insert(END, selected[1])		#Author added
	year.insert(END, selected[2])		#Year added
	isbn.insert(END, selected[3])		#isbn added

def clearEntires():
	title.delete(0, END)
	author.delete(0, END)
	year.delete(0, END)
	isbn.delete(0, END)
	
def viewAll():
	rows = db1.fetchD(DBName, tableName)
	displayList.delete(0,END)					#Empty the list before adding
	for row in rows:
		displayList.insert(rows.index(row), row)

def searchBook():
	rows = db1.searchD(DBName,tableName,isbn.get())
	displayList.delete(0,END)
	for row in rows:
		displayList.insert(rows.index(row),row)

def addBook():
	
	db1.insertD(DBName,tableName,title.get(),author.get(),year.get(),isbn.get())

def updateBook():
	db1.updateD(DBName, tableName, title.get(), author.get(), year.get(), isbn.get())
	

def deleteBook():
	db1.deleteDRow(DBName, tableName, title.get(), author.get(), year.get(), isbn.get())

def closeBook():
	root.quit()
	root.destroy()
	exit()
	
#Labels and entries
#col1
titleL  = Label(text='Title',font=15).place(x=10,y=10)
title   = Entry(root,font=15)
title.place(x=55,y=10)
yearL = Label(text='Year',font=15).place(x=10,y=45)
year = Entry(root,font=15)
year.place(x=55,y=45)
#col2
authorL = Label(text='Author',font=15).place(x=300,y=10)
author  = Entry(root,font=15)
author.place(x=365,y=10)
isbnL = Label(text='ISBN',font=15).place(x=300,y=45)
isbn = Entry(root,font=15)
isbn.place(x=365,y=45)

listFrame = Frame(root)

#ListBox
displayList = Listbox(root)
viewAll()
displayList.place(x=20,y=100,width=350,height=350)
#select event
displayList.bind("<<ListboxSelect>>",itemSelected)

#Scrollbar
listScrollBar = Scrollbar(root)
displayList.configure(yscrollcommand=listScrollBar.set)
listScrollBar.configure(command=displayList.yview)
listScrollBar.place(x=370,y=100,height=350)

#Buttons
viewAll = Button(text="View all",command=viewAll,font=15).place(x=420,y=100,width=160)
searchEntry = Button(text="Search Entry",command=searchBook,font=15).place(x=420,y=140,width=160)
addEntry = Button(text="Add Entry",command=addBook,font=15).place(x=420,y=180,width=160)
updateSelected = Button(text="Update Selected",command=updateBook,font=15).place(x=420,y=220,width=160)
deleteSelected = Button(text="Delete Selected",command=deleteBook,font=15).place(x=420,y=260,width=160)
clearValues = Button(text="Clear Entries",command=clearEntires,font=15).place(x=420,y=300,width=160)
closeAll = Button(text="Close",command=closeBook,font=15).place(x=420,y=340,width=160)


#Start GUI
root.mainloop()

