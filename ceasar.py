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

mode = sys.argv[1]
filename = sys.argv[2]
key = sys.argv[3]

if mode == 'e':
    print(encrypt(filename, key))
elif mode == 'd':
    if key == "unknown":
        for i in range(50):
            key = i
            print(decrypt(filename, int(key)))
    elif key.isdigit():
        print(decrypt(filename, int(key)))
    else:
        print("Invalid key. Please try again.")
else:
    print("Invalid input.")
