from Frequency import Frequency
import operator
from audioop import reverse
import Util

class Decoder:   

    @staticmethod
    def decode():
        
        standard_frequency = Frequency.get(Util.FILE_NAME)

        text_frequency = standard_frequency.fromkeys(standard_frequency.keys(), float(0))
        
        file = open(Util.ENCODED_FILE, "r")
        
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
        
        keys = []
        list_index = 0
        index_key = 0
        while index_key == 0:
            
            standard_character, standard_value = sorted_standard_frequency[list_index]
            text_character, text_value = sorted_text_frequency[list_index]
            list_index = list_index + 1
            
            standard_ascii = ord(standard_character)
            text_ascii = ord(text_character)
            
            if standard_ascii > text_ascii:
                key_value = standard_ascii - text_ascii
            else:
                key_value = text_ascii - standard_ascii
            
            found_key = False
            for key, key_confidence in keys:
                print "Dentro for in key"
                if key_value == key:
                    found_key = True
                    print "key found!"
            
            if not found_key:
                print "key not found"
                keys.insert(len(keys), (key_value, 0))
                
                key_value, key_confidence = keys[len(keys) - 1]
                
                for f in sorted_text_frequency:
                    text_character, text_value = f
                    
                    decodedKey = ord(text_character) - key_value
                    
                    if decodedKey < 97:
                        decodedKey = decodedKey + 26
                        
                    standard_character, standard_value = sorted_standard_frequency[sorted_text_frequency.index(f)]
                    
                    if (standard_character == chr(decodedKey)):
                        key_confidence = key_confidence + text_value
                
                keys[len(keys) - 1] = (key_value, key_confidence)
                
                for k in keys:
                    value, confidence = k
                    print keys.index(k)+1 ,". Encryption key: ", value, ", confidence value: ", confidence, "."
                
                
                while True:
                    input_key = raw_input("Select a key or type 0 to calculate another key -> ")
                    try:
                        index_key = int(input_key)
                        if (index_key >= 1) and (index_key <= len(keys)):
                            key_value, key_confidence = keys[index_key - 1]
                            break
                        else:
                            if (index_key == 0) and (list_index < len(sorted_standard_frequency)):
                                print "Calculating another key..."
                                break
                            else:
                                if index_key == 0:
                                    print "All keys have been already generated!"
                                else:
                                    print "Key index incorrect!"
                    
                    except Exception as e:
                        print "Key index incorrect, please insert a number!"
                
            
        file = open(Util.ENCODED_FILE, "r")
        decrypted = open(Util.DECODED_FILE, "w")
        encoded_character = file.read(1)
        while encoded_character != '':
            
            ascii = ord(encoded_character)
            decoded_character = ascii
            
            if (ascii >= 65 and ascii <= 90) or (ascii >= 97 and ascii <= 122):
                
                decoded_character = ascii - key_value
                
                if decoded_character < 65:
                    decoded_character = decoded_character + 26
                if decoded_character < 97 and (ascii >= 97 and ascii <= 122):
                    decoded_character = decoded_character + 26
            
            decrypted.write(chr(int(decoded_character)))
            
            encoded_character = file.read(1)
        
        decrypted.close()
        file.close()
          