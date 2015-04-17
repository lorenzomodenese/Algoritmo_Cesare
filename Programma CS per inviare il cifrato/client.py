import socket
import os

ip=raw_input("Inserire indirizzo ip del server: ")
nome_file=raw_input("Inserire nome del file: ")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((ip, 9093))

file = open(nome_file, "r")

while 1: 
	stringa = file.read(1024)
	clientsocket.send(stringa)	
	if stringa == "": 
	    	break	   
file.close()

clientsocket.close()

print "File inviato corretamente"

