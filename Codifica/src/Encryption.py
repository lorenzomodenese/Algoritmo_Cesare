import sys

def cifratura(carattere, key):
    ascii=ord(carattere)
    cif=ascii
    if (ascii >=65 and ascii<=90) or (ascii >=97 and ascii<=122): #cifriamo solo le lettere
        cif=ascii+key
        if cif >= 91 and (ascii >=65 and ascii<=90): #se il cifrato va oltre il range delle sue 26 lettere maiuscole, tolgo 26 per ciclare solo sulle maiuscole, possiamo finire nel range delle minuscole
            cif=cif-26
        if cif >= 123:
            cif=cif-26
    return cif

def calcolaChiave(chiave):
    print int(chiave)%26
    return int(chiave)%26

print "CIFRATURA DEL TESTO (CIFRARIO DI CESARE)\n"

#inserimento file inpiut
chiave = raw_input("Inserire la chiave (esc per uscire): ")
if chiave=="esc":
    sys.exit()
file_name = raw_input("Inserire il file da cifrare: ")
key=calcolaChiave(chiave)

#apro il file e ne leggo un po alla volta 
file = open(file_name, "r")
cifrato = open("cifrato.txt", "w")
while 1: 
    carattere = file.read(1) 
    if carattere == "": 
        print "Fine file"
        break
    lettera_cifrata = cifratura(carattere,key)
    cifrato.write(chr(int(lettera_cifrata)))  #convertiamo in carattere il numero ascii
cifrato.close()
file.close()



     



