import socket

global inIP
inIP = "127.0.0.1"

global inPORT
inPORT = 2020

global outIP
outIP = "127.0.0.1"

global outPORT
outPORT = 9093

global mirrorIP
mirrorIP = "127.0.0.1"

global mirrorPORT
mirrorPORT = 9094

inSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
inSocket.bind((inIP, inPORT))

outSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mirrorSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
	data, address = inSocket.recvfrom(1024)
	print "\n\n\t\t\t-------------------------\n-> ", address, "---: \n", data
	outSocket.sendto(data, (outIP, outPORT))
	mirrorSocket.sendto(data, (mirrorIP, mirrorPORT))

