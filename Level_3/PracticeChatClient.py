import socket
s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
host = 'localhost'
port = 12345
s.connect ((host,port))
while True:
    msg_recv = s.recv (1024)
    print (msg_recv.decode ())
    msg = input ('enter msg - ')
    s.send (msg.encode ())
