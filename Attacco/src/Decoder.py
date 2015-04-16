from Frequency import Frequency

class Decoder:
    
    global FILE_NAME
    FILE_NAME = "english.txt"

    @staticmethod
    def decode(encoded_text):
        
        standard_frequency = Frequency.get(FILE_NAME)

        text_frequency = standard_frequency.fromkeys(standard_frequency.keys(), 0)