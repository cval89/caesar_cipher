# Christian Valles 
# caesar_cipher.py

# Caesar Cipher
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
    while True:
        print('Do you wish to encrypt or decrypt a message?')
        mode = input().lower()
        if mode in ['encrypt', 'e', 'decrypt', 'd']:
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
    print('Enter your message:')
    return input()

def getKey():
    while True:
        print(f'Enter the key number (1-{MAX_KEY_SIZE}):')
        try:
            key = int(input())
            if 1 <= key <= MAX_KEY_SIZE:
                return key
        except ValueError:
            pass
        print(f'Please enter a number between 1 and {MAX_KEY_SIZE}.')

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)
        if symbolIndex == -1:
            # Symbol not found in SYMBOLS — add without change
            translated += symbol
        else:
            # Shift symbol by key
            symbolIndex += key

            # Wrap around if needed
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)

            translated += SYMBOLS[symbolIndex]

    return translated

# Run the program
if __name__ == '__main__':
    mode = getMode()
    message = getMessage()
    key = getKey()
    print('Your translated text is:')
    print(getTranslatedMessage(mode, message, key))
