import sys

FILE_NAME_LOVE_STORY = "encrypted_msg.txt"
FIRST_NAME = 1
MILON_ENCRYPT = {'A': '56', 'B': '57', 'C': '58', 'D': '59', 'E': '40', 'F': '41', 'G': '42', 'H': '43', 'I': '44',
                 'J': '45',
                 'K': '46', 'L': '47', 'M': '48', 'N': '49', 'O': '60', 'P': '61', 'Q': '62', 'R': '63', 'S': '64',
                 'T': '65',
                 'U': '66', 'V': '67', 'W': '68', 'X': '69', 'Y': '10', 'Z': '11', 'a': '12', 'b': '13', 'c': '14',
                 'd': '15',
                 'e': '16', 'f': '17', 'g': '18', 'h': '19', 'i': '30', 'j': '31', 'k': '32', 'l': '33', 'm': '34',
                 'n': '35',
                 'o': '36', 'p': '37', 'q': '38', 'r': '39', 's': '90', 't': '91', 'u': '92', 'v': '93', 'w': '94',
                 'x': '95',
                 'y': '96', 'z': '97', ' ': '98', ',': '99', '.': '100', ';': '101', "'": '102', '?': '103', '!': '104',
                 ':':
                     '105'}
MILON_DECRYPT = {v: k for k, v in MILON_ENCRYPT.items()}


def encrypt_text(msg):
    if not len(msg) == 0:
        temp = list(msg)
        for letter in temp:
            temp[letter] = MILON_ENCRYPT.get(temp[letter])
        msg = ", ".join(temp)
        file_handle = open(FILE_NAME_LOVE_STORY, 'w')
        file_handle.write(msg)
        file_handle.close()
    else:
        file_handle = open(FILE_NAME_LOVE_STORY, 'w')
        file_handle.write("")
        file_handle.close()


def decrypt_text(msg):
    temp = list(msg)
    for letter in temp:
        temp[letter] = MILON_DECRYPT.get(temp[letter])
    msg = ", ".join(temp)
    print(msg)


def main():
    if sys.argv[FIRST_NAME] == 'encrypt':
        msg = input("enter the secret massage you want to encrypt: ")
        try:
            encrypt_text(msg)
        except Exception:
            print("couldn't encrypt the massage")
    elif sys.argv[FIRST_NAME] == 'decrypt':
        try:
            file_handle = open(FILE_NAME_LOVE_STORY, 'r')
            msg = file_handle.read()
            file_handle.close()
            decrypt_text(msg)
        except Exception:
            print("couldn't decrypt the massage")

    else:
        print("You have entered wrong parameters")


if __name__ == '__main__':
    main()
