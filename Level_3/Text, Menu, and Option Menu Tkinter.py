import tkinter
from tkinter import *
import wikipedia
from tkinter import filedialog as fd
from tkinter import messagebox
root = Tk ()
root.title ('Screen')
#root.geometry ('600x600')

##def submit ():
##    info = wikipedia.summary (e1.get (),sentences = 1)
##    tb1 = Text (root)
##    tb1.insert (END,info)
##    tb1.grid (row = 1,columnspan = 3)
##l1 = Label (root,text = 'Search').grid ()
##e1 = Entry (root)
##e1.grid (row = 0,column = 1)
##b1 = Button (root,text = 'Submit',command = submit)
##b1.grid (row = 0,column = 2)

#For Challenge, not sure how to configure other parts of the Textbox
##def newf ():
##    global fname
##    fname = None
##    t1.delete ('1.0','end')
##def openf ():
##    global fname
##    fname = fd.askopenfilename ()
##    file1 = open (fname,'r')
##    t1.delete ('1.0','end')
##    t1.insert ('1.0',file1.read ())
##    file1.close ()
##def savef ():
##    global fname
##    if fname != None:
##            fname = fd.asksaveasfilename ()
##    file1 = open (fname + '.txt','w')
##    file1.write (t1.get ('1.0','end'))
##    file1.close ()
##def exitf ():
##    exit ()
##def aboutf ():
##    messagebox.showinfo ('About','This is a custom made notepad.\nThis allows you to create new files.\nYou can modify an existing file as well.')
##def conf ():
##    font1 = (input ('Font - '),int (input ('Size - ')))
##    fg1 = input ('Text Color - ')
##    bg1 = input ('Background Color - ')
##    t1.configure (font = font1,fg = fg1,bg = bg1)
##mb1 = Menu (root)
##filemenu = Menu (mb1,tearoff = 0)
##filemenu.add_command (label = 'New',command = newf)
##filemenu.add_command (label = 'Open',command = openf)
##filemenu.add_command (label = 'Save',command = savef)
##filemenu.add_separator ()
##filemenu.add_command (label = 'Exit',command = exitf)
##mb1.add_cascade (label = 'File',menu = filemenu)
##optmenu = Menu (mb1,tearoff = 0)
##optmenu.add_command (label = 'Configure Notepad',command = conf)
##mb1.add_cascade (label = 'Options',menu = optmenu)
##helpmenu = Menu (mb1,tearoff = 0)
##helpmenu.add_command (label = 'About',command = aboutf)
##mb1.add_cascade (label = 'Help',menu = helpmenu)
##t1 = Text (root,width = 50,height = 100)
##t1.grid ()
##root.config (menu = mb1)

##mvar = StringVar ()
##dvar = StringVar ()
##yvar = StringVar ()
##nl = Label (root,text = 'Name').grid ()
##ne = Entry (root)
##ne.grid (row = 0,column = 1,columnspan = 3)
##dm = Label (root,text = 'Month').grid (row = 1,column = 1)
##dd = Label (root,text = 'Day').grid (row = 1,column = 2)
##dy = Label (root,text = 'Year').grid (row = 1,column = 3)
##dl = Label (root,text = 'Date of Birth').grid (row = 2)
##l1 = [1,2,3,4,5,6,7,8,9,10,11,12]
##l2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
##l3 = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]
##om1 = OptionMenu (root,mvar,*l1).grid (row = 2,column = 1)
##om2 = OptionMenu (root,dvar,*l2).grid (row = 2,column = 2)
##om3 = OptionMenu (root,yvar,*l3).grid (row = 2,column = 3)
##el = Label (root,text = 'Email-ID').grid (row = 3)
##ee = Entry (root)
##ee.grid (row = 3,column = 1,columnspan = 3)
##pl = Label (root,text = 'Password').grid (row = 4)
##pe = Entry (root,show = '*')
##pe.grid (row = 4,column = 1,columnspan = 3)
##cpl = Label (root,text = 'Confirm Password').grid (row = 5)
##cpe = Entry (root,show = '*')
##cpe.grid (row = 5,column = 1,columnspan = 3)
##def create ():
##    if ne.get () == '' or mvar.get () == '' or dvar.get () == '' or yvar.get () == '' or ee.get () == '' or pe.get () == '' or cpe.get () == '':
##        messagebox.showerror ('Error','At least one of the entry fields is not filled in.')
##    else:
##        if pe.get () == cpe.get ():
##            file1 = open ('Menu_Registration.txt','a+')
##            file1.write (ne.get () + ' ' + mvar.get () + '/' + dvar.get () + '/' + yvar.get () + ' ' + ee.get () + ' ' + pe.get () + '\n')
##            file1.close ()
##            messagebox.showinfo ('Success','Registration complete.')
##        else:
##            messagebox.showerror ('Error','Passwords do not match.')
##b1 = Button (root,text = 'Create Account',command = create).grid (row = 6,column = 0,columnspan = 4)

#List Comprehension
##l4 = [i for i in range (0,100,5)]
##print (l4)
##l5 = [j for j in range (0,100,1) if j % 2 == 0]
##print (l5)

root.mainloop ()
