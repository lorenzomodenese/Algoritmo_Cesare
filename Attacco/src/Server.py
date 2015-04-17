import socket
import Util

class Server:   
    
    @staticmethod
    def initServerSocket():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((Util.ADDRESS, Util.PORT))
        s.listen(5)
        return s
    
    @staticmethod
    def readSocket(clientSocket):
        string = clientSocket.recv(Util.SIZE)
        return string