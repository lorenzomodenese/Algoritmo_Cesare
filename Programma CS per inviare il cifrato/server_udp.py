import sys
import socket
import os

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 9093))
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #sock.listen(5)
except:
    print "Errore confg iniziale"
print "Avvio server, pronto a ricevere un file"



print "Ricevuta richiesta",
file = open("cifrato.txt", 'wb')
try:
	while 1:
	    data, address = sock.recvfrom(1024*1)
	    if not data:
		break
	    file.write(data)

except Exception as e:
	print e
finally:
	file.close()

sock.close()
