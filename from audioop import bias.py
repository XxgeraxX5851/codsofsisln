from audioop import bias
bias.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')
return morseCode.replace('.', MORSE_CODE['.']).replace('-', MORSE_CODE['-']).replace(' ', '')
def decode_morse(morse_code):
    words = morse_code.strip().split('   ')  # Morse words are separated by 3 spaces
    return ' '.join(
        ''.join(MORSE_CODE[char] for char in word.split()) for word in words)
    