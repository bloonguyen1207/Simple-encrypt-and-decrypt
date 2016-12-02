import string
import random
import sys


def check_int_input(a_string):
    for i in range(len(a_string)):
        if a_string[i] not in string.digits:
            return False
    return True


def key_generator(key_file_name, length):
    str_alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
    in_file = open(key_file_name, 'w')
    for i in range(length):
        ch_index = random.randint(0, len(str_alphabet) - 1)  # randint return n from a <= n <= b
        in_file.write(str_alphabet[ch_index])
    in_file.close()


def vernam_encryption(in_file_name, key_file_name, offset):
    str_alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
    length_alphabet = len(str_alphabet)
    in_file = open(in_file_name, 'r')
    key_file = open(key_file_name, 'r')
    message = in_file.read()
    key = key_file.read()
    enc_mes = ""

    length_message = len(message)

    # regenerate key if length of key is less than length of the message
    if length_message > len(key):
        key_generator(key_file_name, length_message)
        key_file.seek(0)
        key = key_file.read()

    length_key = len(key)

    # shift all the key by offset to make it easier to code
    if length_message <= length_key - offset:
        actual_key = key[offset: offset + length_message]
    else:
        temp = length_message - (length_key - offset)
        actual_key = key[offset:] + key[:temp]

    for i in range(length_message):
        ch_index = (str_alphabet.index(message[i]) + str_alphabet.index(actual_key[i])) % length_alphabet
        enc_mes += str_alphabet[ch_index]

    in_file.close()
    key_file.close()

    outfile = open("vernam_encrypt.enc", 'w')
    outfile.write(enc_mes)
    outfile.close()

    print(enc_mes, end='')


def vernam_decryption(in_file_name, key_file_name, offset):
    str_alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
    length_alphabet = len(str_alphabet)
    in_file = open(in_file_name, 'r')
    key_file = open(key_file_name, 'r')
    enc_mes = in_file.read()
    enc_mes = enc_mes[enc_mes.index('>') + 1: enc_mes.index('<')]  # remove > <
    key = key_file.read()
    message = ""

    length_message = len(enc_mes)
    length_key = len(key)

    # length of key must larger or equal to length of message
    if length_message > length_key:
        print("Wrong key")

    # shift all the key by offset to make it easier to code
    if length_message <= length_key - offset:
        actual_key = key[offset: offset + length_message]
    else:
        temp = length_message - (length_key - offset)
        actual_key = key[offset:] + key[:temp]

    for i in range(length_message):
        # in case the character is not found in the str_alphabet, it will be replaced with '='
        if enc_mes[i] not in str_alphabet or actual_key[i] not in str_alphabet:
            message += '='
            continue
        ch_index = (str_alphabet.index(enc_mes[i]) - str_alphabet.index(actual_key[i])) % length_alphabet
        message += str_alphabet[ch_index]

    in_file.close()
    key_file.close()

    print(message, end='')


if sys.argv[1] == 'g':      # Generate key
    if check_int_input(sys.argv[3]):
        n = int(sys.argv[3])
        key_generator(sys.argv[2], n)
elif sys.argv[1] == 'e':    # Encrypt
    if check_int_input(sys.argv[4]):
        n = int(sys.argv[4])
        vernam_encryption(sys.argv[2], sys.argv[3], n)
elif sys.argv[1] == 'd':    # Decrypt
    if check_int_input(sys.argv[4]):
        n = int(sys.argv[4])
        vernam_decryption(sys.argv[2], sys.argv[3], n)
else:                       # Mode validation
    print("Invalid input.")
