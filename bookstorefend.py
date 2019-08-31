"""
A program that stores book imformation:
Title,author,Year,ISBN

User can
1)Search data
2)Add data
3)View all records
4)Update entry
5)Delete
6)Close

"""
#!/Applications/anaconda3/bin/python

import tkinter as tk
import bookstorebend as bk

def view_command():
	list1.delete(0,tk.END)  #to not allow repitition on pressing view button more than once
	for row in bk.view():
		list1.insert(tk.END,row)	#add data to the listbox
		
def search_data():
	list1.delete(0,tk.END) 
	for row in bk.search(title_text.get(),author_text.get()):
		list1.insert(tk.END,row)

def add_entry():
	bk.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
	list1.delete(0,tk.END)
	list1.insert(tk.END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
 

def get_selected_row(event):
	global tuple1
	index=list1.curselection()[0]
	tuple1=list1.get(index)
	try :
	    e1.delete(0,tk.END)
	    e1.insert(tk.END,tuple1[1])
	    e2.delete(0,tk.END)
	    e2.insert(tk.END,tuple1[2])
	    e3.delete(0,tk.END)
	    e3.insert(tk.END,tuple1[3])
	    e4.delete(0,tk.END)
	    e4.insert(tk.END,tuple1[4])
	except IndexError:
		pass


def delete_fun():
	bk.delete(tuple1[0])

def update_data():
	bk.update(tuple1[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())



window = tk.Tk()
window.wm_title("Bookstore")


l1=tk.Label(window,text="Title")
l1.grid(row=0,column=0)

l2=tk.Label(window,text="Author")
l2.grid(row=0,column=2)

l3=tk.Label(window,text="Year")
l3.grid(row=1,column=0)

l4=tk.Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text=tk.StringVar()
e1=tk.Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=tk.StringVar()
e2=tk.Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=tk.IntVar()
e3=tk.Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=tk.IntVar()
e4=tk.Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

list1=tk.Listbox(window,height=12,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=tk.Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)     #widget.bind(event, handler) 
                                                     # If the defined event occurs in the widget, the "handler" function is called with an event object. describing the event. 


b1=tk.Button(window,text="View all",width=12,command=view_command)
b1.grid(row=3,column=3)

b2=tk.Button(window,text="Search Entry",width=12,command=search_data)
b2.grid(row=4,column=3)

b3=tk.Button(window,text="Add Entry",width=12,command=add_entry)
b3.grid(row=5,column=3)

b4=tk.Button(window,text="Update",width=12,command=update_data)
b4.grid(row=6,column=3)

b5=tk.Button(window,text="Delete",width=12,command=delete_fun)
b5.grid(row=7,column=3)

b6=tk.Button(window,text="Close",width=12,command=window.destroy)
b6.grid(row=8,column=3)








window.mainloop()

