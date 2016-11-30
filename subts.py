import sys
import random
import json


def checkfrequency(file):
    alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
    frequency = {}
    with open(file, 'r') as f:
        message = f.read().rstrip().strip("<>")
    for i in alphabet:
        frequency[i] = message.count(i)
    return frequency


def genkey(file):
    alphabet = list("""ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789""")
    alphabet_cp = alphabet.copy()
    key = {}

    for i in range(len(alphabet)):
        index = random.randint(0, len(alphabet_cp) - 1)
        key[alphabet[i]] = alphabet_cp[index]
        alphabet_cp.pop(index)

    with open(file, 'w') as key_file:
        json.dump(key, key_file)


def encrypt(file, key_file):
    key = json.load(open(key_file, 'r'))
    with open(file, 'r') as f:
        message = f.read().rstrip().strip("<>")
    message = message.upper()
    message_enc = ""
    for i in message:
        if i in key:
            message_enc += key[i]
    return message_enc


def decrypt(file, key_file):
    key = json.load(open(key_file, 'r'))
    reverse_key = {}
    for k, v in key.items():
        reverse_key[v] = k
    with open(file, 'r') as f:
        message = f.read().rstrip().strip("<>")

    message = message.upper()

    message_dec = ""
    for i in message:
        if i in reverse_key:
            message_dec += reverse_key[i]
    return message_dec


if sys.argv[1] == 'g':
    genkey(sys.argv[2])
elif sys.argv[1] == 'f':
    print(checkfrequency(sys.argv[2]))
elif sys.argv[1] == 'e':
    print(encrypt(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == 'd':
    print(decrypt(sys.argv[2], sys.argv[3]))
else:
    print("Invalid input.")

