"""
author: Yarden Hadas
Date: 29/10
Description: Encrypting and Decrypting messages to save Romeo, depending on which parameter was entered to sys.argv
"""
import sys
import logging

logging.basicConfig(filename="logi.log", level="DEBUG")
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
    """
    param msg: massage to encrypt
    return: the encrypted massage
    """
    if not len(msg) == 0:
        temp = []
        for letter in msg:
            temp.append(MILON_ENCRYPT[letter])
        msg = ",".join(temp)
        return msg
    else:
        return ""


def decrypt_text(msg):
    """

    :param msg: massage to decrypt
    :return:
    """
    temp = ""
    num_array = msg.split(",")
    for num in num_array:
        temp += MILON_DECRYPT[num]
    return temp


def write_to_file(msg):
    """
    :param msg: the encrypted message that will be written to a file
    :return: none
    """
    try:
        file_handle = open(FILE_NAME_LOVE_STORY, 'w')
        file_handle.write(msg)
        file_handle.close()
    except IOError:
        print("error writing to file failed")


def get_encrypted_information():
    """
    :param: none
    :return: the massage decrypted from the file with the encrypted massage
    """
    try:
        file_handle = open(FILE_NAME_LOVE_STORY, 'r')
        msg = file_handle.read()
        file_handle.close()
        return msg
    except Exception as err:
        print(err)


def main():
    if sys.argv[FIRST_NAME] == 'encrypt':
        msg = input("enter the secret massage you want to encrypt: ")
        logging.debug("encryption_input: " + msg)
        msg = encrypt_text(msg)
        logging.debug("encryption_output: " + msg)
        write_to_file(msg)
    elif sys.argv[FIRST_NAME] == 'decrypt':
        msg = get_encrypted_information()
        logging.debug("decryption_input: " + msg)
        msg = decrypt_text(msg)
        logging.debug("decryption_output: " + msg)
        print(msg)
    else:
        print("You have entered wrong parameters")


