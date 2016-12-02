import string
import sys
# import ceasar


def check_int_input(a_string):
    for i in range(len(a_string)):
        if a_string[i] not in string.digits:
            return False
    return True


def columnar_encryption(in_file_name, int_key):
    in_file = open(in_file_name, 'r')
    enc_mes = ""

    message = in_file.read()

    rows = len(message) // int_key

    if len(message) % int_key != 0:
        rows += 1

    for i in range(int_key):
        for j in range(rows):
            ch_index = i + j * int_key
            if ch_index >= len(message):
                enc_mes += ' '
            else:
                enc_mes += message[ch_index]

    in_file.close()
    print(enc_mes, end='')


def columnar_decryption(in_file_name, int_key):
    in_file = open(in_file_name, 'r')
    message = ""

    enc_mes = in_file.read().rstrip().strip('<>')

    rows = len(enc_mes) // int_key

    for i in range(rows):
        for j in range(int_key):
            ch_index = i + j * rows
            message += enc_mes[ch_index]

    in_file.close()
    return message


def col_dec_without_key(in_file_name):
    in_file = open(in_file_name, 'r')
    enc_mes = in_file.read()
    enc_mes = enc_mes[enc_mes.index('>') + 1: enc_mes.index('<')]  # remove > <
    print(enc_mes)
    length_enc = len(enc_mes)
    print("Length of message: " + str(length_enc))
    key_list = []

    for i in range(2, length_enc // 2):
        if length_enc % i == 0:
            key_list.append([i, length_enc // i])  # store number of col and row
            key_list.append([length_enc // i, i])  # reverse col and row

    print(["Key list: "] + key_list)

    for k in range(len(key_list)):
        cols = key_list[k][0]
        rows = key_list[k][1]
        message = ""
        for i in range(rows):
            for j in range(cols):
                ch_index = i + j * rows
                message += enc_mes[ch_index]
        print("----key: " + str(cols) + "----")
        print(message, end='')
        print("--------------")

    in_file.close()


# this function is used to decrypt message 6
# in order to use this function:
# + comment the main function of "ceasar.py" and this file
# + uncomment this function, "import ceasar", and "decrypt_message6(sys.argv[1])"
# + the argument only contains the name of the encrypt file.

# def decrypt_message6(in_file_name):
#     in_file = open(in_file_name, 'r')
#     enc_mes = in_file.read().strip("<>")
#     for i in range(1, len(enc_mes)):
#         print("---key: " + str(i) + "---")
#         message = columnar_decryption(in_file_name, i)
#         message = ceasar.decrypt_with_string(message, i)
#         print(message)


mode = sys.argv[1]
file_name = sys.argv[2]
str_key = sys.argv[3]
key = 1

if str_key != "unknown" and check_int_input(str_key):
    key = int(str_key)
if mode == "e":
    columnar_encryption(file_name, key)
elif mode == "d":
    # if key is "unknown", the program will try all appropriate keys
    if str_key == "unknown":
        col_dec_without_key(file_name)
    else:
        print(columnar_decryption(file_name, key), end='')

# decrypt_message6(sys.argv[1])
