from Server import Server
from Decoder import Decoder
import os
import Util

s = Server.initServerSocket()
print "Running and waiting..."

while True:
    
    clientSocket, address = s.accept()
    
    pid = os.fork()
    
    if(pid == 0):
        
        print "Receiving data..."
        
        try:
            s.close()
            
            encoded_text = Server.readSocket(clientSocket)
            
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
            
        finally:
            clientSocket.close()
            os._exit(0)
        
    else:
        clientSocket.close()