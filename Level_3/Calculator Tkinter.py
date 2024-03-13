import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk ()
root.title ('Screen')

f2 = Frame (root)
str1 = ''
e1 = Entry (f2)
e1.grid (columnspan = 4)
str1 = ''

histcond = False
f1 = Frame (root)
scroll = Scrollbar (f1,orient = VERTICAL)
lb1 = Listbox (f1,height = 5,yscrollcommand = scroll.set)
lb1.pack (side = LEFT)
scroll.config (command = lb1.yview)
scroll.pack (side = RIGHT)
class cbutton:
    def __init__ (self,n,rnum,cnum,cspan):
        self.name = n
        self.r = rnum
        self.c = cnum
        self.cspan = cspan
    def bclicked (self):
        global str1,e1,f1,lb1,histcond
        if self.name == '=': #Scrollbar doesn't show any equations
            str1 = e1.get ()
            try:
                result = eval (str1)
                print (result)
                lb1.insert ('end',str1)
                e1.delete (0,'end')
                str1 = result
            except:
                pass
        elif self.name == '⌫':
            try:
                eqlist = list (str1)
                eqlist.pop (len (eqlist) - 1)
                str1 = ''.join (eqlist)
                e1.delete (0,'end')
                e1.insert (0,str1)
            except:
                pass
        elif self.name == 'C':
            str1 = ''
        elif self.name == 'History':
            histcond = not (histcond)
            print ('histcond',histcond)
            if histcond == True:
                f2.pack_forget ()
                f1.pack ()
                f2.pack ()
                print ('Showing frame')
            else:
                f1.pack_forget ()
                f2.pack_forget ()
                f2.pack ()
                print ('Hiding frame')
        else:
            str1 = e1.get () + self.name
        e1.delete (0,'end')
        e1.insert (0,str1)
    def draw (self):
        self.b = Button (f2,text = self.name,command = self.bclicked)
        self.b.grid (row = self.r,column = self.c,columnspan = self.cspan)

b1 = cbutton ('1',2,0,1)
b2 = cbutton ('2',2,1,1)
b3 = cbutton ('3',2,2,1)
b4 = cbutton ('4',3,0,1)
b5 = cbutton ('5',3,1,1)
b6 = cbutton ('6',3,2,1)
b7 = cbutton ('7',4,0,1)
b8 = cbutton ('8',4,1,1)
b9 = cbutton ('9',4,2,1)
bpoint = cbutton ('.',5,0,1)
b0 = cbutton ('0',5,1,1)
beq = cbutton ('=',5,2,1)
bhist = cbutton ('History',1,0,2)
bback = cbutton ('⌫',1,2,1)
bC = cbutton ('C',1,3,1)
bplus = cbutton ('+',2,3,1)
bminus = cbutton ('-',3,3,1)
bmult = cbutton ('*',4,3,1)
bdiv = cbutton ('/',5,3,1)

b1.draw ()
b2.draw ()
b3.draw ()
b4.draw ()
b5.draw ()
b6.draw ()
b7.draw ()
b8.draw ()
b9.draw ()
bpoint.draw ()
b0.draw ()
beq.draw ()
bhist.draw ()
bback.draw ()
bC.draw ()
bplus.draw ()
bminus.draw ()
bmult.draw ()
bdiv.draw ()
f2.pack (side = TOP)

while True:
    selection = lb1.curselection () #contains indices of lines selected
    if len (selection) > 0:
        selequation = lb1.get (selection [0])
        print (selequation)
        e1.delete (0,'end')
        e1.insert (0,selequation)
        str1 = selequation
        lb1.selection_clear (0,'end')
    root.update ()
root.mainloop ()
