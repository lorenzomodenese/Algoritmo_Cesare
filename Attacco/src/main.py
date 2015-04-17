from Server import Server
from Decoder import Decoder
import os

Decoder.decode("cifrato.txt")
print "Dopo decoder testo.txt"

encoded_file = "encoded_text.txt"

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
            
            file = open(encoded_file, "w")
            
            file.write(encoded_text)
            
            file.close()
            
            print "Decoding data..."
            
            Decoder.decode(encoded_file)
            
        except Exception as e:
            print e
            print("Error!")
            
        finally:
            clientSocket.close()
            os._exit(0)
        
    else:
        clientSocket.close()