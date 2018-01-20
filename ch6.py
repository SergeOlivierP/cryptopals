import base64
import re
import numpy as np


def deCipher(cipher, key):
    buf = str("".join([key for y in range(len(cipher))]))[:len(cipher)]
    result = "".join([chr(cipher[i] ^ ord(buf[i]))
                     for i in range(0, len(cipher))])
    return(result)


def hamming_dist(text1, text2):
    return sum([bin(text1[i] ^ text2[i]).count('1')
               for i in range(len(text1))])


def getNorm(k, ciph):
    d1 = hamming_dist(ciph[:k], ciph[k:2*k])
    d2 = hamming_dist(ciph[2*k:3*k], ciph[3*k:4*k])
    d3 = hamming_dist(ciph[4*k:5*k], ciph[5*k:6*k])
    d4 = hamming_dist(ciph[6*k:7*k], ciph[7*k:8*k])
    return (d1 + d2 + d3 + d4)/(4*k)


def findKeySizes(cipher, n):
    tab = []
    for i in range(2, 40):
        tab.append((i, getNorm(i, cipher)))
    tab.sort(key=lambda tup: tup[1])
    return [tab[i][0] for i in range(n)]


def xorSingleChar(bytestr, char):
    return ''.join([chr(b ^ ord(char)) for b in bytestr])


def getScore(b):

    blob = str("".join([j for j in b if re.match(r"[a-zA-Z]|[ ]", j)]))

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
    for i in blob:
        if i.lower() in freqs:
            score += freqs[i.lower()]
    return score


def findCeasarKey(cipher):
    printable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012'\
    + '3456789:,. !?"

    plain = [getScore(xorSingleChar(cipher, char)) for char in printable]
    return printable[np.argmax(plain)]


def splitCipher(cipher_text, k):
    blocks = splitTxt(k, cipher_text)
    return [blob for blob in transpose(blocks[:-1])]


def splitTxt(keySize, cipher):
    l = len(cipher)
    return [list(cipher[i:i+keySize]) for i in range(0, l, keySize)]


def transpose(blocks):
    return [tup for tup in list(zip(*blocks))]


if __name__ == "__main__":

    with open('cipherfile2', 'r') as f:
        c = f.read()

    cipher_txt = base64.b64decode(c)
    key_lenghts = findKeySizes(cipher_txt, 5)

    for guess in key_lenghts:
        print('Key size:', guess)
        splitted = splitCipher(cipher_txt, guess)
        key = "".join(findCeasarKey(splitted[l]) for l in range(len(splitted)))
        print(key, "\n")
