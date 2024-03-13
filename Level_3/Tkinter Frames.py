import tkinter
from tkinter import *
from tkinter import messagebox
root = Tk ()
root.title ('Screen')
root.geometry ('600x600')

##var1 = Frame (root,width = 600,height = 200,bg = 'gray')
##var2 = Frame (root,width = 600,height = 200,bg = 'white')
##var3 = Frame (root,width = 600,height = 200,bg = 'gray')
##var1 = Frame (root,width = 200,height = 600,bg = 'gray')
##var2 = Frame (root,width = 200,height = 600,bg = 'white')
##var3 = Frame (root,width = 200,height = 600,bg = 'red')
##var1.pack ()
##var2.pack ()
##var3.pack ()
##var1.pack (side = LEFT)
##var2.pack (side = LEFT)
##var3.pack (side = LEFT)

##f1 = Frame (root,width = 600,height = 300,bg = 'red')
##f2 = Frame (root,width = 600,height = 300,bg = 'green')
##f3 = Frame (f1,width = 300,height = 300,bg = 'yellow')
##f4 = Frame (f2,width = 300,height = 300,bg = 'blue')
##b1 = Button (f1,text = 'Button')
##b2 = Button (f1,text = 'Button 2')
##b3 = Button (f2,text = 'Button 3')
##b4 = Button (f2,text = 'Button 4')
##f1.pack ()
##f2.pack ()
##f3.place (x = 0,y = 0)
##f4.place (x = 0,y = 0)
##b1.place (x = 0,y = 0)
##b2.place (x = 300,y = 0)
##b3.place (x = 0,y = 0)
##b4.place (x = 300,y = 0)

##result = DoubleVar ()
##var1 = DoubleVar ()
##var2 = DoubleVar ()
##def getval ():
##    global var1,var2
##    try:
##        if float (e1.get ()) % 1 == 0 and float (e2.get ()) % 1 == 0:
##            var1 = float (e1.get ())
##            var2 = float (e2.get ())
##    except:
##        messagebox.showwarning ('Error!','Please input an integer or decimal number, not a string.')
##    e1.delete (0,END)
##    e2.delete (0,END)
##def add ():
##    global var1,var2,result
##    getval ()
##    result.set (round (var1 + var2,3))
##def sub ():
##    global var1,var2,result
##    getval ()
##    result.set (round (var1 - var2,3))
##def mult ():
##    global var1,var2,result
##    getval ()
##    result.set (round (var1 * var2,3))
##def div ():
##    global var1,var2,result
##    getval ()
##    if var2 != 0:
##        result.set (round (var1 / var2,3))
##    else:
##        messagebox.showwarning ('Error!','You cannot divide by 0!')
##f1 = Frame (root,width = 600,height = 150,bg = 'gray')
##f2 = Frame (root,width = 600,height = 150,bg = 'white')
##f3 = Frame (root,width = 600,height = 150,bg = 'gray')
##f4 = Frame (root,width = 600,height = 150,bg = 'white')
##f1.pack ()
##f2.pack ()
##f3.pack ()
##f4.pack ()
##l1 = Label (f1,text = 'First Number:')
##e1 = Entry (f1)
##l1.place (x = 50,y = 60)
##e1.place (x = 225,y = 60)
##l2 = Label (f2,text = 'Second Number:')
##e2 = Entry (f2)
##l2.place (x = 50,y = 60)
##e2.place (x = 225,y = 60)
##b1 = Button (f3,text = '+',padx = 25,command = add)
##b2 = Button (f3,text = '-',padx = 25,command = sub)
##b3 = Button (f3,text = '*',padx = 25,command = mult)
##b4 = Button (f3,text = '/',padx = 25,command = div)
##b1.place (x = 50,y = 60)
##b2.place (x = 200,y = 60)
##b3.place (x = 350,y = 60)
##b4.place (x = 500,y = 60)
##l3 = Label (f4,text = 'Result:')
##l4 = Label (f4,textvariable = result)
##l3.place (x = 50,y = 60)
##l4.place (x = 225,y = 60)

##def clear ():
##    l1.grid_forget ()
##    b2 = Button (root,text = 'Hello Again')
##    b2.grid ()
##l1 = Label (root,text = 'Hello')
##l1.grid ()
##b1 = Button (root,text = 'Click Here',command = clear)
##b1.grid (row = 1)

