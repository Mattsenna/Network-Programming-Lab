import socket
import binascii
rhost = "www.reddit.com"
rhp = socket.gethostbyname(rhost)
print "The reddit IP address is : ", rhp
#print bin(rhp)
max = len(rhp)
i=0
ip1=''
ip2=''
ip3=''
ip4=''
while rhp[i] != '.':
    ip1+=rhp[i]
#print ip1
    i=i+1
i=i+1
while rhp[i] != '.':
    ip2+=rhp[i]
#print ip2
    i=i+1
i=i+1
while rhp[i] != '.':
    ip3+=rhp[i]
    i=i+1
#print ip3
i=i+1
while i<max:
    ip4+=rhp[i]
    i=i+1
#print ip4
#i=i+1
ipi1 = int(ip1)
ipi2 = int(ip2)
ipi3 = int(ip3)
ipi4 = int(ip4)
print "The address in binary is : ", bin(ipi1), '.', bin(ipi2), '.', bin(ipi3), '.', bin(ipi4)
#print "The reddit IP address in binary is ", bin(int(binascii.hexlify(rhp), 16))
