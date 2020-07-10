from tkinter import *
from backend import *

win=Tk(screenName="Okay")
win.wm_title("BookStore")
def view_command():
    lb1.delete(0,END)
    rows=viewall()
    for row in rows:
        lb1.insert(END,row)

def search_command():
    lb1.delete(0,END)
    rows=search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    for row in rows:
        lb1.insert(END,row)

def add_command():
    lb1.delete(0,END)
    insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    lb1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    lb1.delete(0,END)
    delete(int(value[0]))
    rows=viewall()
    for row in rows:
        lb1.insert(END,row)

def update_command():
    update(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),value[0])
    lb1.delete(0,END)
    lb1.insert(END,(search(value[1],value[2],value[3],value[4])))
    
    
def display_selected_value():
    e1.delete(0,END)
    e1.insert(END,value[1])
    e2.delete(0,END)
    e2.insert(END,value[2])
    e3.delete(0,END)
    e3.insert(END,value[3])
    e4.delete(0,END)
    e4.insert(END,value[4])
    
l1=Label(win,text='Title : ')
l1.grid(row=0,column=0)

title_text=StringVar()
e1=Entry(win,textvariable=title_text)
e1.grid(row=0,column=1,columnspan=1)

l2=Label(win,text="Author : ")
l2.grid(row=0,column=2)

author_text=StringVar()
e2=Entry(win,textvariable=author_text)
e2.grid(row=0,column=3,columnspan=1)

l3=Label(win,text="Year : ")
l3.grid(row=1,column=0)

year_text=StringVar()
e3=Entry(win,textvariable=year_text)
e3.grid(row=1,column=1,columnspan=1)

l4=Label(win,text="ISBN : ")
l4.grid(row=1,column=2)

isbn_text=StringVar()
e4=Entry(win,textvariable=isbn_text)
e4.grid(row=1,column=3,columnspan=1)

lb1=Listbox(win,height=6,width=50)
lb1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(win)
sb1.grid(row=4,column=2,rowspan=6,columnspan=2)

def onselect(evt):
    try:
        global value
        w=evt.widget
        index=int(w.curselection()[0])
        value=w.get(index)
        display_selected_value()
        return value
    except IndexError:
        pass
        
lb1.bind('<<ListboxSelect>>',onselect)


#sb2=Scrollbar(win)
#sb2.grid(row=3,column=1)
def a():
    print(value)
#lb1.configure(xscrollcommad=sb2.set)
#sb2.configure(command=lb1.xview)

lb1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lb1.yview)

b1=Button(win,text="View all",width=12,command=view_command)
b1.grid(row=3,column=4)

b2=Button(win,text="Search entry",width=12,command=search_command)
b2.grid(row=4,column=4)

b3=Button(win,text="Add entry",width=12,command=add_command)
b3.grid(row=5,column=4)

b4=Button(win,text="Update",width=12,command=update_command)
b4.grid(row=6,column=4)

b5=Button(win,text="Delete",width=12,command=delete_command)
b5.grid(row=7,column=4)

b6=Button(win,text="Close",width=12,command=win.destroy)
b6.grid(row=8,column=4)


win.mainloop()
