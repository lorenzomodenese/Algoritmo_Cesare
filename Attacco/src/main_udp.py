from Server_udp import ServerUDP
from Decoder import Decoder
import os
import Util

socket = ServerUDP.initServerSocket()
print "Running and waiting..."

while True:

    try:
        
        encoded_text = ServerUDP.readSocket(socket)
        
        print "Data received!"
        
        file = open(Util.ENCODED_FILE, "w")
        
        file.write(encoded_text)
        
        file.close()
        
        print "Decoding data..."
        
        Decoder.decode()
        
        print "File successfully decoded!"
        print "\nRunning and waiting..."
        
    except Exception as e:
        print e
        print("Error!")
        
#   finally:
#       socket.close()
#       os._exit(0)