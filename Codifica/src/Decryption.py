import sys

def decifratura(carattere, key):
    ascii=ord(carattere)
    cif=ascii
    if (ascii >=65 and ascii<=90) or (ascii >=97 and ascii<=122): #cifriamo solo le lettere
        cif=ascii-key
        if cif <= 64 : #se il cifrato va oltre il range delle sue 26 lettere maiuscole, tolgo 26 per ciclare solo sulle maiuscole, possiamo finire nel range delle minuscole
            cif=cif+26
        if cif <=96 and (ascii >=97 and ascii<=122):
            cif=cif+26
    return cif

def calcolaChiave(chiave):
    return int(chiave)%26

print "**********************************************"
print "* DECIFRATURA DEL TESTO (CIFRARIO DI CESARE) *"
print "**********************************************"

#inserimento file inpiut
while 1:
    chiave = raw_input("Inserire la chiave (esc per uscire): ")
    key=calcolaChiave(chiave)
    if chiave=="esc":
        sys.exit()
    if int(chiave) <=0 or key==0:
        print "Chiave errata (si richiede una chiave positiva >0 e non multipla di 26)"
    else:
        break
file_name = raw_input("Inserire il file da decifrare: ")

#apro il file e ne leggo un po alla volta 
file = open(file_name, "r")
decifrato = open("decifrato.txt", "w")
while 1: 
    carattere_cifrato = file.read(1) 
    if carattere_cifrato == "": 
        print "Fine decifratura"
        break
    lettera_decifrata = decifratura(carattere_cifrato,key)
    decifrato.write(chr(int(lettera_decifrata)))  #convertiamo in carattere il numero ascii
decifrato.close()
file.close()