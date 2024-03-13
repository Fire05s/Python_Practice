import tkinter,random,pygame,time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
root = Tk ()
root.title ('Screen')
import webcolors
import pytz,datetime
from datetime import datetime
#root.geometry ('400x300')

##import webbrowser
##str1 = StringVar ()
##str1 = ''
##l1 = Label (root,text = str1,)
##def fblink ():
##    str1 = 'Facebook: JohnSmithFB'
##    l1 ['text'] = str1
##    webbrowser.open_new_tab ('www.facebook.com')
##def sclink ():
##    str1 = 'Snapchat: JohnSmithSC'
##    l1 ['text'] = str1
##    webbrowser.open_new_tab ('www.snapchat.com')
##def iglink ():
##    str1 = 'Facebook: JohnSmithIG'
##    l1 ['text'] = str1
##    webbrowser.open_new_tab ('www.instagram.com')
##def twlink ():
##    str1 = 'Twitter: JohnSmithTW'
##    l1 ['text'] = str1
##    webbrowser.open_new_tab ('www.twitter.com')
##fb = Button (root,text = 'Facebook',bg = 'blue',fg = 'white',command = fblink,width = 10,height = 1)
##sc = Button (root,text = 'Snaphchat',bg = 'yellow',fg = 'black',command = sclink,width = 10,height = 1)
##ig = Button (root,text = 'Instagram',bg = 'red',fg = 'white',command = iglink,width = 10,height = 1)
##tw = Button (root,text = 'Twitter',bg = 'blue',fg = 'white',command = twlink,width = 10,height = 1)
##fb.grid ()
##sc.grid (row = 0,column = 1)
##ig.grid (row = 1)
##tw.grid (row = 1,column = 1)
##l1.grid (row = 2,column = 0,columnspan = 2)

##mainlist = ['man','dog','cat','tree','real','fantastic','magic','evil','good','help']
##gamelist = mainlist
##active = False
##question = 1
##points = 0
##newword = StringVar ()
##newword = ''
##word = ''
##b1text = StringVar ()
##b1text = 'Click to Start'
##end = False
##def start ():
##    global active,newword,b1text,end,b1,word,gamelist
##    if end == False:
##        if active == False:
##            b1text = 'Guess the Jumbled Word'
##            b1 ['text'] = b1text
##            wordlist = random.sample (gamelist,1)
##            word = ''.join (wordlist)
##            gamelist.remove (word)
##            splitword = list (word)
##            while splitword == list (word):
##                random.shuffle (splitword)
##            newword = ''.join (splitword)
##            l1 ['text'] = newword
##            active = True
##def submit ():
##    global active,newword,b1text,end,b1,word,points,question,gamelist,mainlist
##    if end == False:
##        submission = str (e1.get ())
##        if submission == word and active == True:
##            messagebox.showinfo ('Correct','You got a point.')
##            points = points + 1
##            question = question + 1
##            active = False
##            b1text = 'Click to Receive a New Word'
##            b1 ['text'] = b1text
##            if gamelist == []:
##                messagebox.showinfo ('Completed','You have finished all questions! Your final score is '+str(points)+'.')
##                b1text = 'Thanks for Playing! Bye!'
##                b1 ['text'] = b1text
##                newword = ''
##                l1 ['text'] = newword
##                end = True
##        elif submission != word:
##            messagebox.showerror ('Wrong','You got the wrong answer.')
##b1 = Button (root,text = b1text,bg = 'orange',fg = 'black',width = 30,height = 1,command = start)
##b1 ['text'] = b1text
##b2 = Button (root,text = 'Submit',bg = 'white',fg = 'black',width = 10,height = 1,command = submit)
##l1 = Label (root,text = newword,bg = 'cyan',fg = 'black',width = 10,height = 1)
##e1 = Entry (root)
##b1.grid (columnspan = 2)
##b2.grid (row = 2,column = 1)
##l1.grid (row = 1)
##e1.grid (row = 1,column = 1)

##q = IntVar ()
##q = 0
##cart = {}
##def sub ():
##    global q
##    if q != 0:
##        q = q - 1
##        l3 ['text'] = q
##def add ():
##    global q
##    q = q + 1
##    l3 ['text'] = q
##def addcart ():
##    global q,cart
##    cart [e1.get ()] = q
##    print (cart)
##def check ():
##    global cart
##    messagebox.showinfo ('Grocery Cart',cart)
##    root.destroy ()
##l1 = Label (root,text = 'Please enter an item: ')
##l2 = Label (root,text = 'Choose the quantity: ')
##b1 = Button (root,text = '-',fg = 'red',command = sub)
##b2 = Button (root,text = '+',fg = 'green',command = add)
##b3 = Button (root,text = 'CHECKOUT',fg = 'red',command = check)
##b4 = Button (root,text = 'ADD TO CART',fg = 'blue',command = addcart)
##e1 = Entry (root)
##l3 = Label (root,text = q)
##l1.grid (columnspan = 3)
##l2.grid (row = 1,columnspan = 3)
##e1.grid (row = 0,column = 3,columnspan = 3)
##b1.grid (row = 1,column = 3)
##b2.grid (row = 1,column = 5)
##l3.grid (row = 1,column = 4)
##b3.grid (row = 2,columnspan = 3)
##b4.grid (row = 2,column = 3,columnspan = 3)

