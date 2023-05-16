import sys


def read_each_carac(string: str, MorseCode):
    content = ""
    for carac in string:
        content += MorseCode[carac]

    return content


def main():
    lst = []
    NESTED_MORSE =  \
        {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
         'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                    'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                    'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
                    'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
                    '1': '.----',
                    '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                    '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.', ' ': '/ '}
    if (sys.argv.__len__() >= 2):
        lst = sys.argv[1:]
        lst = [str.upper(elem) for elem in lst]

    for elem in lst:
        for cara in elem:
            if (cara.isalnum()):
                continue
            elif (cara.isspace()):
                continue
            else:
                print("wrong symbol access")
                exit(1)

    content = ""
    for elem in lst:
        content += read_each_carac(elem, NESTED_MORSE)

    print(content)


if (__name__ == "__main__"):
    main()
