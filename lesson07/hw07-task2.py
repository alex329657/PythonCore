"""
Implement a function that would take the morse code as input and return a decoded human-readable string
"""

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-',
                   'SOS': "...−−−..."}

def decodemorse(message):

    message += ' '

    decoded_string = ''
    morse_letter = ''

    for letter in message:

        # checks for space
        if (letter != ' '):
            #space counter
            i = 0
            morse_letter += letter

        #if i = 1 previous character space
        elif i == 1:
            i += 1

        else:
            i += 1
            # if i = 3 - new word

            if i == 3:
                #space separator
                decoded_string += ' '

            else:
                decoded_string += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_letter)]
                morse_letter = ''

    return decoded_string

    message = ".... . -.--   .--- ..- -.. .   ...−−−..."
    result = decodemorse(message)
    print(result)

