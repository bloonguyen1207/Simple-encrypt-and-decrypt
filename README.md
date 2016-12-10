# README #

This project has programs to decrypt and encrypt message using 4 types of cryptography, running on python 3.5:
* Vernam
* Columnar Transposition
* Ceasar Cipher
* Random Substitution

Beside the default functions, we add two new modes, one in Columnar Transposition and one in Random Subtitutions.

## Columnar Transposition ##
* If the key is not known, there is a function in "coltrans.py" program to guess all the possible key in decrypt mode. The syntax to call this mode is just simply replace the integer (which is a key) by the word "unknown"
* For ex: python3 coltrans.py d cipher_file unknown