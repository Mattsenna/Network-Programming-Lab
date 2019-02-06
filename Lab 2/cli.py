import socket
s = socket.socket()
s.settimeout(10)
PORT = 8000
s.connect(('0.0.0.0', PORT))
print s.recv(2048)
try:
    while True:
        option = raw_input("1 for Time, 2 for IP, 3 to Exit")
        s.sendall(option.encode())
        print s.recv(2048)
        if option == '3':
            break
except socket.error as e:
    print(e)
    #print "timeout"
    s.close()
    #print s.recv(2048)
    #print s.recv(2048)
    s.close()