##rv = IntVar ()
##bv = IntVar ()
##gv = IntVar ()
##col = webcolors.rgb_to_hex ((rv.get (),bv.get (),gv.get ()))
##s1 = Scale (root,label = 'Red',variable = rv,from_ = 0,to = 255,orient = VERTICAL)
##s2 = Scale (root,label = 'Blue',variable = bv,from_ = 0,to = 255,orient = VERTICAL)
##s3 = Scale (root,label = 'Green',variable = gv,from_ = 0,to = 255,orient = VERTICAL)
##l1 = Label (root,text = '',bg = col,width = 50)
##s1.grid ()
##s2.grid (row = 0,column = 1)
##s3.grid (row = 0,column = 2)
##l1.grid (row = 1,columnspan = 3)
##while True:
##    r = rv.get ()
##    b = bv.get ()
##    g = gv.get ()
##    col = webcolors.rgb_to_hex ((r,g,b))
##    print (rv.get (),bv.get (),gv.get (),col)
##    l1.configure (bg = col)
##    root.update ()

#
##hflag = pygame.image.load ('hong_kong.png')
##cflag = pygame.image.load ('canada.png')
##fflag = pygame.image.load ('france.png')
##uflag = pygame.image.load ('usa.png')
##hflag = pygame.transform.scale (hflag,(200,100))
##cflag = pygame.transform.scale (cflag,(200,100))
##fflag = pygame.transform.scale (fflag,(200,100))
##uflag = pygame.transform.scale (uflag,(200,100))
##pygame.image.save (hflag,'C:/Users/Brandon Tsai/OneDrive/Desktop/Level 3/hong_kong.png')
##pygame.image.save (cflag,'C:/Users/Brandon Tsai/OneDrive/Desktop/Level 3/canada.png')
##pygame.image.save (fflag,'C:/Users/Brandon Tsai/OneDrive/Desktop/Level 3/france.png')
##pygame.image.save (uflag,'C:/Users/Brandon Tsai/OneDrive/Desktop/Level 3/usa.png')
#
##f1 = Frame (root,width = 200,height = 150)
##f2 = Frame (root,width = 200,height = 150)
##f3 = Frame (root,width = 200,height = 150)
##f4 = Frame (root,width = 200,height = 150)
##f1.grid ()
##f2.grid (row = 0,column = 1)
##f3.grid (row = 1)
##f4.grid (row = 1,column = 1)
##h1 = Label (f1,text = 'Hong Kong').place (x = 80,y = 5)
##c1 = Label (f2,text = 'Canada').place (x = 80,y = 5)
##fr1 = Label (f3,text = 'France').place (x = 80,y = 5)
##u1 = Label (f4,text = 'USA').place (x = 80,y = 5)
##himg = PhotoImage (file = 'hong_kong.png')
##cimg = PhotoImage (file = 'canada.png')
##fimg = PhotoImage (file = 'france.png')
##uimg = PhotoImage (file = 'usa.png')
##hfl = Label (f1,image = himg).place (x = 0,y = 25)
##cfl = Label (f2,image = cimg).place (x = 0,y = 25)
##ffl = Label (f3,image = fimg).place (x = 0,y = 25)
##ufl = Label (f4,image = uimg).place (x = 0,y = 25)
##htime = StringVar ()
##ctime = StringVar ()
##ftime = StringVar ()
##utime = StringVar ()
##t1 = Label (f1,textvariable = htime).place (x = 10,y = 135)
##t2 = Label (f2,textvariable = ctime).place (x = 10,y = 135)
##t3 = Label (f3,textvariable = ftime).place (x = 10,y = 135)
##t4 = Label (f4,textvariable = utime).place (x = 10,y = 135)
##while True:
##    timezone = pytz.timezone ('Hongkong')
##    current = datetime.now (timezone)
##    final_time1 = current.strftime ('%Y-%m-%d%I:%M:%S%p%Z')
##    htime.set (final_time1)
##    timezone = pytz.timezone ('Canada/Eastern')
##    current = datetime.now (timezone)
##    final_time2 = current.strftime ('%Y-%m-%d%I:%M:%S%p%Z')
##    ctime.set (final_time2)
##    timezone = pytz.timezone ('Europe/Amsterdam')
##    current = datetime.now (timezone)
##    final_time3 = current.strftime ('%Y-%m-%d%I:%M:%S%p%Z')
##    ftime.set (final_time3)
##    timezone = pytz.timezone ('US/Pacific')
##    current = datetime.now (timezone)
##    final_time4 = current.strftime ('%Y-%m-%d%I:%M:%S%p%Z')
##    utime.set (final_time4)
##    root.update ()

