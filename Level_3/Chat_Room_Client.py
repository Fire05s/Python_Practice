import socket
import tkinter
import threading
from tkinter import *
root = Tk ()
root.title ('Chat Room Client')
host = 'localhost'
port = 12345
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
import atexit
def handleExit ():
    print ('Interrupt')
    s.close ()
atexit.register (handleExit)
s.connect ((host,port))
print ('Connected')
user = ''
def get ():
    while True:
        data = s.recv (1024).decode ()
        l2 = Label (f1,text = data,fg = 'red',anchor = 'w')
        l2.pack (side = TOP,fill = X)
e1 = Entry (root,width = 120)
f1 = Frame (root,width = 100,height = 500)
def send ():
    msg = e1.get ()
    l1 = Label (f1,text = msg,fg = 'green',anchor = 'e')
    l1.pack (side = TOP,fill = X)
    s.sendall (msg.encode ())
    e1.delete (0,END)
def login ():
    global user
    user = loge1.get ()
    s.sendall (user.encode ())
    recp = threading.Thread (target = get)
    recp.start ()
    logl1.pack_forget ()
    loge1.pack_forget ()
    logb1.pack_forget ()
    e1.pack (side = BOTTOM)
    f1.pack (side = TOP)
    b1 = Button (root,text = 'SEND',width = 100,command = send)
    b1.pack (side = BOTTOM)
logl1 = Label (root,text = 'Enter your username')
logl1.pack (side = TOP)
loge1 = Entry (root,width = 120)
loge1.pack (side = TOP)
logb1 = Button (root,text = 'Login',command = login)
logb1.pack (side = TOP)
root.mainloop ()
s.close ()
