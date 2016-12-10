# README #

### Overview ###
This project has programs to decrypt and encrypt message using 4 types of cryptography, running on python 3.5:

* Vernam
* Columnar Transposition
* Ceasar Cipher
* Random Substitution

Beside the default functions, we added one new mode in Random Subtitutions and modified the decrypt functions of columnar transposition and ceasar cipher.

### Random Substitution ###
* We create a new mode to check frequency of characters in a cipher text. The input includes mode "f" and name of the cipher file.
* For ex: python3 subst.py f cipher_file

### Columnar Transposition and Ceasar Cipher###
* If the key is not known, there is a function in "coltrans.py" and "ceasar.py" program to guess all the possible key in decrypt mode. The syntax to call this mode is just simply replace the integer (which is a key) by the word "unknown"
* For ex: python3 program_name d cipher_file unknown
