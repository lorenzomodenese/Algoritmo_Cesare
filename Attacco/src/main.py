from Server import Server
from Decoder import Decoder
import os

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
            
            print "Decoding data..."
            
            Decoder.decode(encoded_text)
            
        except Exception as e:
            print e
            print("Error!")
            
        finally:
            clientSocket.close()
            os._exit(0)
        
    else:
        clientSocket.close()