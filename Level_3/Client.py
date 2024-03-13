import socket
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
while True:
    data = s.recv (1024)
    print (recdata.decode ())
    client = input ('Client - ')
    s.sendall (client.encode ())
    if client == 'q':
        s.close ()