##str1 = StringVar ()
##result = DoubleVar ()
##def basstr ():
##    def uppercase ():
##        string = e1.get ()
##        str1.set (string.upper ())
##    def lowercase ():
##        string = e1.get ()
##        str1.set (string.lower ())
##    f2.pack_forget ()
##    f3.pack_forget ()
##    f4.pack_forget ()
##    f1.pack ()
##    l1 = Label (f1,text = 'Enter a string: ')
##    e1 = Entry (f1)
##    l1.place (x = 75,y = 200)
##    e1.place (x = 200,y = 200)
##    b1 = Button (f1,text = 'Uppercase',command = uppercase)
##    b2 = Button (f1,text = 'Lowercase',command = lowercase)
##    b1.place (x = 100,y = 400)
##    b2.place (x = 200,y = 400)
##    l2 = Label (f1,textvariable = str1)
##    l2.place (x = 125,y = 300)
##def advstr ():
##    def length ():
##        string1 = e1.get ()
##        str1.set (str (len (string1)))
##    def compare ():
##        string1 = e1.get ()
##        string2 = e2.get ()
##        if len (string1) > len (string2):
##            str1.set ('The first string is greater than the second.')
##        elif len (string1) < len (string2):
##            str1.set ('The second string is greater than the first.')
##        else:
##            str1.set ('The strings are equal.')
##    f1.pack_forget ()
##    f3.pack_forget ()
##    f4.pack_forget ()
##    f2.pack ()
##    l1 = Label (f2,text = 'Enter a string: ')
##    e1 = Entry (f2)
##    l2 = Label (f2,text = 'Enter a second string: ')
##    e2 = Entry (f2)
##    l1.place (x = 75,y = 200)
##    e1.place (x = 200,y = 200)
##    l2.place (x = 75,y = 250)
##    e2.place (x = 200,y = 250)
##    b1 = Button (f2,text = 'Length',command = length)
##    b2 = Button (f2,text = 'Compare',command = compare)
##    b1.place (x = 100,y = 400)
##    b2.place (x = 200,y = 400)
##    l3 = Label (f2,textvariable = str1)
##    l3.place (x = 125,y = 300)
##def basnum ():
##    def add ():
##        num1 = float (e1.get ())
##        num2 = float (e2.get ())
##        result.set (round (num1 + num2,3))
##        e1.delete (0,END)
##        e2.delete (0,END)
##    def sub ():
##        num1 = float (e1.get ())
##        num2 = float (e2.get ())
##        result.set (round (num1 - num2,3))
##        e1.delete (0,END)
##        e2.delete (0,END)
##    f1.pack_forget ()
##    f2.pack_forget ()
##    f4.pack_forget ()
##    f3.pack ()
##    l1 = Label (f3,text = 'Enter a number: ')
##    e1 = Entry (f3)
##    l2 = Label (f3,text = 'Enter a second number: ')
##    e2 = Entry (f3)
##    l1.place (x = 75,y = 200)
##    e1.place (x = 250,y = 200)
##    l2.place (x = 75,y = 250)
##    e2.place (x = 250,y = 250)
##    b1 = Button (f3,text = 'Add',command = add)
##    b2 = Button (f3,text = 'Subtract',command = sub)
##    b1.place (x = 100,y = 400)
##    b2.place (x = 200,y = 400)
##    l3 = Label (f3,textvariable = result)
##    l3.place (x = 125,y = 300)
##def advnum ():
##    def sol ():
##        num1 = float (e1.get ())
##        num2 = float (e2.get ())
##        result.set (num1 // num2)
##        e1.delete (0,END)
##        e2.delete (0,END)
##    def rem ():
##        num1 = float (e1.get ())
##        num2 = float (e2.get ())
##        result.set (round (num1 % num2,3))
##        e1.delete (0,END)
##        e2.delete (0,END)
##    f1.pack_forget ()
##    f2.pack_forget ()
##    f3.pack_forget ()
##    f4.pack ()
##    l1 = Label (f4,text = 'Enter a number: ')
##    e1 = Entry (f4)
##    l2 = Label (f4,text = 'Enter a second number: ')
##    e2 = Entry (f4)
##    l1.place (x = 75,y = 200)
##    e1.place (x = 250,y = 200)
##    l2.place (x = 75,y = 250)
##    e2.place (x = 250,y = 250)
##    b1 = Button (f4,text = 'Solution Only',command = sol)
##    b2 = Button (f4,text = 'Remainder Only',command = rem)
##    b1.place (x = 100,y = 400)
##    b2.place (x = 200,y = 400)
##    l3 = Label (f4,textvariable = result)
##    l3.place (x = 125,y = 300)
##leftf = Frame (root,width = 100,height = 600,bg = 'gray')
##f1 = Frame (root,width = 500,height = 600,bg = 'white')
##f2 = Frame (root,width = 500,height = 600,bg = 'white')
##f3 = Frame (root,width = 500,height = 600,bg = 'white')
##f4 = Frame (root,width = 500,height = 600,bg = 'white')
##b1 = Button (leftf,text = 'Basic Strings',command = basstr)
##b2 = Button (leftf,text = 'Adv. Strings',command = advstr)
##b3 = Button (leftf,text = 'Basic Numbers',command = basnum)
##b4 = Button (leftf,text = 'Adv. Numbers',command = advnum)
##leftf.pack (side = LEFT)
##f1.pack (side = LEFT)
##b1.place (x = 10,y = 50)
##b2.place (x = 10,y = 200)
##b3.place (x = 10,y = 350)
##b4.place (x = 10,y = 500)