if __name__ == '__main__':
    """
    checking
    """
    assert encrypt_text("") == ""
    assert encrypt_text("My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I "
                        "have, for both are infinite.") == ("48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,"
                                                            "35,15,33,16,90,90,98,12,90,98,91,19,16,98,90,16,12,99,"
                                                            "98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,"
                                                            "91,19,16,98,34,36,39,16,98,44,98,18,30,93,16,98,91,36,"
                                                            "98,91,19,16,16,99,98,65,19,16,98,34,36,39,16,98,44,98,"
                                                            "19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,12,39,16,"
                                                            "98,30,35,17,30,35,30,91,16,100")
    assert encrypt_text("Don't waste your love on somebody, who doesn't value it.") == ("59,36,35,102,91,98,94,12,90,"
                                                                                        "91,16,98,96,36,92,39,98,33,"
                                                                                        "36,93,16,98,36,35,98,90,36,"
                                                                                        "34,16,13,36,15,96,99,98,94,"
                                                                                        "19,36,98,15,36,16,90,35,102,"
                                                                                        "91,98,93,12,33,92,16,98,30,"
                                                                                        "91,100")
    assert encrypt_text("Love is a smoke raised with the fume of sighs; Being purged, a fire sparkling in lovers' "
                        "eyes; Being vexed a sea nourish'd with loving tears: What is it else? a madness most "
                        "discreet, A choking gall, and a preserving sweet.") == ('47,36,93,16,98,30,90,98,12,98,90,34,'
                                                                                 '36,32,16,98,39,12,30,90,16,15,98,'
                                                                                 '94,30,91,19,98,91,19,16,98,17,92,'
                                                                                 '34,16,98,36,17,98,90,30,18,19,90,'
                                                                                 '101,98,57,16,30,35,18,98,37,92,39,'
                                                                                 '18,16,15,99,98,12,98,17,30,39,16,'
                                                                                 '98,90,37,12,39,32,33,30,35,18,98,'
                                                                                 '30,35,98,33,36,93,16,39,90,102,98,'
                                                                                 '16,96,16,90,101,98,57,16,30,35,18,'
                                                                                 '98,93,16,95,16,15,98,12,98,90,16,'
                                                                                 '12,98,35,36,92,39,30,90,19,102,15,'
                                                                                 '98,94,30,91,19,98,33,36,93,30,35,'
                                                                                 '18,98,91,16,12,39,90,105,98,68,19,'
                                                                                 '12,91,98,30,90,98,30,91,98,16,33,'
                                                                                 '90,16,103,98,12,98,34,12,15,35,16,'
                                                                                 '90,90,98,34,36,90,91,98,15,30,90,'
                                                                                 '14,39,16,16,91,99,98,56,98,14,19,'
                                                                                 '36,32,30,35,18,98,18,12,33,33,99,'
                                                                                 '98,12,35,15,98,12,98,37,39,16,90,'
                                                                                 '16,39,93,30,35,18,98,90,94,16,16,'
                                                                                 '91,100')

    assert encrypt_text("My only love sprung from my only hate! Too early seen unknown, and known too late! "
                        "Prodigious birth of love it is to me That I must love a loathed enemy.") == ("48,96,98,36,35,"
                                                                                                      "33,96,98,33,"
                                                                                                      "36,93,16,98,"
                                                                                                      "90,37,39,92,"
                                                                                                      "35,18,98,17,"
                                                                                                      "39,36,34,98,"
                                                                                                      "34,96,98,36,"
                                                                                                      "35,33,96,98,"
                                                                                                      "19,12,91,16,"
                                                                                                      "104,98,65,36,"
                                                                                                      "36,98,16,12,"
                                                                                                      "39,33,96,98,"
                                                                                                      "90,16,16,35,"
                                                                                                      "98,92,35,32,"
                                                                                                      "35,36,94,35,"
                                                                                                      "99,98,12,35,"
                                                                                                      "15,98,32,35,"
                                                                                                      "36,94,35,98,"
                                                                                                      "91,36,36,98,"
                                                                                                      "33,12,91,16,"
                                                                                                      "104,98,61,39,"
                                                                                                      "36,15,30,18,"
                                                                                                      "30,36,92,90,"
                                                                                                      "98,13,30,39,"
                                                                                                      "91,19,98,36,"
                                                                                                      "17,98,33,36,"
                                                                                                      "93,16,98,30,"
                                                                                                      "91,98,30,90,"
                                                                                                      "98,91,36,98,"
                                                                                                      "34,16,98,65,"
                                                                                                      "19,12,91,98,"
                                                                                                      "44,98,34,92,"
                                                                                                      "90,91,98,33,"
                                                                                                      "36,93,16,98,"
                                                                                                      "12,98,33,36,"
                                                                                                      "12,91,19,16,"
                                                                                                      "15,98,16,35,"
                                                                                                      "16,34,96,100")

    assert (decrypt_text("48,96,98,13,36,92,35,91,96,98,30,90,98,12,90,98,13,36,92,35,15,33,16,90,90,98,12,90,98,91,"
                         "19,16,98,90,16,12,99,98,48,96,98,33,36,93,16,98,12,90,98,15,16,16,37,101,98,91,19,16,98,34,"
                         "36,39,16,98,44,98,18,30,93,16,98,91,36,98,91,19,16,16,99,98,65,19,16,98,34,36,39,16,98,44,"
                         "98,19,12,93,16,99,98,17,36,39,98,13,36,91,19,98,12,39,16,98,30,35,17,30,35,30,91,16,100") ==
            "My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I have, "
            "for both are infinite.")

    assert (decrypt_text("59,36,35,102,91,98,94,12,90,91,16,98,96,36,92,39,98,33,36,93,16,98,36,35,98,90,36,34,16,13,"
                         "36,15,96,99,98,94,19,36,98,15,36,16,90,35,102,91,98,93,12,33,92,16,98,30,91,100") ==
            ("Don't "
             "waste"
             " your "
             "love "
             "on "
             "somebody, who doesn't value it."))

    assert decrypt_text("47,36,93,16,98,30,90,98,12,98,90,34,36,32,16,98,39,12,30,90,16,15,98,94,30,91,19,98,91,19,"
                        "16,98,17,92,34,16,98,36,17,98,90,30,18,19,90,101,98,57,16,30,35,18,98,37,92,39,18,16,15,99,"
                        "98,12,98,17,30,39,16,98,90,37,12,39,32,33,30,35,18,98,30,35,98,33,36,93,16,39,90,102,98,16,"
                        "96,16,90,101,98,57,16,30,35,18,98,93,16,95,16,15,98,12,98,90,16,12,98,35,36,92,39,30,90,19,"
                        "102,15,98,94,30,91,19,98,33,36,93,30,35,18,98,91,16,12,39,90,105,98,68,19,12,91,98,30,90,98,"
                        "30,91,98,16,33,90,16,103,98,12,98,34,12,15,35,16,90,90,98,34,36,90,91,98,15,30,90,14,39,16,"
                        "16,91,99,98,56,98,14,19,36,32,30,35,18,98,18,12,33,33,99,98,12,35,15,98,12,98,37,39,16,90,"
                        "16,39,93,30,35,18,98,90,94,16,16,91,100") == ("Love is a smoke raised with the fume of sighs; "
                                                                       "Being purged, a fire sparkling in lovers' "
                                                                       "eyes; Being vexed a sea nourish'd with loving "
                                                                       "tears: What is it else? a madness most "
                                                                       "discreet, A choking gall, and a preserving "
                                                                       "sweet.")

    assert decrypt_text("48,96,98,36,35,33,96,98,33,36,93,16,98,90,37,39,92,35,18,98,17,39,36,34,98,34,96,98,36,35,"
                        "33,96,98,19,12,91,16,104,98,65,36,36,98,16,12,39,33,96,98,90,16,16,35,98,92,35,32,35,36,94,"
                        "35,99,98,12,35,15,98,32,35,36,94,35,98,91,36,36,98,33,12,91,16,104,98,61,39,36,15,30,18,30,"
                        "36,92,90,98,13,30,39,91,19,98,36,17,98,33,36,93,16,98,30,91,98,30,90,98,91,36,98,34,16,98,"
                        "65,19,12,91,98,44,98,34,92,90,91,98,33,36,93,16,98,12,98,33,36,12,91,19,16,15,98,16,35,16,"
                        "34,96,100") == ("My only love sprung from my only hate! Too early seen unknown, and known too "
                                         "late! Prodigious birth of love it is to me That I must love a loathed enemy.")

    main()
