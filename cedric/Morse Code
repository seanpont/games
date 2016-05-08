
morse_code_dict = {"A": ".-",
                   "B": "-...",
                   "C": "-.-.",
                   "D": "-..",
                   "E": ".",
                   "F": "..-.",
                   "G": "--.",
                   "H": "....",
                   "I": "..",
                   "J": ".---",
                   "K": "-.-",
                   "L": ".-..",
                   "M": "--",
                   "N": "-.",
                   "O": "---",
                   "P": ".--.",
                   "Q": "--.-",
                   "R": ".-.",
                   "S": "...",
                   "T": "-",
                   "U": "..-",
                   "V": "...-",
                   "W": ".--",
                   "X": "-..-",
                   "Y": "-.--",
                   "Z": "--..",
                   "0": "-----",
                   "1": ".----",
                   "2": "..---",
                   "3": "...--",
                   "4": "....-",
                   "5": ".....",
                   "6": "-....",
                   "7": "--...",
                   "8": "---..",
                   "9": "----."}

def to_morse_code(input):
    c_input = ""
    for letter in input:
        if letter == " ":
            c_input += "  "
        else:
            letter = letter.upper()
            c_input += morse_code_dict[letter]
            c_input += " "
    return c_input

def w_spliter(input):
    return input.split("  ")

def from_morse_code(input):
    c_input = ""
    w_list = w_spliter(input)
    for word in w_list:
        for moca in word.split():
            rd = reverse_dict(morse_code_dict)
            c_input += rd[moca]
        c_input += " "
    return c_input.lower()

def reverse_dict(dict):
    reverse_dict = {}
    for p in dict:
        reverse_dict[dict[p]] = p
    return reverse_dict




print to_morse_code("red bycicle")
print from_morse_code(to_morse_code("red bycicle"))
print from_morse_code("--- .--.")
print w_spliter(to_morse_code("red bycicle"))