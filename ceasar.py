import sys


def encrypt(file, key):
    # with open('alphabet.txt', 'r') as af:
    #     alpha = af.read().rstrip()
    alpha = """ABCDEFGHIJKLMNOPQRSTUVWXYZ .,:;()-!?$'"\n0123456789"""
    with open(file, 'r') as f:
        message = f.read().rstrip().strip('<>')
    message = message.upper()
    message_enc = ""
    for i in range(len(message)):
        if message[i] in alpha:
            j = alpha.find(message[i])
            message_enc += alpha[(j + int(key)) % len(alpha)]
        else:
            raise Exception("Not in alphabet")

    return message_enc


def decrypt(file, key):
    return encrypt(file, -key)

if sys.argv[1] == 'e':
    print(encrypt(sys.argv[2], sys.argv[3]))
elif sys.argv[1] == 'd':
    print(decrypt(sys.argv[2], int(sys.argv[3])))
else:
    print("Invalid input.")
