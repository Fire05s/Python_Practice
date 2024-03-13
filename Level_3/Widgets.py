import tkinter,time,random
from tkinter import *
from tkinter import messagebox
root = Tk ()
root.title ('Screen')
#root.geometry ('600x600')

##label1 = Label (root,text = 'Label',relief = RIDGE) #flat,raised,groove,ridge,sunken
##label1.pack ()
##button1 = Button (root,text = 'Button',bg = 'gray',fg = 'white')
##button1.pack ()
##enter = Entry (root)
##enter.pack ()

##label2 = Label (root,text = 'Label2',relief = GROOVE)
##button2 = Button (root,text = 'Quit',bg = 'black',fg = 'white',command = exit,width = 10,height = 5)
##label2.pack ()
##button2.pack ()

##def enterinput ():
##    l1 ['text'] = entry1.get ()
##def clear ():
##    entry1.delete (0,END)
##    entry2.delete (0,END)
##l1 = Label (root,text = 'Entry 1:')
##l2 = Label (root,text = '')
##entry1 = Entry (root)
##entry2 = Entry (root,width = 10)
##l1.pack (side = LEFT) #top,bottom,left,right
##entry1.pack ()
##l2.pack ()
##entry2.pack ()
##b1 = Button (root,text = 'Change Label',bg = 'gray',fg = 'white',command = enterinput)
##b2 = Button (root,text = 'Clear Text',bg = 'gray',fg = 'white',command = clear)
##b3 = Button (root,text = 'Quit',bg = 'gray',fg = 'white',command = exit)
##b1.pack ()
##b2.pack ()
##b3.pack ()

##timevar = IntVar ()
##timevar = 0
##timecond = False
##stringvar = StringVar ()
##def start ():
##    global timevar,timecond
##    timecond = True
##    while timecond:
##        stringvar.set (timevar)
##        print (timevar)
##        timevar = timevar + 1
##        root.update ()
##        time.sleep (1)
##def reset ():
##    global timevar,timecond
##    timevar = 0
##    stringvar.set (timevar)
##    timecond = False
##    print (timevar)
##def stop ():
##    global timevar,timecond
##    timecond = False
##    root.update ()
##start = Button (root,text = 'Start Timer',bg = 'gray',fg = 'white',command = start)
##reset = Button (root,text = 'Reset Timer',bg = 'gray',fg = 'white',command = reset)
##stop = Button (root,text = 'Stop Timer',bg = 'gray',fg = 'white',command = stop)
##start.pack ()
##reset.pack ()
##stop.pack ()
##timelabel = Label (root,textvariable = stringvar)
##timelabel.pack ()

##l1 = Label (root,text = 'flat',relief = FLAT)
##l2 = Label (root,text = 'raised',relief = RAISED)
##l3 = Label (root,text = 'grooved',relief = GROOVE)
##l4 = Label (root,text = 'ridged',relief = RIDGE)
##l5 = Label (root,text = 'sunken',relief = SUNKEN)
##l1.pack (side = LEFT)
##l2.pack (side = LEFT)
##l3.pack (side = LEFT)
##l4.pack (side = LEFT)
##l5.pack (side = LEFT)

##b1 = Button (root,text = 'Row0,Col0',width = 10,height = 5)
##b1.grid ()
##b2 = Button (root,text = 'Row0,Col1',width = 10,height = 5)
##b2.grid (row = 0,column = 1)
##b3 = Button (root,text = 'Row1,Col0',width = 10,height = 5)
##b3.grid (row = 1)
##b4 = Button (root,text = 'Row1,Col1',width = 10,height = 5)
##b4.grid (row = 1,column = 1)
##b5 = Button (root,text = 'Row2,Col0',width = 10,height = 5)
##b5.grid (row = 2,column = 0)
##b6 = Button (root,text = 'Row2,Col1',width = 10,height = 5)
##b6.grid (row = 2,column = 1)