##f1 = Frame (root,width = 300,height = 50,bg = 'red').grid ()
##f2 = Frame (root,width = 300,height = 50,bg = 'blue').grid (row = 1)
##f3 = Frame (root,width = 300,height = 50,bg = 'yellow').grid (row = 2)
##f4 = Frame (root,width = 300,height = 50,bg = 'green').grid (row = 3)
##gp = StringVar ()
##gp1 = Label (f1,text = 'Generated Password: ').place (x = 10,y = 10)
##gp2 = Label (f1,textvariable = gp).place (x = 150,y = 10)
##ps1 = Label (f2,text = 'Password Strength: ').place (x = 10,y = 60)
##v1 = IntVar ()
###coordinates all from root (0,0)
##psb1 = Radiobutton (f2,text = 'Low',variable = v1,value = 1).place (x = 120,y = 60)
##psb2 = Radiobutton (f2,text = 'Medium',variable = v1,value = 2).place (x = 170,y = 60)
##psb3 = Radiobutton (f2,text = 'High',variable = v1,value = 3).place (x = 240,y = 60)
##pl1 = Label (f3,text = 'Password Length: ').place (x = 10,y = 110)
##num = IntVar ()
##num.set (6)
##plspin = Spinbox (f3,textvariable = num,from_ = 6,to = 12).place (x = 150,y = 110)
##print (num.get ())
##def submit ():
##    global v1,gp,plspin
##    plist = []
##    strength = 0
##    print (v1.get ())
##    if v1.get () == 1:
##        strength = 1
##    elif v1.get () == 2:
##        strength = 2
##    else:
##        strength = 3
##    alphabet = 'abcdefghijklmnopqrstuvwxyz'
##    numbers = '1234567890'
##    char = '!@#$%^&*()'
##    for loop in range (0,num.get (),1):
##        if strength == 1:
##            plist.append (random.choice (alphabet))
##        if strength == 2:
##            choice = random.randint (1,2)
##            if choice == 1:
##                plist.append (random.choice (alphabet))
##            else:
##                plist.append (random.choice (numbers))
##        if strength == 3:
##            choice = random.randint (1,3)
##            if choice == 1:
##                plist.append (random.choice (alphabet))
##            elif choice == 2:
##                plist.append (random.choice (numbers))
##            else:
##                plist.append (random.choice (char))
##    p = ''.join (plist)
##    print (p)
##    gp.set (p)
##sub = Button (f4,text = 'Submit',command = submit).place (x = 10, y = 160)

##gdict = {'Milk':5,'Chocolates':3,'Eggs':7,'Bread':4,'Fruits':2}
##f1 = Frame (root,width = 300,height = 300)
##f1.grid ()
##l1 = Label (f1,text = 'Choose the items that you want to buy.').place (x = 10,y = 10)
##v1 = BooleanVar ()
##v2 = BooleanVar ()
##v3 = BooleanVar ()
##v4 = BooleanVar ()
##v5 = BooleanVar ()
##c1 = Checkbutton (f1,text = 'Milk',variable = v1)
##c1.place (x = 100,y = 30)
##c2 = Checkbutton (f1,text = 'Chocolates',variable = v2)
##c2.place (x = 100,y = 60)
##c3 = Checkbutton (f1,text = 'Eggs',variable = v3)
##c3.place (x = 100,y = 90)
##c4 = Checkbutton (f1,text = 'Bread',variable = v4)
##c4.place (x = 100,y = 120)
##c5 = Checkbutton (f1,text = 'Fruits',variable = v5)
##c5.place (x = 100,y = 150)
##def clear ():
##    global c1,c2,c3,c4,c5
##    c1.deselect ()
##    c2.deselect ()
##    c3.deselect ()
##    c4.deselect ()
##    c5.deselect ()
####    v1.set (False)
####    v2.set (False)
####    v3.set (False)
####    v4.set (False)
####    v5.set (False)
##def nextf ():
##    f1.grid_forget ()
##b1 = Button (f1,text = 'Clear',command = clear).place (x = 40,y = 270)
##b2 = Button (f1,text = 'Next',command = nextf).place (x = 240,y = 270)

