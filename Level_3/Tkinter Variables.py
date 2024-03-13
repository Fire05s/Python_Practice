import tkinter,random
from tkinter import *
root = Tk ()
root.title ('Screen')
#root.geometry ('600x600')

##var1 = IntVar ()
##num = 0
##def add ():
##    global num
##    num = num + 1
##    var1.set (num)
##def sub ():
##    global num
##    num = num - 1
##    var1.set (num)
##b1 = Button (root,text = '+',command = add)
##b1.grid (pady = 10,padx = 5)
##b2 = Button (root,text = '-',command = sub)
##b2.grid (row = 0,column = 2,pady = 10,padx = 5)
##l1 = Label (root,textvariable = var1)
##l1.grid (row = 0,column = 1,pady = 10,padx = 5)

##list1 = ['Bob','Terry','Jim']
##rname = StringVar ()
##rname.set (random.choice (list1))
##print (rname.get ())
##def pickname ():
##    rname.set (random.choice (list1))
##    print (rname.get ())
##l1 = Label (root,textvariable = rname)
##l1.grid ()
##b1 = Button (root,text = 'Name',command = pickname)
##b1.grid (row = 1)

##var1 = Message (root,text = 'Hello, this is a very long line of text.')
##var1.pack ()

##def infoget ():
##    global name,num,bal,amount
##    name = e1.get ()
##    num = e2.get ()
##    bal = int (e3.get ())
##    amount = int (e4.get ())
##def withdraw ():
##    global bal,amount
##    infoget ()
##    bal = bal - amount
##    message.set ('Acc. Name : '+str(name)+'  Acc. No. : '+str(num)+'  Balance : '+str(bal))
##    e3.delete (0,END)
##    e3.insert (0,bal)
##    print (bal)
##def add ():
##    global bal,amount
##    infoget ()
##    bal = bal + amount
##    message.set ('Acc. Name: '+str(name)+'Acc. No.: '+str(num)+'Balance: '+str(bal))
##    e3.delete (0,END)
##    e3.insert (0,bal)
##    print (bal)
##l1 = Label (root,text = 'Account Name: ')
##l2 = Label (root,text = 'Acc No.: ')
##l3 = Label (root,text = 'Balance: ')
##l4 = Label (root,text = 'Amount: ')
##l1.grid ()
##l2.grid (row = 1)
##l3.grid (row = 2)
##l4.grid (row = 3)
##e1 = Entry (root)
##e2 = Entry (root)
##e3 = Entry (root)
##e4 = Entry (root)
##e1.grid (row = 0,column = 1)
##e2.grid (row = 1,column = 1)
##e3.grid (row = 2,column = 1)
##e4.grid (row = 3,column = 1)
##message = StringVar ()
##m1 = Message (root,textvariable = message)
##m1.grid (row = 0,column = 2,rowspan = 4)
##b1 = Button (root,text = 'Withdraw',command = withdraw)
##b2 = Button (root,text = 'Deposit',command = add)
##b1.grid (row = 4,column = 1)
##b2.grid (row = 4,column = 2)

##def mins ():
##    global time
##    time.set (round (int (e1.get ()) / 60,2))
##def hr ():
##    global time
##    time.set (round (int (e1.get ()) / 3600,2))
##time = DoubleVar ()
##l1 = Label (root,text = 'Time:')
##l2 = Label (root,textvariable = time)
##l1.grid ()
##l2.grid (row = 1,column = 1)
##e1 = Entry (root)
##e1.grid (row = 0,column = 1)
##b1 = Button (root,text = 'Minutes',command = mins)
##b2 = Button (root,text = 'Hours',command = hr)
##b1.grid (row = 2,column = 1)
##b2.grid (row = 2,column = 2)

##def rint ():
##    global numint
##    e1.delete (0,END)
##    numint.set (random.randint (0,100))
##    #e1.insert (0,numint.get ())
##def rfloat ():
##    global numfloat
##    e2.delete (0,END)
##    numfloat.set (random.uniform (0,100))
##    #e2.insert (0,numfloat.get ())
##numint = IntVar ()
##numfloat = DoubleVar ()
##l1 = Label (root,text = 'Integer:')
##l2 = Label (root,text=  'Float:')
##e1 = Entry (root,textvariable = numint)
##e2 = Entry (root,textvariable = numfloat)
##l1.grid ()
##l2.grid (row = 1)
##e1.grid (row = 0,column = 1)
##e2.grid (row = 1,column = 1)
##b1 = Button (root,text = 'Rand. Int.',command = rint)
##b2 = Button (root,text = 'Rand. Float',command = rfloat)
##b1.grid (row = 2)
##b2.grid (row = 2,column = 1)

root.mainloop ()
