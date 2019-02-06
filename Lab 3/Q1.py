import socket
PORT = 80
s = socket.socket()
s.connect(('1.1.1.1', PORT))
print (s.getsockname()[0])
print (socket.gethostname())
s.close()