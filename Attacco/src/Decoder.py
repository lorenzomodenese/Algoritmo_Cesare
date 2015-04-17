from Frequency import Frequency
import operator
from audioop import reverse

class Decoder:
    
    global FILE_NAME
    FILE_NAME = "english.txt"
    
    global DECODED_FILE
    DECODED_FILE = "decoded_file.txt"

    @staticmethod
    def decode(encoded_file):
        
        standard_frequency = Frequency.get(FILE_NAME)

        text_frequency = standard_frequency.fromkeys(standard_frequency.keys(), float(0))
        
        file = open(encoded_file, "r")
        
        numchar = 0
        c = file.read(1)
        while c != '':
            o = ord(c)
            
            if o in range(65, 90):
                o = o + 32
            
            if o in range(97, 122):
                c = chr(o)
                text_frequency[c] = text_frequency[c] + 1
                numchar = numchar + 1
            
            c = file.read(1)
        
        file.close()
                
        for f in text_frequency:
            text_frequency[f] = 100 * text_frequency[f] / numchar
            print f, text_frequency[f]
        
        sorted_standard_frequency = sorted(standard_frequency.items(), key=operator.itemgetter(1), reverse=True)
        sorted_text_frequency = sorted(text_frequency.items(), key=operator.itemgetter(1), reverse=True)
        
        print sorted_standard_frequency
        standard_character, standard_value = sorted_standard_frequency.pop(0)
        text_character, text_value = sorted_text_frequency.pop(0)
        
        standard_ascii = ord(standard_character)
        text_ascii = ord(text_character)
        
        if standard_ascii > text_ascii:
            key = standard_ascii - text_ascii
        else:
            key = text_ascii - standard_ascii
        
        #correggere uso pop
        confidence = text_value
        standard_temp = list(sorted_standard_frequency) 
        text_temp = list(sorted_text_frequency)   
        for f in standard_temp:
            standard_char, standard_value = f
            decodedKey = chr(ord(char) + key)
            text_char, text_value=text_temp.pop(0)
            if (text_char==decodedKey):
                confidence = confidence + text_value
        
        print "Encryption key found: ", key, " confidence value : ", confidence, "."
            
            
        file = open(encoded_file, "r")
        decrypted = open(DECODED_FILE, "w")
        encoded_character = file.read(1)
        while encoded_character != '':
            
            ascii = ord(encoded_character)
            decoded_character = ascii
            
            if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
                
                decoded_character = ascii - key
                
                if decoded_character < 65:
                    decoded_character = decoded_character + 26
                if decoded_character < 97 and (ascii >= 97 and ascii <= 122):
                    decoded_character = decoded_character + 26
            
            decrypted.write(chr(int(decoded_character)))
            
            encoded_character = file.read(1)
        
        decrypted.close()
        file.close()
          