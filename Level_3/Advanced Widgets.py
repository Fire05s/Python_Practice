import tkinter
from tkinter import *

from tkinter import ttk

root = Tk ()
root.title ('Screen')
root.geometry ('600x600')

##ans = StringVar ()
##scr = IntVar ()
##def display ():
##    def ansf11 ():
##        ans.set ('Correct')
##        scr.set (scr.get () + 1)
##    def ansf12 ():
##        ans.set ('Incorrect')
##    def ansf21 ():
##        ans.set ('Incorrect')
##    def ansf22 ():
##        ans.set ('Correct')
##        scr.set (scr.get () + 1)
##    def ansf23 ():
##        ans.set ('Incorrect')
##    def ansf31 ():
##        ans.set ('Incorrect')
##    def ansf32 ():
##        ans.set ('Incorrect')
##    def ansf33 ():
##        ans.set ('Incorrect')
##    def ansf34 ():
##        ans.set ('Correct')
##        scr.set (scr.get () + 1)
##        
##    n1.add (f1,text = 'One')
##    n1.add (f2,text = 'Two')
##    n1.add (f3,text = 'Three')
##    
##    l1 = Label (f1,textvariable = ans)
##    l2 = Label (f2,textvariable = ans)
##    l3 = Label (f3,textvariable = ans)
##    l1.pack ()
##    l2.pack ()
##    l3.pack ()
##    l4 = Label (f1,textvariable = scr)
##    l5 = Label (f2,textvariable = scr)
##    l6 = Label (f3,textvariable = scr)
##    
##    q1 = Label (f1,text = '1 + 1 = ?')
##    b1 = Button (f1,text = '2',command = ansf11)
##    b2 = Button (f1,text = '11',command = ansf12)
##    q1.pack ()
##    b1.pack ()
##    b2.pack ()
##    l4.pack ()
##    
##    q2 = Label (f2,text = '5 * 1 = ?')
##    b1 = Button (f2,text = '6',command = ansf21)
##    b2 = Button (f2,text = '5',command = ansf22)
##    b3 = Button (f2,text = '51',command = ansf23)
##    q2.pack ()
##    b1.pack ()
##    b2.pack ()
##    b3.pack ()
##    l5.pack ()
##
##    q3 = Label (f3,text = '1 / 0 = ?')
##    b1 = Button (f3,text = '0',command = ansf31)
##    b2 = Button (f3,text = '1',command = ansf32)
##    b3 = Button (f3,text = '2',command = ansf33)
##    b4 = Button (f3,text = 'Undefined',command = ansf34)
##    q3.pack ()
##    b1.pack ()
##    b2.pack ()
##    b3.pack ()
##    b4.pack ()
##    l6.pack ()
##    
##    n1.pack ()
##n1 = ttk.Notebook (root)
##f1 = ttk.Frame (n1,width = 600,height = 600)
##f2 = ttk.Frame (n1,width = 600,height = 600)
##f3 = ttk.Frame (n1,width = 600,height = 600)
##display ()

##from Contacts import *
##def main ():
##    global lb1,n1,p1 #?
##    n1 = StringVar ()
##    p1 = StringVar ()
##    f1 = Frame (root,width = 600,height = 100,bg = 'gray')
##    l1 = Label (f1,text = 'Name: ')
##    e1 = Entry (f1,textvariable = n1)
##    l2 = Label (f1,text = 'Number: ')
##    e2 = Entry (f1,textvariable = p1)
##    f1.pack ()
##    l1.place (x = 0,y = 0)
##    e1.place (x = 70,y = 0)
##    l2.place (x = 0,y = 30)
##    e2.place (x = 70,y = 30)
##    f2 = Frame (root,width = 600,height = 50,bg = 'white')
##    b1 = Button (f2,text = 'Add',command = add)
##    b2 = Button (f2,text = 'Update',command = update)
##    b3 = Button (f2,text = 'Load',command = load)
##    b4 = Button (f2,text = 'Delete',command = delete)
##    f2.pack ()
##    b1.place (x = 0,y = 0)
##    b2.place (x = 50,y = 0)
##    b3.place (x = 100,y = 0)
##    b4.place (x = 150, y = 0)
##    f3 = Frame (root,width = 600,height = 450,bg = 'gray')
##    scr = Scrollbar (f3,orient = VERTICAL)
##    lb1 = Listbox (f3,height = 2,width = 15,yscrollcommand = scr.set)
##    scr.config (command = lb1.yview)
##    f3.pack ()
##    lb1.place (x = 25,y = 0)
##    scr.place (x = 120,y = 15)
##def select ():
##    lb1.delete (0,END)
##    clist.sort ()
##    for name,num in clist:
##         lb1.insert (END,name)
##def delete ():
##    del clist [lb1.curselection () [0]]
##    select ()
##def add ():
##    clist.append ([n1.get (),p1.get ()])
##    select ()
##def load ():
##    e1,e2 = clist [lb1.curselection () [0]]
##    n1.set (e1)
##    p1.set (e2)
##def update ():
##    clist [lb1.curselection () [0]] = [n1.get (),p1.get ()]
##    select ()
##main ()
##select ()

