# Python program to implement Morse Code Translator

'''
VARIABLE KEY
'encoded_string' -> 'stores the morse translated form of the english string'
'decoded_string' -> 'stores the english translated form of the morse string'
'morse_letter' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''

# Dictionary representing the morse code chart
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


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    encoded_string = ''
    for letter in message:
        if letter != ' ':

            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            encoded_string += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 3 indicates different words
            encoded_string += '  '

    return encoded_string


# Function to decrypt the string
# from morse to english
def decrypt(message):
    # extra space added at the end to access the
    # last morse code
    message += ' '

    decoded_string = ''
    morse_letter = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            morse_letter += letter

        # if i = 1 that indicates a previous character was space
        elif i == 1:
            i += 1
        else:
            i += 1
            # if i = 3 that indicates a new word
            if i == 3:

                # adding space to separate words
                decoded_string += ' '
            else:

                # accessing the keys using their values (reverse of encryption)
                decoded_string += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(morse_letter)]
                morse_letter = ''

    return decoded_string


# Hard-coded driver function to run the program
def main():
    message = "HEY JUDE SOS"
    result = encrypt(message.upper())
    print(result)

    message = ".... . -.--   .--- ..- -.. .   ...−−−..."

    result = decrypt(message)
    print(result)

# Executes the main function
if __name__ == '__main__':
    main()
