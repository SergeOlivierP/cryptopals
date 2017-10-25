from util import getScore
import re

def xorSingleChar(hexstr, char):
    b1 = bytearray.fromhex(hexstr)
    printable = []
    for byte in b1:
        if re.match(r"[a-zA-Z]|[ ]", chr(byte ^ ord(char))):
            printable.append(chr(byte ^ ord(char)))
    return str("".join([y for y in printable]))

def loadFile(name):
    with open(name, 'r') as f:
        dicto = f.read()
    return dicto.split('\n')


if __name__ == "__main__":

    with open('cipherfile1', 'r') as f:
        ciphers = f.read().split('\n')

    toute = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    ciphertext = ""
    key = ""
    plaintext = ""
    bestscore = 0

    for line in ciphers:
        x = [getScore(xorSingleChar(line, char)) for char in toute]
        if max(x) > bestscore:
            bestscore = max(x)
            key = toute[x.index(max(x))]
            plaintext = xorSingleChar(line,key)
            ciphertext = line

    print("Best score is: " + str(bestscore))
    print("With Key: " + key)
    print("With ciphertext: " + ciphertext)
    print("Plaintext: " + plaintext)