def correct ():
    ans.set ('Correct')
    scr.set (scr.get () + 1)
def wrong ():
    ans.set ('Incorrect')
def nextq ():
    global qnum
    if qnum == 1:
        qnum = 2
    elif qnum == 2:
        qnum = 3
    elif qnum == 3:
        qnum = 4
    elif qnum == 4:
        qnum = 5
    elif qnum == 5:
        messagebox.showinfo ('Stop!','You cannot go further than Question 5.')
def prev ():
    global qnum
    if qnum == 1:
        messagebox.showinfo ('Stop!','You cannot go back from Question 1.')
    elif qnum == 2:
        qnum = 1
    elif qnum == 3:
        qnum = 2
    elif qnum == 4:
        qnum = 3
    elif qnum == 5:
        qnum = 4
def showmain ():
    check = Label (main,textvariable = ans)
    score = Label (main,textvariable = scr)
    nxt = Button (main,text = 'Next',command = nextq)
    prv = Button (main,text = 'Previous',command = prev)
    main.pack ()
    check.pack ()
    score.pack ()
    nxt.pack ()
    prv.pack ()
def q1 ():
    f2.pack_forget ()
    f3.pack_forget ()
    f4.pack_forget ()
    f5.pack_forget ()
    main.pack_forget ()
    l11 = Label (f1,text = 'Q1: 1 + 1 = ?')
    b11 = Button (f1,text = '2',command = correct)
    b12 = Button (f1,text = '11',command = wrong)
    f1.pack ()
    l11.pack ()
    b11.pack ()
    b12.pack ()
    showmain ()
def q2 ():
    f1.pack_forget ()
    f3.pack_forget ()
    f4.pack_forget ()
    f5.pack_forget ()
    main.pack_forget ()
    l21 = Label (f2,text = 'Q2: 1 * 1 = ?')
    b21 = Button (f2,text = '1',command = correct)
    b22 = Button (f2,text = '2',command = wrong)
    f2.pack ()
    l21.pack ()
    b21.pack ()
    b22.pack ()
    showmain ()
def q3 ():
    f1.pack_forget ()
    f2.pack_forget ()
    f4.pack_forget ()
    f5.pack_forget ()
    main.pack_forget ()
    l31 = Label (f3,text = 'Q3: 3 * 7 =?')
    b31 = Button (f3,text = '37',command = wrong)
    b32 = Button (f3,text = '21',command = correct)
    f3.pack ()
    l31.pack ()
    b31.pack ()
    b32.pack ()
    showmain ()
def q4 ():
    f1.pack_forget ()
    f2.pack_forget ()
    f3.pack_forget ()
    f5.pack_forget ()
    main.pack_forget ()
    l41 = Label (f4,text = 'Q4: 13 * 31 = ?')
    b41 = Button (f4,text = '1',command = wrong)
    b42 = Button (f4,text = '403',command = correct)
    f4.pack ()
    l41.pack ()
    b41.pack ()
    b42.pack ()
    showmain ()
def q5 ():
    f1.pack_forget ()
    f2.pack_forget ()
    f3.pack_forget ()
    f4.pack_forget ()
    main.pack_forget ()
    l51 = Label (f5,text = 'Q5: 6 / 0 = ?')
    b51 = Button (f5,text = 'Undefined',command = correct)
    b52 = Button (f5,text = '0',command = wrong)
    f5.pack ()
    l51.pack ()
    b51.pack ()
    b52.pack ()
    showmain ()
ans = StringVar ()
scr = IntVar ()
qnum = 1
main = Frame (root,width = 200,height = 600,bg = 'white')
f1 = Frame (root,width = 400,height = 600,bg = 'gray')
f2 = Frame (root,width = 400,height = 600,bg = 'gray')
f3 = Frame (root,width = 400,height = 600,bg = 'gray')
f4 = Frame (root,width = 400,height = 600,bg = 'gray')
f5 = Frame (root,width = 400,height = 600,bg = 'gray')
print (qnum)
if qnum == 1:
    q1 ()
    print ('hello')
elif qnum == 2:
    q2 ()
    print ('hello2')
elif qnum == 3:
    q3 ()
elif qnum == 4:
    q4 ()
elif qnum == 5:
    q5 ()

root.mainloop ()
