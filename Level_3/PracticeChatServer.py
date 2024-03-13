import socket
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
host = ''
port = 12345
s.bind ((host,port))
print ('socket has binded to',port)
s.listen (5)
print ('listening')
conn,addr = s.accept ()
print ('received',addr)
while True:
    msg = input ('enter msg - ')
    conn.send (msg.encode ())
    msg_recv = conn.recv (1024)
    print (msg_recv.decode ())
