import socket
import threading
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
import atexit
def handleExit ():
    print ('Interrupt')
    s.close ()
atexit.register (handleExit)
host = ''
port = 12345
s.bind ((host,port))
s.listen (10)

connections = {}

def send_everyone (msg,conn):
    for loop in connections:
        try:
            if connections [loop] != conn:
                connections [loop].sendall (msg.encode ())
        except:
            continue

def get_and_send (user,conn):
    while True:
        try:
            msg = conn.recv (1024).decode ('utf-8')
            send_everyone (('<' + user + '>: ' + msg),conn)
        except:
            send_everyone ((user + ' has left the chat.'),conn)
            del connections [user]
            return

def getuser ():
    while True:
        conn,addr = s.accept ()
        print ('Got a connection from',addr)
        user = conn.recv (1024).decode ('utf-8')
        connections [user] = conn
        send_everyone ((user + ' has joined the chat.'),conn)
        print (connections)
        userthread = threading.Thread (target = get_and_send,args = (user,conn))
        userthread.start ()

getuser ()
conn.close ()
