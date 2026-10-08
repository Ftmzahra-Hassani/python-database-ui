from tkinter import *
from tkinter import messagebox
from DATABASE import Database
db = Database()
database = db

win = Tk()
win.geometry("700x500")
win.resizable(False , False)
win.config(bg="#005a52")

#function
def populate_list():
    lst.delete(0 , END)
    for row in db.fetch():
        lst.insert(END , row)

def add_item():
    if ent_name.get() =='' or ent_lname.get()=='' or ent_add.get()=='' or ent_phone.get()=='':
        messagebox.showerror("Error" , "لطفا همه ورودی هارا پر کنید")
        return
    db.insert(ent_name.get() , ent_lname.get() , ent_add.get() , ent_phone())
    clear()
    populate_list()
def fetch(event):
        index = lst.curselection()
        if index:
             record = lst.get(index[0])
             ent_name.delete(0 , END)
             ent_name.insert(END , record[1])
             ent_lname.delete(0 , END)
             ent_lname.insert(END , record[2])
             ent_add.delete(0 , END)
             ent_add.insert(END , record[3])
             ent_phone.delete(0 , END)
             ent_phone.insert(END , record[4])

def update():
    index = lst.curselection()
    if index:
         record = lst.get(index[0])
         name = ent_name.get()
         lname = ent_lname.get()
         phone = ent_phone.get()
         address = ent_add.get()
         database.update(record[0],name , lname ,address , phone)

         show()
         clear()

def delete():
     index = lst.curselection()
     if index:
          record = lst.get(index[0])
          database.delete_user(record[0])
          show()
          clear()

def clear():
    ent_name.delete(0,END)
    ent_lname.delete(0,END)
    ent_add.delete(0,END)
    ent_phone.delete(0,END)
    ent_name.focus_set()

def exit():
    result=messagebox.askquestion("exit","Are you sure to exit?")
    if result=="yes":
        win.destroy()

def serch():
     text = ent_serch.get()
     lst.delete(0 , END)

     records = database.serch_user(text)
     for record in records:
          lst.insert(END , record)

def show():
     lst.delete(0 , END)
     records = database.show_users()

     for record in records:
          lst.insert(END , record)

def add():
     name=ent_name.get()
     lname=ent_lname.get()
     address=ent_add.get()
     phone=ent_phone.get()

     database.add_user(name , lname , address , phone)
    
     show()



#widget
sb = Scrollbar(win , orient=VERTICAL)
sb.place(x=668 , y=170 , height=150)

lst = Listbox(win , width=110 , yscrollcommand=sb.set)
lst.place(x=5 , y=169 , height=152 )

lst.configure(yscrollcommand= sb.set)
sb.configure(command=lst.yview)

lbl_name=Label(win , text="Frist name: " , font="arial 15 bold" , width=12)
lbl_name.place(x=5 , y=10)

lbl_lname = Label(win , text="Last name: " , font="arial 15 bold" , width=12)
lbl_lname.place(x=5 , y=50)

lbl_add=Label(win , text="Address: " , font="arial 15 bold" , width=12)
lbl_add.place(x=5 , y=90)

lbl_phone=Label(win , text="Phone: " , font="arial 15 bold" , width=12)
lbl_phone.place(x=5 , y=130)

lbl_serch=Label(win , text="Serch :" , font="arial 15 bold" , width=19)
lbl_serch.place(x=5 , y=333 , height=40)

ent_name=Entry(win , width=82)
ent_name.place(x=170 , y=15 , height=25)

ent_lname=Entry(win , width=82)
ent_lname.place(x=170 , y=55 , height=25)

ent_add=Entry(win , width=82)
ent_add.place(x=170 , y=95 , height=25)

ent_phone=Entry(win , width=82)
ent_phone.place(x=170 , y=135 , height=25)

ent_serch=Entry(win , width=66)
ent_serch.place(x=269 , y=333 , height=38)

btn_update=Button(win , text="Update" , font="arial 15 bold",width=12 , command=update)
btn_update.place(x=5 , y=390)

btn_add=Button(win , text="Add" , font="arial 15 bold" , width=12 , command=add)
btn_add.place(x=175, y=390)

btn_clear=Button(win , text="Clear" , font="arial 15 bold" , width=12 , command=clear)
btn_clear.place(x=345 , y=390)

btn_delete=Button(win , text="Delete" , font="arial 15 bold" , width=12 , command=delete)
btn_delete.place(x=515 , y=390)

btn_show=Button(win , text="Show" , font="arial 15 bold" , width=12 , command=show)
btn_show.place(x=5 , y=440)

btn_exit=Button(win , text="Exit" , font="arial 15 bold", width=12 , command=exit)
btn_exit.place(x=515 , y=440)

lst.bind("<<ListboxSelect>>" , fetch)


win.mainloop()