##def twitter ():
##    label ['text'] = '@TwitterAccount'
##def linkedin ():
##    label ['text'] = 'John'
##def youtube ():
##    label ['text'] = 'JohnYT'
##def facebook ():
##    label ['text'] = 'JohnS'
##twitterb = Button (root,text = 'Twitter',command = twitter)
##twitterb.grid ()
##linkedinb = Button (root,text = 'LinkedIn',command = linkedin)
##linkedinb.grid (row = 0,column = 1)
##youtubeb = Button (root,text = 'YouTube',command = youtube)
##youtubeb.grid (row = 1)
##facebookb = Button (root,text = 'Facebook',command = facebook)
##facebookb.grid (row = 1,column = 1)
##label = Label (root,text = '')
##label.grid (row = 2,columnspan = 2,sticky = 'W')

##b1 = Radiobutton (root,text = 'Option 1',value = 0)
##b1.pack ()
##b2 = Checkbutton (root,text = 'Check 1')
##b2.pack ()
##b3 = Radiobutton (root,text = 'Option 2',value = 1)
##b3.pack ()

##l1 = Label (root,text = 'Find: ')
##l2 = Label (root,text = 'Replace: ')
##e1 = Entry (root,width = 50)
##e2 = Entry (root,width = 50)
##b1 = Button (root,text = 'b1')
##b2 = Button (root,text = 'b2')
##b3 = Button (root,text = 'b3')
##b4 = Button (root,text = 'b4')
##cb1 = Checkbutton (root,text = 'cb1')
##cb2 = Checkbutton (root,text = 'cb2')
##cb3 = Checkbutton (root,text = 'cb3')
##rb1 = Radiobutton (root,text = 'rb1',value = 0)
##rb2 = Radiobutton (root,text = 'rb2',value = 1)
##rblabel = Label (root,text = 'Direction: ')
##
##l1.grid (sticky = 'W')
##l2.grid (row = 1,sticky = 'W')
##e1.grid (row = 0,column = 1,columnspan = 5)
##e2.grid (row = 1,column = 1,columnspan = 5)
##b1.grid (row = 0,column = 6)
##b2.grid (row = 1,column = 6)
##b3.grid (row = 2,column = 6)
##b4.grid (row = 3,column = 6)
##cb1.grid (row = 2,column = 1)
##cb2.grid (row = 3,column = 1)
##cb3.grid (row = 4,column = 1)
##rblabel.grid (row = 2,column = 2)
##rb1.grid (row = 3,column = 2)
##rb2.grid (row = 3,column = 3)

##def clear ():
##    namebox.delete (0,END)
##title = Label (root,text = 'Application Form',font=('Arial',12,'bold'))
##title.grid (columnspan = 3)
##namebox = Entry (root)
##namebox.grid (row = 1,column = 1,columnspan = 2)
##clearb = Button (root,text = 'Clear',command = clear)
##submitb = Button (root,text = 'Submit')
##clearb.grid (row = 2,column = 1)
##submitb.grid (row = 2,column = 2)
##namel = Label (root,text = 'Name: ')
##namel.grid (row = 1)

##def clear ():
##    fentry.delete (0,END)
##    centry.delete (0,END)
##def calculate ():
##    centry.delete (0,END)
##    fahr = int (fentry.get ())
##    cels = 5/9*(fahr-32)
##    centry.insert (0,cels)
##flab = Label (root,text = 'Fahrenheit: ')
##clab = Label (root,text = 'Celsius: ')
##flab.grid ()
##clab.grid (row = 1)
##fentry = Entry (root)
##centry = Entry (root)
##fentry.grid (row = 0,column = 1,columnspan = 2)
##centry.grid (row = 1,column = 1,columnspan = 2)
##clearb = Button (root,text = 'Clear',command = clear)
##clearb.grid (row = 2)
##calcb = Button (root,text = 'Calculate',command = calculate)
##calcb.grid (row = 2,column = 1)
##quitb = Button (root,text = 'Quit',command = quit)
##quitb.grid (row = 2,column = 2)

##def guess ():
##    global randn
##    guessn = int (e1.get ())
##    if guessn < randn:
##        #print ('Number entered is too low.')
##        messagebox.showinfo ('Number Low','Number entered is too low.')
##    elif guessn > randn:
##        #print ('Number entered is too high.')
##        messagebox.showinfo ('Number High','Number entered is too high.')
##    else:
##        #print ('Number entered is Correct! Resetting number... You may play again if you want.')
##        messagebox.showinfo ('Correct','Number entered is Correct! Resetting number... You may play again if you want.')
##        randn = random.randint (1,100)
##def clear ():
##    e1.delete (0,END)
##randn = random.randint (1,100)
##l1 = Label (root,text = 'Guess number from (1-100)')
##e1 = Entry (root)
##l1.grid ()
##e1.grid (row = 0,column = 1)
##b1 = Button (root,text = 'Guess Number',command = guess)
##b1.grid (row = 1)
##b2 = Button (root,text = 'Clear',command = clear)
##b2.grid (row = 1,column = 1)
##b3 = Button (root,text = 'Quit',command = quit)
##b3.grid (row = 1,column = 2)

