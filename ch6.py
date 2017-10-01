import base64
import re
import numpy as np
from operator import itemgetter


def hammingDist(text1, text2):
    return sum([bin(text1[i] ^ text2[i]).count('1')
               for i in range(len(text1))])


def getNorm(k, ciph):
    d1 = hammingDist(ciph[:k], ciph[k:2*k])
    d2 = hammingDist(ciph[2*k:3*k], ciph[3*k:4*k])
    d3 = hammingDist(ciph[4*k:5*k], ciph[5*k:6*k])
    d4 = hammingDist(ciph[6*k:7*k], ciph[7*k:8*k])
    return (d1 + d2 + d3 + d4)/(4*k)


def splitCipher(keySize, cipher):
    l = len(cipher)
    splitted = [itemgetter(*range((0 + i) % keySize, l, keySize))(cipher)
                for i in range(0, keySize)]
    return splitted[0]


def xorSingleChar(bytestr, char):
    return ''.join([ord(b) ^ ord(char) for b in bytestr])


def getScore(b):

    s = str("".join([chr(j)
            for j in b if re.match(r"[a-zA-Z]|[ ]", chr(j))]))

    freqs = {
            'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835,
            'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888,
            'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
            'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645,
            'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
            'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
            'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
            }
    score = 0
    for i in s:
        c = i.lower()
        if c in freqs:
            score += freqs[c]
    return score


def findCeasarKey(cipher):
    printable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012'\
    + '3456789:,. !?"

    plain = [getScore(xorSingleChar(cipher, char)) for char in printable]
    return printable[np.argmax(plain)]


def findKeySizes(cipher, n):
    tab = []
    for i in range(2, 40):
        tab.append((i, getNorm(i, cipher)))
    tab.sort(key=lambda tup: tup[1])
    return tab[n][0]


def findKey(cipherText, KeySize):
    blocks = splitCipher(k, cipherTxt)
    print(blocks)
    splitted = [j.encode() for j in i for i in blocks]
    return "".join(findCeasarKey(splitted[l]) for l in range(0, k))


def deCipher(cipher, key):
    buf = str("".join([key for y in range(len(cipher))]))[:len(cipher)]
    result = "".join([chr(cipher[i] ^ ord(buf[i]))
                     for i in range(0, len(cipher))])
    return(result)


if __name__ == "__main__":

    with open('cipherfile2', 'r') as f:
        cipherTxt = base64.b64decode(f.read())

    for guess in range(0, 5):
        k = findKeySizes(cipherTxt, guess)
        print('Key size:', k)
        print(findKey(cipherTxt, k), "\n")