f1 = Frame (root,width = 200,height = 50).grid ()
l1 = Label (f1,text = 'Score: ').place (x = 75,y = 20)
score = IntVar ()
scorevar = 0
def supdate ():
    global scorevar
    scorevar = scorevar + 1
    score.set (scorevar)
    print (scorevar,score.get ())
    root.update ()
l2 = Label (f1,textvariable = score).place (x = 120,y = 20)
class Question:
    def __init__ (self,q,ans,olist,choice):
        self.f = Frame (root,width = 200,height = 150,bg = 'gray')
        self.l = Label (self.f,text = q)
        self.a = ans
        self.tracker = IntVar ()
        self.options = []
        i = 1
        for loop in olist:
            self.options.append (Radiobutton (self.f,text = loop,variable = self.tracker,value = i))
            i = i + 1
        self.achoice = choice
    def show (self):
        self.f.grid (row = 1)
        self.l.place (x = 10,y = 10)
        ry = 40
        for loop in self.options:
            loop.place (x = 10,y = ry)
            ry = ry + 30
    def hide (self):
        self.f.grid_forget ()
q1 = Question ('5+7','12',['12','5','7'],1)
q2 = Question ('5*7','35',['5','35','7'],2)
q3 = Question ('4*9','36',['8','2','36'],3)
q4 = Question ('36/6','6',['18','216','6'],3)
q5 = Question ('216-25','191',['191','9','36'],1)
q1.show ()
qnum = 1
def submit ():
    global q1,q2,q3,q4,q5,scorevar
    if qnum == 1:
        for loop in q1.options:
            loop.config (state = DISABLED)
        if q1.tracker.get () == q1.achoice:
            supdate ()
            q1.options [q1.tracker.get ()-1] ['fg'] = 'green'
        else:
            q1.options [q1.tracker.get ()-1] ['fg'] = 'red'
            q1.options [q1.achoice-1] ['fg'] = 'green'
    if qnum == 2:
        for loop in q2.options:
            loop.config (state = DISABLED)
        if q2.tracker.get () == q2.achoice:
            supdate ()
            q2.options [q2.tracker.get ()-1] ['fg'] = 'green'
        else:
            q2.options [q2.tracker.get ()-1] ['fg'] = 'red'
            q2.options [q2.achoice-1] ['fg'] = 'green'
    if qnum == 3:
        for loop in q3.options:
            loop.config (state = DISABLED)
        if q3.tracker.get () == q3.achoice:
            supdate ()
            q3.options [q3.tracker.get ()-1] ['fg'] = 'green'
        else:
            q3.options [q3.tracker.get ()-1] ['fg'] = 'red'
            q3.options [q3.achoice-1] ['fg'] = 'green'
    if qnum == 4:
        for loop in q4.options:
            loop.config (state = DISABLED)
        if q4.tracker.get () == q4.achoice:
            supdate ()
            q4.options [q4.tracker.get ()-1] ['fg'] = 'green'
        else:
            q4.options [q4.tracker.get ()-1] ['fg'] = 'red'
            q4.options [q4.achoice-1] ['fg'] = 'green'
    if qnum == 5:
        for loop in q5.options:
            loop.config (state = DISABLED)
        if q5.tracker.get () == q5.achoice:
            supdate ()
            q5.options [q5.tracker.get ()-1] ['fg'] = 'green'
        else:
            q5.options [q5.tracker.get ()-1] ['fg'] = 'red'
            q5.options [q5.achoice-1] ['fg'] = 'green'
    root.update ()
def nextq ():
    global q1,q2,q3,q4,q5,qnum
    if qnum == 1:
        q1.hide ()
        q2.show ()
    if qnum == 2:
        q2.hide ()
        q3.show ()
    if qnum == 3:
        q3.hide ()
        q4.show ()
    if qnum == 4:
        q4.hide ()
        q5.show ()
    if qnum == 5:
        print ('You\'ve completed the quiz.')
        qnum = qnum + 1
    qnum = qnum + 1
f3 = Frame (root,width = 200,height = 50).grid (row = 2)
b1 = Button (f3,text = 'Submit',command = submit).place (x = 10,y = 220)
b2 = Button (f3,text = 'Next',command = nextq).place (x = 140,y = 220)

##def disable ():
##    b1.config (state = DISABLED)
##    l1.config (text = 'Bye')
##b1 = Button (root,text = 'B1',command = disable)
##b2 = Button (root,text = 'B2',state = DISABLED)
##l1 = Label (root,text = 'Hello')
##b1.grid ()
##b2.grid (row = 1)
##l1.grid (row = 2)


root.mainloop ()
