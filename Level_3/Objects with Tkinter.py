import tkinter,time
from tkinter import *
root = Tk ()
root.title ('Screen')
#root.geometry ('600x600')

##class widg ():
##    def __init__ (self,t):
##        self.b1 = Button (root,text = t)
##    def display (self,r = 0,c = 0):
##        self.b1.pack ()
##        self.b1.grid (row = r,column = c)
##b11 = widg ('Hello')
##b12 = widg ('Bye')
##b11.display ()
##b12.display (0,1)

##timet = 0
##timev = IntVar ()
##timev.set (timet)
##contin = False
##class timer ():
##    def __init__ (self,t,f):
##        self.b = Button (root,text = t,command = f)
##    def display (self,r = 0,c = 0,cs = 0):
##        self.b.grid (row = r,column = c,columnspan = cs)
##def go ():
##    global contin,timet
##    contin = True
##    while contin == True:
##        timet = timet + 1
##        timev.set (timet)
##        print (timet)
##        root.update ()
##        time.sleep (1)
##def reset ():
##    global contin,timet
##    contin = False
##    timet = 0
##    timev.set (0)
##    root.update ()
##b1 = timer ('Start',go)
##b2 = timer ('Reset',reset)
##l1 = Label (root,textvariable = timev)
##l1.grid (columnspan = 4)
##b1.display (1,0,2)
##b2.display (1,2,2)

##operation = 0
##n1 = ''
##n2 = ''
##sol = 0
##tn1 = StringVar ()
##tn2 = StringVar ()
##op1 = StringVar ()
##s1 = StringVar ()
##class button ():
##    def __init__ (self,t,r,c):
##        self.text = t
##        self.row = r
##        self.column = c
##    def display (self):
##        self.b1 = Button (root,text = self.text,command = self.click)
##        self.b1.grid (row = self.row,column = self.column)
##    def click (self):
##        global operation,n1,n2,sol
##        if self.text == '+' or self.text == '-' or self.text == '*' or self.text == '/':
##            operation = self.text
##            print (operation)
##            op1.set (operation)
##        if operation == 0:
##            n1 = n1 + str (self.text)
##            print (n1)
##            tn1.set (n1)
##        if operation != 0 and (type (self.text) == int or self.text == '.'):
##            n2 = n2 + str (self.text)
##            print (n2)
##            tn2.set (n2)
##        if self.text == '=':
##            if n2 != '':
##                if operation == '+':
##                    sol = float (n1) + float (n2)
##                    print (sol)
##                    s1.set (sol)
##                    n1 = ''
##                    n2 = ''
##                    operation = 0
##                    tn1.set (n1)
##                    tn2.set (n2)
##                    op1.set ('')
##                if operation == '-':
##                    sol = float (n1) - float (n2)
##                    print (sol)
##                    s1.set (sol)
##                    n1 = ''
##                    n2 = ''
##                    operation = 0
##                    tn1.set (n1)
##                    tn2.set (n2)
##                    op1.set ('')
##                if operation == '*':
##                    sol = float (n1) * float (n2)
##                    print (sol)
##                    s1.set (sol)
##                    n1 = ''
##                    n2 = ''
##                    operation = 0
##                    tn1.set (n1)
##                    tn2.set (n2)
##                    op1.set ('')
##                if operation == '/:':
##                    sol = float (n1) / float (n2)
##                    print (sol)
##                    s1.set (sol)
##                    n1 = ''
##                    n2 = ''
##                    operation = 0
##                    tn1.set (n1)
##                    tn2.set (n2)
##                    op1.set ('')

