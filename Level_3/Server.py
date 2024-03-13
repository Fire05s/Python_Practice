import socket
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
import atexit
def handleExit ():
    print ('Interrupt')
    s.close ()
atexit.register (handleExit)
host = ''
port = 12345
s.bind ((host,port))
s.listen (5)
print ('Socket is listening')
conn,addr = s.accept ()
print ('Got a connection from',addr)
while True:
    serverv = input ('Server - ')
    conn.sendall (serverv.encode ())
    data = conn.recv (1024)
    print (addr,data.decode ())
    if serverv == 'q':
        s.close ()