##def check ():
##    euser = e1.get ()
##    epass = e2.get ()
##    if euser == username:
##        if epass == password:
##            print ('Access Granted')
##        else:
##            print ('Password is incorrect. Access Denied')
##    else:
##        print ('Username is incorrect. Access Denied')
##username = 'User'
##password = '12345'
##l1 = Label (root,text = 'Username')
##l2 = Label (root,text = 'Password')
##l1.grid ()
##l2.grid (row = 1)
##e1 = Entry (root)
##e2 = Entry (root,show = '*')
##e1.grid (row = 0,column = 1,columnspan = 3)
##e2.grid (row = 1,column = 1,columnspan = 3)
##b1 = Button (root,text = 'Login',command = check)
##b1.grid (row = 2,column = 3)

##messagebox.showwarning ("Warning","It could harm your system")
##messagebox.showinfo ("Message", "Your system is updated")
##messagebox.showerror("Error","Syntax Error")
##messagebox.askquestion("Confirm","Are you sure?")

##messagebox.askokcancel("Redirect","Redirecting you to www.javatpoint.com")
##messagebox.askyesno("Application","Got It?")  
##messagebox.askretrycancel("Application","Try Again?")

##def answer ():
##    var1 = messagebox.askquestion ('Popout','Submit Answer?')
##    if var1:
##        if var1 == 'yes':
##            messagebox.showwarning ('Popout: 2','Your answer has been submitted.')
##        elif var1 == 'no':
##            messagebox.askretrycancel ('Popout: 2','Try again.')
##def leave ():
##    if messagebox.askyesno ('Popout','Quit?'):
##        quit ()
##    else:
##        messagebox.showwarning ('Popout: 2','The Quit has been cancelled.')
##b1 = Button (root,text = 'Answer',command = answer)
##b1.grid ()
##b2 = Button (root,text = 'Quit',command = leave)
##b2.grid (row = 0,column = 1)

##def submit ():
##    num = int (e1.get ())
##    if num % 2 == 0:
##        messagebox.showinfo ('Even','The number entered is even.')
##        if messagebox.askretrycancel ('Popout','Test another number?'):
##            e1.delete (0,END)
##        else:
##            quit ()
##    else:
##        messagebox.showinfo ('Odd','The number entered is odd.')
##        if messagebox.askretrycancel ('Popout','Test another number?'):
##            e1.delete (0,END)
##        else:
##            quit ()
##l1 = Label (root,text = 'Enter a number: ')
##l1.grid ()
##e1 = Entry (root)
##e1.grid (row = 0,column = 1)
##b1 = Button (root,text = 'Submit',command = submit)
##b1.grid (row = 1,column = 1)

##answer = IntVar ()
##message = StringVar ()
##def submit ():
##    a = answer.get ()
##    if a == 1:
##        message.set ('Correct')
##    elif a == 2:
##        message.set ('Wrong')
##l1 = Label (root,text = 'What is 15*(5+3)?')
##l1.grid (columnspan = 2)
##b1 = Radiobutton (root,text = '120',value = 1,variable = answer)
##b2 = Radiobutton (root,text = '78',value = 2,variable = answer)
##b1.grid (row = 1)
##b2.grid (row = 2)
##b3 = Button (root,text = 'Submit',command = submit)
##b3.grid (row = 3)
##l2 = Label (root,textvariable = message)
##l2.grid (row = 3,column = 1)

