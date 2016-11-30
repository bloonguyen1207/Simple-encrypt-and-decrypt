import os.path
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
        ch_index = random.randint(0, len(str_alphabet) - 1)
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

    if length_message > len(key):
        key_generator(key_file_name, length_message)
        key_file.seek(0)
        key = key_file.read()

    length_key = len(key)

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
    key = key_file.read()
    message = ""

    length_message = len(enc_mes)
    length_key = len(key)

    if length_message > length_key:
        print("Wrong key")

    if length_message <= length_key - offset:
        actual_key = key[offset: offset + length_message]
    else:
        temp = length_message - (length_key - offset)
        actual_key = key[offset:] + key[:temp]

    for i in range(length_message):
        ch_index = (str_alphabet.index(enc_mes[i]) - str_alphabet.index(actual_key[i])) % length_alphabet
        message += str_alphabet[ch_index]

    in_file.close()
    key_file.close()

    print(message, end='')


mode = sys.argv[1]
file_name = sys.argv[2]
key_name = sys.argv[3]
str_n = sys.argv[4]
n = 1
if mode != "g" and not os.path.isfile(file_name):
    print("Wrong input")
if not os.path.isfile(key_name):
    print("Wrong input")
if check_int_input(str_n):
    n = int(str_n)
else:
    print("Wrong input")
if mode == "e":
    vernam_encryption(file_name, key_name, n)
elif mode == "d":
    vernam_decryption(file_name, key_name, n)
elif mode == "g":
    key_generator(key_name, n)