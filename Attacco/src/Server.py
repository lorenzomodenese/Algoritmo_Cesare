import socket

class Server:
    
    global ADDRESS
    ADDRESS = "192.168.43.71"
    
    global PORT
    PORT = 9093
    
    global SIZE
    SIZE = 4096
    
    @staticmethod
    def initServerSocket():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ADDRESS, PORT))
        s.listen(5)
        return s
    
    @staticmethod
    def readSocket(clientSocket):
        string = clientSocket.recv(SIZE)
        return string