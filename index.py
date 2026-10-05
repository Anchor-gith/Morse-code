# Standard International Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Reverse dictionary for decoding
REVERSE_MORSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}

def text_to_morse(text):
    """Converts plain text into Morse code."""
    morse_result = []
    for word in text.upper().split(' '):
        morse_word = []
        for char in word:
            if char in MORSE_CODE_DICT:
                morse_word.append(MORSE_CODE_DICT[char])
        morse_result.append(' '.join(morse_word))
    # Words are separated by a forward slash with spaces
    return ' / '.join(morse_result)

def morse_to_text(morse):
    """Decodes a Morse code string back into plain text."""
    text_result = []
    # Split by words using the slash separator
    words = morse.split('/')
    for word in words:
        # Split by individual letters
        letters = word.strip().split(' ')
        text_word = ""
        for letter in letters:
            if letter in REVERSE_MORSE_DICT:
                text_word += REVERSE_MORSE_DICT[letter]
            elif letter == '':
                continue
            else:
                text_word += '?' # Unknown symbol placeholder
        text_result.append(text_word)
    return ' '.join(text_result)

def main():
    print("--- Python Morse Code Translator ---")
    print("1. Text to Morse Code")
    print("2. Morse Code to Text")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == '1':
        text = input("Enter text to translate: ")
        print(f"\nMorse Code:\n{text_to_morse(text)}")
    elif choice == '2':
        morse_input = input("Enter Morse code (letters separated by spaces, words by ' / '): ")
        print(f"\nDecoded Text:\n{morse_to_text(morse_input)}")
    else:
        print("Invalid choice.")

if __name__ == '__main__':
    main()