##        if n1 == '' and operation == 0:
##            if self.text == '0':
##                n1 = '0'
##                print (n1,n2)
##            elif self.text == '1':
##                n1 = '1'
##                print (n1,n2)
##            elif self.text == '2':
##                n1 = '2'
##                print (n1,n2)
##            elif self.text == '3':
##                n1 = '3'
##                print (n1,n2)
##            elif self.text == '4':
##                n1 = '4'
##                print (n1,n2)
##            elif self.text == '5':
##                n1 = '5'
##                print (n1,n2)
##            elif self.text == '6':
##                n1 = '6'
##                print (n1,n2)
##            elif self.text == '7':
##                n1 = '7'
##                print (n1,n2)
##            elif self.text == '8':
##                n1 = '8'
##                print (n1,n2)
##            elif self.text == '9':
##                n1 = '9'
##                print (n1,n2)
##            elif self.text == '.':
##                n1 = '.'
##                print (n1,n2)
##        elif n1 != '' and operation == 0:
##            if self.text == '0':
##                n1 = n1 + '0'
##                print (n1,n2)
##            elif self.text == '1':
##                n1 = n1 + '1'
##                print (n1,n2)
##            elif self.text == '2':
##                n1 = n1 + '2'
##                print (n1,n2)
##            elif self.text == '3':
##                n1 = n1 + '3'
##                print (n1,n2)
##            elif self.text == '4':
##                n1 = n1 + '4'
##                print (n1,n2)
##            elif self.text == '5':
##                n1 = n1 + '5'
##                print (n1,n2)
##            elif self.text == '6':
##                n1 = n1 + '6'
##                print (n1,n2)
##            elif self.text == '7':
##                n1 = n1 + '7'
##                print (n1,n2)
##            elif self.text == '8':
##                n1 = n1 + '8'
##                print (n1,n2)
##            elif self.text == '9':
##                n1 = n1 + '9'
##                print (n1,n2)
##            elif self.text == '.':
##                n1 = n1 + '.'
##                print (n1,n2)
##        if n2 == '' and operation != 0:
##            if self.text == '0':
##                n2 = '0'
##                print (n1,n2)
##            elif self.text == '1':
##                n2 = '1'
##                print (n1,n2)
##            elif self.text == '2':
##                n2 = '2'
##                print (n1,n2)
##            elif self.text == '3':
##                n2 = '3'
##                print (n1,n2)
##            elif self.text == '4':
##                n2 = '4'
##                print (n1,n2)
##            elif self.text == '5':
##                n2 = '5'
##                print (n1,n2)
##            elif self.text == '6':
##                n2 = '6'
##                print (n1,n2)
##            elif self.text == '7':
##                n2 = '7'
##                print (n1,n2)
##            elif self.text == '8':
##                n2 = '8'
##                print (n1,n2)
##            elif self.text == '9':
##                n2 = '9'
##                print (n1,n2)
##            elif self.text == '.':
##                n2 = '.'
##                print (n1,n2)
##        elif n2 != '':
##            if self.text == '0':
##                n2 = n2 + '0'
##                print (n1,n2)
##            elif self.text == '1':
##                n2 = n2 + '1'
##                print (n1,n2)
##            elif self.text == '2':
##                n2 = n2 + '2'
##                print (n1,n2)
##            elif self.text == '3':
##                n2 = n2 + '3'
##                print (n1,n2)
##            elif self.text == '4':
##                n2 = n2 + '4'
##                print (n1,n2)
##            elif self.text == '5':
##                n2 = n2 + '5'
##                print (n1,n2)
##            elif self.text == '6':
##                n2 = n2 + '6'
##                print (n1,n2)
##            elif self.text == '7':
##                n2 = n2 + '7'
##                print (n1,n2)
##            elif self.text == '8':
##                n2 = n2 + '8'
##                print (n1,n2)
##            elif self.text == '9':
##                n2 = n2 + '9'
##                print (n1,n2)
##            elif self.text == '.':
##                n2 = n2 + '.'
##                print (n1,n2)
##        if self.text == '=' and n1 != '' and n2 != '' and operation != 0:
##            n1 = float (n1)
##            n2 = float (n2)
##            if operation == 1:
##                sol = n1 + n2
##                print (sol)
##                n1 = ''
##                n2 = ''
##                operation = 0
##            if operation == 2:
##                sol = n1 - n2
##                print (sol)
##                n1 = ''
##                n2 = ''
##                operation = 0
##            if operation == 3:
##                sol = n1 * n2
##                print (sol)
##                n1 = ''
##                n2 = ''
##                operation = 0
##            if operation == 4:
##                sol = n1 / n2
##                print (sol)
##                n1 = ''
##                n2 = ''
##                operation = 0

##b0 = button ('0')
##b1 = button ('1')
##b2 = button ('2')
##b3 = button ('3')
##b4 = button ('4')
##b5 = button ('5')
##b6 = button ('6')
##b7 = button ('7')
##b8 = button ('8')
##b9 = button ('9')
##b9.display (0,2)
##b8.display (0,1)
##b7.display ()
##b6.display (1,2)
##b5.display (1,1)
##b4.display (1,0)
##b3.display (2,2)
##b2.display (2,1)
##b1.display (2,0)
##b0.display (3,1)

##bplus = button ('+')
##bmin = button ('-')
##bmult = button ('*')
##bdiv = button ('/')
##bdec = button ('.')
##bequ = button ('=')
##bplus.display (0,3)
##bmin.display (1,3)
##bmult.display (2,3)
##bdec.display (3,2)
##bdiv.display (3,3)
##bequ.display (3)

##rnum = 0
##cnum = 0
##for loop in range (0,10,1):
##    b = button (loop,rnum,cnum)
##    b.display ()
##    cnum = cnum + 1
##    print ('column',cnum)
##    if cnum == 3:
##        cnum = 0
##        rnum = rnum + 1
##        print ('row',rnum)
##bplus = button ('+',0,3)
##bmin = button ('-',1,3)
##bmult = button ('*',2,3)
##bdiv = button ('/',3,3)
##bdec = button ('.',3,1)
##bequ = button ('=',3,2)
##bplus.display ()
##bmin.display ()
##bmult.display ()
##bdec.display ()
##bdiv.display ()
##bequ.display ()
##l1 = Label (root,textvariable = tn1)
##l2 = Label (root,textvariable = tn2)
##opl = Label (root,textvariable = op1)
##soll = Label (root,textvariable = s1)
##l1.grid (row = 1,column = 4)
##l2.grid (row = 1,column = 6)
##opl.grid (row = 1,column = 5)
##soll.grid (row = 2,column = 5)

root.mainloop ()
