import socket
import tkinter
import threading
from tkinter import *
root = Tk ()
root.title ('Chat Box Client')
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

e1 = Entry (root,width = 120)
e1.pack (side = BOTTOM)
def send ():
    msg = e1.get ()
    l1 = Label (f1,text = msg,fg = 'green',anchor = 'e')
    l1.pack (side = TOP,fill = X)
    s.sendall (msg.encode ())
    e1.delete (0,END)
f1 = Frame (root,width = 100,height = 500)
f1.pack (side = TOP)
b1 = Button (root,text = 'SEND',width = 100,command = send)
b1.pack (side = BOTTOM)
def get ():
    while True:
        data = s.recv (1024).decode ()
        l2 = Label (f1,text = data,fg = 'red',anchor = 'w')
        l2.pack (side = TOP,fill = X)
recp = threading.Thread (target = get)
recp.start ()
root.mainloop ()