##def name (n):
##    l1 ['text'] = n
##l1 = Label (root,text = '')
##b1 = Button (root,text = 'B1',command = lambda : name ('Hello'))
##b2 = Button (root,text = 'B2',command = lambda : name ('Bye'))
##l1.grid (row = 0,column = 1)
##b1.grid (row = 1)
##b2.grid (row = 1,column = 1)

def idone (i,d,s1,s2):
    i.pack_forget ()
    d.pack_forget ()
    s1.pack ()
    s2.pack ()
def info (x,y,i,b):
    x.pack_forget ()
    y.pack_forget ()
    i.pack ()
    b.pack ()
def display ():
    n1.add (f1,text = 'Country')
    n1.add (f2,text = 'Capital')
    n1.add (f3,text = 'Cuisine')

    b1.pack ()
    b2.pack ()
    b3.pack ()
    b4.pack ()
    b5.pack ()
    b6.pack ()

    n1.pack ()
    
n1 = ttk.Notebook (root)
f1 = ttk.Frame (n1,width = 600,height = 600)
f2 = ttk.Frame (n1,width = 600,height = 600)
f3 = ttk.Frame (n1,width = 600,height = 600)

usi = Label (f1,text = 'The United States of America lies at the center of the continent of North America.')
b11 = Button (f1,text = 'Done?',command = lambda : idone (usi,b11,b1,b2))
rsi = Label (f1,text = 'Russia lies in an area known as Eurasia, approximately between Asia and Europe.')
b12 = Button (f1,text = 'Done?',command = lambda : idone (rsi,b12,b1,b2))

usc = Label (f2,text = 'The capital of the USA is the District of Columbia or Washington, DC.')
b21 = Button (f2,text = 'Done?',command = lambda : idone (usc,b21,b3,b4))
rsc = Label (f2,text = 'The capital of Russia is Moscow.')
b22 = Button (f2,text = 'Done?',command = lambda : idone (rsc,b22,b3,b4))

ucu = Label (f3,text = 'The cuisine of the USA is a mixture of many immigrants\' native cultures and adaptations of these foods.')
b31 = Button (f3,text = 'Done?',command = lambda : idone (ucu,b31,b5,b6))
rcu = Label (f3,text = 'The cuisine of Russia is an adaptation of European foods in soup dishes and other types of food.')
b32 = Button (f3,text = 'Done?',command = lambda : idone (rcu,b32,b5,b6))

b1 = Button (f1,text = 'USA',command = lambda : info (b1,b2,usi,b11))
b2 = Button (f1,text = 'Russia',command = lambda : info (b1,b2,rsi,b12))
b3 = Button (f2,text = 'US Capital',command = lambda : info (b3,b4,usc,b21))
b4 = Button (f2,text = 'Russian Capital',command = lambda : info (b3,b4,rsc,b22))
b5 = Button (f3,text = 'US Cuisine',command = lambda : info (b5,b6,ucu,b31))
b6 = Button (f3,text = 'Russian Cuisine',command = lambda : info (b5,b6,rcu,b32))

display ()

root.mainloop ()
