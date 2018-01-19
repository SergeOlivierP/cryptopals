from util import getScore
import re


def xorSingleChar_fromHex(hexstr, char):
    array = bytes.fromhex(hexstr)
    reg = re.compile(r"[a-zA-Z]|[ ]")
    printable = filter(reg.match, map(lambda x: chr(x ^ ord(char)), array))
    return str("".join(printable))


def loadFile(name):
    with open(name, 'r') as f:
        return f.readlines()


if __name__ == "__main__":

    with open('cipherfile1', 'r') as f:
        ciphers = f.read().split('\n')

    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    bestscore = 0

    for line in ciphers:
        x = list(map(lambda x: getScore(xorSingleChar_fromHex(line, x)), alpha))
        if max(x) > bestscore:
            bestscore = max(x)
            key = alpha[x.index(max(x))]
            plaintext = xorSingleChar_fromHex(line, key)
            ciphertext = line

    print("Best score is: " + str(bestscore))
    print("With Key: " + key)
    print("With ciphertext: " + ciphertext)
    print("Plaintext: " + plaintext)
