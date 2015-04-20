import socket
import os

ip=raw_input("Inserire indirizzo ip del server: ")
nome_file=raw_input("Inserire nome del file: ")

server_address=(ip,2020)
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#clientsocket.connect((ip, 2020))

file = open(nome_file, "r")
i=0
while 1: 
	stringa = file.read(1024)
	i=int(i)+1	
	print "Invio",i
	clientsocket.sendto(stringa,server_address)	
	if stringa == "": 
	    	break	   
file.close()

clientsocket.close()

print "File inviato corretamente"

