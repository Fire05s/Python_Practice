import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk ()
root.title ('Screen')
#root.geometry ('600x600')
import pytz
from datetime import datetime

##l1 = Label (root,text = 'COLORS').grid ()
##lb1 = Listbox (root)
##lb1.grid (row = 1)
##lb1.insert (END,'white')
##lb1.insert (END,'red')
##lb1.insert (END,'green')
##lb1.insert (END,'blue')
##lb1.insert (END,'black')
##l2 = Label (root)
##l2.grid (row = 2,columnspan = 1)
##while True:
##    selection = lb1.curselection ()
##    if len (selection) > 0:
##        index = selection [0]
##        actual_value = lb1.get (index)
##        if actual_value == 'white':
##            l2 ['bg'] = 'white'
##        elif actual_value == 'red':
##            l2 ['bg'] = 'red'
##        elif actual_value == 'green':
##            l2 ['bg'] = 'green'
##        elif actual_value == 'blue':
##            l2 ['bg'] = 'blue'
##        elif actual_value == 'black':
##            l2 ['bg'] = 'black'
##    root.update ()

##l1 = Label (root,text = 'Choose any Timezone').pack ()
##timezones = pytz.all_timezones
##scroll = Scrollbar (root,orient = VERTICAL)
##lb1 = Listbox (root,height = 7)
##lb1.pack (side = LEFT,fill = BOTH,expand = 1)
##scroll.pack (side = RIGHT,fill = Y)
####lb1.grid (row = 1)
####scroll.grid (row = 1,column = 1,sticky = N)
##lb1.config (yscrollcommand = scroll.set)
##scroll.config (command = lb1.yview)
##for loop in timezones:
##    lb1.insert (END,loop)
##info = StringVar ()
##l2 = Label (root,textvariable = info).pack (side = BOTTOM)
##while True:
##    selection = lb1.curselection ()
##    if len (selection) > 0:
##        index = selection [0]
##        timezone = pytz.timezone (timezones [index])
##        current = datetime.now (timezone)
##        final_time = current.strftime('%d %b %Y %I:%M:%S %p %Z')
##        info.set (final_time)
##    root.update ()

file = open ('Example_Logins.txt','r')
n1 = ttk.Notebook (root)
f1 = ttk.Frame (n1)
f2 = ttk.Frame (n1)
f3 = ttk.Frame (n1)
f4 = ttk.Frame (n1)
n1.add (f1,text = 'Login')
n1.add (f2,text = 'Register')
n1.add (f3,text = 'Reset Password')
n1.add (f4,text = 'Unsubscribe')
n1.pack ()
logins = {}
for loop in file:
    print (loop,len (loop))
    loop = loop.strip ()
    user,password = loop.split ()
    logins [user] = password
ll1 = Label (f1,text = 'Username').grid ()
ll2 = Label (f1,text = 'Password').grid (row = 1)
le1 = Entry (f1)
le1.grid (row = 0,column = 1)
le2 = Entry (f1)
le2.grid (row = 1,column = 1)
def submit ():
    match = False
    for loop in logins:
        if le1.get () == loop and logins [loop] == le2.get ():
            match = True
    if match == True:
        messagebox.showinfo ('Login Success','Login has been successful.')
    if match == False:
        messagebox.showerror ('Login Failed','Username or password is incorrect.')
lb1 = Button (f1,text = 'Submit',command = submit)
lb1.grid (row = 2,columnspan = 2)
rl1 = Label (f2,text = 'Username').grid ()
rl2 = Label (f2,text = 'Password').grid (row = 1)
re1 = Entry (f2)
re1.grid (row = 0,column = 1)
re2 = Entry (f2)
re2.grid (row = 1,column = 1)
def register ():
    match = False
    for loop in logins:
        if re1.get () == loop:
            match = True
    if match == True:
        messagebox.showerror ('Register Failed','Username already taken.')
    if match == False:
        messagebox.showinfo ('Register Success','Register has been successful.')
        logins [re1.get ()] = re2.get ()
        newreg = open ('Example_Logins.txt','a+')
        newline = '\n' + re1.get () + ' ' + re2.get ()
        newreg.write (newline)
rb1 = Button (f2,text = 'Register',command = register)
rb1.grid (row = 2,columnspan = 2)
rsl1 = Label (f3,text = 'Username').grid ()
rsl2 = Label (f3,text = 'Password').grid (row = 1)
rse1 = Entry (f3)
rse1.grid (row = 0,column = 1)
rse2 = Entry (f3)
rse2.grid (row = 1,column = 1)
def reset ():
    match = False
    for loop in logins:
        if rse1.get () == loop:
            match = True
    if match == True:
        messagebox.showinfo ('Reset Success','Password has been changed.')
        logins [rse1.get ()] = rse2.get ()
        newres = open ('Example_Logins.txt','w')
        newres.write (rse1.get () + ' ' + rse2.get () + '\n')
    if match == False:
        messagebox.showerror ('Reset Failed','Username is incorrect.')
rsb1 = Button (f3,text = 'Reset',command = reset)
rsb1.grid (row = 2,columnspan = 2)
ul1 = Label (f4,text = 'Username').grid ()
ul2 = Label (f4,text = 'Password').grid (row = 1)
ue1 = Entry (f4)
ue1.grid (row = 0,column = 1)
ue2 = Entry (f4)
ue2.grid (row = 1,column = 1)
def unsub ():
    match = False
    for loop in logins:
        if ue1.get () == loop and logins [loop] == ue2.get ():
            match = True
    if match == True:
        messagebox.showinfo ('Login Success','Unsubscription has been successful.')
        del (logins [ue1.get ()])
        newreg = open ('Example_Logins.txt','w')
        for loop in logins:
            newline = loop + ' ' + logins [loop] + '\n'
            newreg.write (newline)
    if match == False:
        messagebox.showerror ('Login Failed','Username or password is incorrect.')
ub1 = Button (f4,text = 'Unsubscribe',command = unsub)
ub1.grid (row = 2,columnspan = 2)

root.mainloop ()
