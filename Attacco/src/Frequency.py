import operator
from audioop import reverse

class Frequency:
    
    @staticmethod
    def get(file_name):
        file = open(file_name, "r")
        frequency = file.readlines()
        dictionary = {}
        
        for c in frequency:
            dictionary[c[0]] = float(c[1:])
        
        #dictionary = sorted(temp_dictionary.items(), key=operator.itemgetter(1), reverse=True)
        
        return dictionary