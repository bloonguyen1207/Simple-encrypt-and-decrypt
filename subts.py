import sys
import random
import json


# Check frequency of each character in the message - Can be used to guess key
def checkfrequency(file):
    alphabet = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
    frequency = {}
    with open(file, 'r') as f:
        message = f.read().rstrip().strip("<>")
    for i in alphabet:
        frequency[i] = message.count(i)
    return frequency


# Generate key file
def genkey(file):
    alphabet = list("""ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789""")
    alphabet_cp = alphabet.copy()
    key = {}

    # Get random number within alphabet length
    # Map the character with character at random index
    # Remove mapped characters
    # Keep going until we a full dictionary with key and values
    for i in range(len(alphabet)):
        index = random.randint(0, len(alphabet_cp) - 1)
        key[alphabet[i]] = alphabet_cp[index]
        alphabet_cp.pop(index)

    with open(file, 'w') as key_file:
        json.dump(key, key_file)


# Keyfile must be in dictionary format
def encrypt(file, key_file):
    # Load key as dictionary
    key = json.load(open(key_file, 'r'))

    # Read message from file and remove '<>' characters
    with open(file, 'r') as f:
        message = f.read().rstrip().strip("<>")

    # Ensure message's format
    message = message.upper()
    message_enc = ""

    # Map characters in message with characters in dictionary
    for i in message:
        if i in key:
            message_enc += key[i]
        else:
            print(i + " is not defined.")

    return message_enc


# Keyfile must be in dictionary format
def decrypt(file, key_file):
    # Load key as dictionary
    key = json.load(open(key_file, 'r'))

    # Create reversed key dictionary since cannot get key from value
    reverse_key = {}
    for k, v in key.items():
        reverse_key[v] = k

    # Read message from file and remove '<>' characters
    with open(file, 'r') as f:
        message = f.read().rstrip().strip("<>")

    # Ensure message's format
    message = message.upper()

    # Map characters in message with characters in dictionary
    message_dec = ""
    for i in message:
        if i in reverse_key:
            message_dec += reverse_key[i]
        else:
            print(i + " is not defined.")

    return message_dec


if sys.argv[1] == 'g':      # Generate key
    genkey(sys.argv[2])
elif sys.argv[1] == 'f':    # Additional mode for frequency checking
    print(checkfrequency(sys.argv[2]))
elif sys.argv[1] == 'e':    # Encrypt
    print(encrypt(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == 'd':    # Decrypt
    print(decrypt(sys.argv[2], sys.argv[3]))
else:                       # Mode validation
    print("Invalid input.")

