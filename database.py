from customtkinter import *
from tkinter import messagebox
import sqlite3

con=sqlite3.connect('orphanage.db')

def insert():
    con=sqlite3.connect('orphanage.db')
    child=child_id_entry.get()
    age=age_entry.get()
    name=name_entry.get().capitalize()
    gender=gender_entry.get().upper()



    ins='''
 INSERT INTO Orphas_child (child_id,age,name,gender) VALUES(?,?,?,?)

 '''
    
    if not child or not age or not name or not gender:
         messagebox.showerror('ALL feild must be filled')
         
    else:
         con.execute(ins,(child,age,name,gender))
    
    con.commit()
        
    child_id_entry.delete(0,END)
    age_entry.delete(0,END)
    name_entry.delete(0,END)
    gender_entry.delete(0,END)
    messagebox.showinfo('Data inserted')
    con.close()




def delete():
    con=sqlite3.connect('orphanage.db')
    child=child_id_entry.get()
 
    deli='''
      DELETE FROM Orphas_child where child_id=?
     
      '''

    con.execute(deli,(child,))
    con.commit()
    con.close()


def display():
       con=sqlite3.connect('orphanage.db')
   
       rows=con.execute('select * from Orphas_child')
    
       for i in rows:
           display_place.insert(END, f'ID: {i[0]}, Age: {i[1]}, Name: {i[2]}, Gender: {i[3]}\n')
           
           
        



def modify():
     con=sqlite3.connect('orphanage.db')
     child=child_id_entry.get()
     age=age_entry.get()
     name=name_entry.get()
     gender=gender_entry.get()
     ins='''
    UPDATE Orphas_child SET age=?,name=?,gender=? where child_id=?
 '''

     con.execute(ins,(age,name,gender,child))
     con.commit()
     con.close





roots=CTk()
roots.geometry('500x350')

roots.title('AanathAshram')

lab=CTkFrame(master=roots)
lab.place(y=100,x=400)
CTkLabel(lab, text='Child ID').grid(row=0, column=0, padx=10, pady=10)
child_id_entry = CTkEntry(lab)
child_id_entry.grid(row=0, column=1, padx=10, pady=10)

CTkLabel(lab, text='Age').grid(row=1, column=0, padx=10, pady=10)
age_entry = CTkEntry(lab)
age_entry.grid(row=1, column=1, padx=10, pady=10)
CTkLabel(lab, text='Name').grid(row=2, column=0, padx=10, pady=10)
name_entry = CTkEntry(lab)
name_entry.grid(row=2, column=1, padx=10, pady=10)
CTkLabel(lab, text='Gender').grid(row=3, column=0, padx=10, pady=10)
gender_entry = CTkEntry(lab)
gender_entry.grid(row=3, column=1, padx=10, pady=10)

button1=CTkButton(roots,text='Insert',command=insert)
button1.place(x=370,y=300)
button2=CTkButton(roots,text='Display',command=display)
button2.place(x=525,y=300)
display_place=CTkTextbox(roots,height=150,width=400)
display_place.place(x=310,y=400)

button3=CTkButton(roots,text='Modify',command=modify)
button3.place(x=370,y=335)
button4=CTkButton(roots,text='delete',command=delete)
button4.place(x=525,y=335)

dis_centre=CTkLabel(roots,text='Display centre:')
dis_centre.place(x=310,y=375)

roots.mainloop()