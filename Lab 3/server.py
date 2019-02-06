import socket
import datetime
import time
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print ("Socket created")
PORT = 8000
HOST = ''
s.bind(('',PORT))
s.listen(5)
while True:
    try:
        c, addr = s.accept()
        c.settimeout(10)
        print('Connection received from', addr)
        c.send('You have connected successfully')
        while True:
            #s.Timeout(10)
            #print c.recv(1024)
            buff = c.recv(1024)
            now = int(time.time())
            if buff == '1':
                dt=str(datetime.datetime.now()) 
                c.send(dt)
            elif buff == '2':
                ad = str(addr)
                print ad
                c.send(ad.encode())
            elif buff == '3':
                c.send('Bye')
                c.close()
                break
            ntime = int(time.time())
    except socket.timeout as e:
        print(e) 
        c.close()
            
    #c.send('Bye')
    #c.close()