##selection = IntVar ()
##message = StringVar ()
##def submit ():
##    if selection.get () == 1:
##        message.set ('1,2,3,...')
##    elif selection.get () == 2:
##        message.set ('0,1,2,3,...')
##    elif selection.get () == 3:
##        message.set ('...,-3,-2,-1,0,1,2,3,...')
##    elif selection.get () == 4:
##        message.set ('...,-root(3),-1,0,1/2,1,...')
##l1 = Label (root,text = 'Select one topic:')
##l1.grid (columnspan = 2)
##b1 = Radiobutton (root,text = 'Natural Numbers',value = 1,variable = selection,command = submit)
##b2 = Radiobutton (root,text = 'Whole Numbers',value = 2,variable = selection,command = submit)
##b3 = Radiobutton (root,text = 'Integers',value = 3,variable = selection,command = submit)
##b4 = Radiobutton (root,text = 'Real Numbers',value = 4,variable = selection,command = submit)
##b1.grid (row = 1)
##b2.grid (row = 1,column = 1)
##b3.grid (row = 2)
##b4.grid (row = 2,column = 1)
##l2 = Label (root,textvariable = message)
##l2.grid (row = 3,columnspan = 2)

##milk = BooleanVar ()
##eggs = IntVar ()
##cer = IntVar ()
##fruit = IntVar ()
##list1 = []
##def add ():
##    global milk,eggs,cer,fruit,list1
##    list1 = []
##    if milk.get () == True:
##        list1.append ('Milk')
####    elif milk != 1:
####        list1.remove ('Milk')
##    if eggs.get () == 1:
##        list1.append ('Eggs')
####    elif eggs != 1:
####        list1.remove ('Eggs')
##    if cer.get () == 1:
##        list1.append ('Cereal')
####    elif cer != 1:
####        list1.remove ('Cereal')
##    if fruit.get () == 1:
##        list1.append ('Fruit')
####    elif fruit != 1:
####        list1.remove ('Fruit')
##def check ():
##    global list1
##    add ()
##    print (list1)
##def clear ():
##    global milk,eggs,cer,fruit
##    milk = False
##    eggs = False
##    cer = False
##    fruit = False
##l1 = Label (root,text = 'Grocery List')
##l1.grid ()
##b1 = Checkbutton (root,text = 'Milk',variable = milk,command = add)
##b2 = Checkbutton (root,text = 'Eggs',variable = eggs,command = add)
##b3 = Checkbutton (root,text = 'Cereal',variable = cer,command = add)
##b4 = Checkbutton (root,text = 'Fruit',variable = fruit,command = add)
##b1.grid (row = 1)
##b2.grid (row = 1,column = 1)
##b3.grid (row = 2)
##b4.grid (row = 2,column = 1)
##b5 = Button (root,text = 'Checkout',command = check)
##b6 = Button (root,text = 'Clear',command = clear)
##b5.grid (row = 3)
##b6.grid (row = 3,column = 1)

##a = BooleanVar ()
##b = BooleanVar ()
##c = BooleanVar ()
##d = BooleanVar ()
##p = DoubleVar ()
##amount = 0
##def calc ():
##    global amount,a,b,c,d,p
##    amount = int (e1.get ())
##    if a.get () == True:
##        p.set (1 * amount)
##        a.set (False)
##    if b.get () == True:
##        p.set (2 * amount)
##        b.set (False)
##    if c.get () == True:
##        p.set (4 * amount)
##        c.set (False)
##    if d.get () == True:
##        p.set (3 * amount)
##        d.set (False)
##l1 = Label (root,text = 'Purchase an Item:')
##l1.grid (columnspan = 2)
##b1 = Radiobutton (root,text = 'Apples',value = 1,variable = a)
##b2 = Radiobutton (root,text = 'Banana',value = 2,variable = b)
##b3 = Radiobutton (root,text = 'Grapes',value = 3,variable = c)
##b4 = Radiobutton (root,text = 'Oranges',value = 4,variable = d)
##b1.grid (row = 1)
##b2.grid (row = 1,column = 1)
##b3.grid (row = 2)
##b4.grid (row = 2,column = 1)
##l2 = Label (root,text = 'Amount: ')
##e1 = Entry (root)
##l3 = Label (root,text = 'Price: ')
##l4 = Label (root,textvariable = p)
##l2.grid (row = 3)
##e1.grid (row = 3,column = 1)
##l3.grid (row = 4)
##l4.grid (row = 4,column = 1)
##b5 = Button (root,text = 'Calculate Price',command = calc)
##b5.grid (row = 5,columnspan = 2)

root.mainloop ()
