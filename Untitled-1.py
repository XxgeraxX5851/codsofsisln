def decode_morse(morse_code):
    # Step 1: Trim whitespace
    morse_code = morse_code.strip()

    # Step 2: Split into words
    words = morse_code.split('   ')  # 3 spaces separate words
    decoded_words = []

    for word in words:
        # Step 3: Split word into characters
        letters = word.split(' ')
        decoded_letters = [MORSE_CODE[letter] for letter in letters if letter in MORSE_CODE]
        decoded_words.append(''.join(decoded_letters))

    # Step 4: Join words with spaces
    return ' '.join(decoded_words)
