MY_CODES = {'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X',\
 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C','Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', \
 'X': 'K', 'Y': 'L', 'Z': 'M'}

def encript(text):
    res = ''
    for letter in text:
        if letter in MY_CODES.keys():
            res = res +  MY_CODES[letter]
        else:
            res = res + letter
    return res

def decript(text):
    res = ''
    #Interchanging the dict keys to values and vice versa
    MY_CODES = dict(map(reversed, My_CODES.items()))
    for letter in text:
        if letter in MY_CODES.keys():
            res = res + MY_CODES[letter]
        else:
            res = res + letter
    return text

while True:
    user_text = input('Enter your text: ').upper()
    user_option = input('Do you wish to (E)ncrypt or (D)ecrypt the text? ')
    if user_option == 'E':
        result = encript(user_text)
        print(f'Here is the encrypted text: {result}')
    elif user_option == 'D':
        result = encript(user_text).upper()
        print(f'Here is the decrypted text: {result}')
    option = input('Would you like to to enter another string(Yy/Nn)? ')
    if option == 'N' or option == 'n':
        print('Program is terminated')
        break
