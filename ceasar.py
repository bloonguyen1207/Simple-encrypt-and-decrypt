import os
import sys
# import coltrans


# Encrypt
def encrypt(file, key):
    # It cannot read /n properly so I don't use it
    # with open('alphabet.txt', 'r') as af:
    #     alpha = af.read().rstrip()

    # Alphabet
    alpha = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""

    # Open file and read whole file then strip newline (if any)
    # then strip '<>' characters
    with open(file, 'r') as f:
        message = f.read().rstrip().strip('<>')

    # Make sure message is uppercase so that it can be mapped with alphabet
    message = message.upper()

    message_enc = ""
    # Loop through each character in message and check with alphabet
    for c in range(len(message)):
        # If character is in alphabet, get the index of that character in alphabet
        if message[c] in alpha:
            index = alpha.find(message[c])

            # Get sum of character index with key then mod the length of alphabet
            # Then add the character at the computed index to the encrypted message
            message_enc += alpha[(index + int(key)) % len(alpha)]
        else:
            print(message[c] + " is not in alphabet.")

    return message_enc


# Undo the encryption to decrypt
def decrypt(file, key):
    return encrypt(file, -key)


# this function is used to decrypt message 6
# in order to use this function:
# + comment the main function of "coltrans.py" and this file
# + uncomment this function, "import coltrans", and "decrypt_message6(sys.argv[1])"
# + the argument only contains the name of the encrypt file.

# def decrypt_message6(in_file_name):
#     alpha = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
#     for i in range(1, len(alpha)):
#         print("---key: " + str(i) + "---")
#         message = decrypt(in_file_name, i)
#         temp_file = open("temp.txt", 'w')
#         temp_file.write(message)
#         temp_file.close()
#         message = coltrans.columnar_decryption("temp.txt", i)
#         os.remove("temp.txt")
#         print(message)


mode = sys.argv[1]
filename = sys.argv[2]
key_ar = sys.argv[3]

if mode == 'e':     # Encrypt
    print(encrypt(filename, key_ar))
elif mode == 'd':   # Decrypt
    # Try all keys if the key is unknown - input unknown for unknown key
    if key_ar == "unknown":
        for i in range(1, 50):
            key_ar = i
            print("----------------------------------------------")
            print("Key: " + str(key_ar))
            print("----------------------------------------------")
            print(decrypt(filename, int(key_ar)))
            print("----------------------------------------------")
    # Key validation
    elif key_ar.isdigit():
        print(decrypt(filename, int(key_ar)))
    else:
        print("Invalid key. Please try again.")
else:               # Mode validation
    print("Invalid input.")

# decrypt_message6(sys.argv[1])
