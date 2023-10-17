letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l" "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", ".", "?", "'", ":", "`", "-", "/", "(", ")"]
morseversion = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", "._..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----", "--..--", ".-.-.-", "..--..", ".-..-.", "---...", ".----.", "-....-", "-..-.", "-.--.", "-.--.-"]

messagetocode = input("What message would you like turned into morse code? ")

def to_morse_code(message):
    morse_code = ""
    for char in message:
        if char == " ":
            mose_code += "  "
        else:
            morse_code += morseversion[char.lower()] + " "
    print(morse_code)

to_morse_code(messagetocode)