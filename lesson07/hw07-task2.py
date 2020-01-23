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

def decrypt(message):
    message += ' '
    decoded_string = ''
    morse_letter = ''
    for letter in message:
        if (letter != ' '):
            i = 0
            morse_letter += letter
        elif i == 1:
            i += 1
        else:
            i += 1
            if i == 3:
                decoded_string += ' '
            else:
                list1 = list(MORSE_CODE_DICT.keys())
                list2 = list(MORSE_CODE_DICT.values()).index(morse_letter)
                decoded_string += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_letter)]
                morse_letter = ''
    return decoded_string

def main():

    message = ".... . -.--   .--- ..- -.. .   ...−−−..."
    result = decrypt(message)
    print(result)

if __name__ == '__main__':
    main()
