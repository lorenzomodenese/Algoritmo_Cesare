import socket
import os

global inIP
inIP = "192.168.43.71"

global inPORT
inPORT = 2020

global outIP
outIP = "192.168.43.41"

global outPORT
outPORT = 9093

global mirrorIP
mirrorIP = "192.168.43.160"

global mirrorPORT
mirrorPORT = 9093

inSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
inSocket.bind((inIP, inPORT))
inSocket.listen(5)

while True:
	
	clientSocket, address = inSocket.accept()
	
	pid = os.fork()
	
	if(pid == 0):
		try:
			inSocket.close()
			data = ""
			
			while True:
				string = clientSocket.recv(1024)
				if not string:
					break
				data = data + string
			
			print "\n\n\t\t\t-------------------------\n-> ", address, "---: \n", data
			
			outSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			outSocket.connect((outIP, outPORT))

			mirrorSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			mirrorSocket.connect((mirrorIP, mirrorPORT))
			
			outSocket.send(data)
			mirrorSocket.send(data)
			
		except Exception as e:
			print e
			print("Error!")
			
		finally:
			clientSocket.close()
			os._exit(0)
	else:
		clientSocket.close()

