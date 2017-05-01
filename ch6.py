import string
import binascii
import base64
import re
from operator import itemgetter


def hammingDist(text1,text2):
    return sum([bin(text1[i] ^ text2[i]).count('1') for i in range(len(text1))])


def getNorm(k,ciph):
    return hammingDist(ciph[:k],ciph[k:2*k])/k


def splitCipher(keySize, cipher):
    l = len(cipher)
    splitted = [itemgetter(*range((0 + i) % keySize, l, keySize))(cipher) for i in range(0,keySize)]    
    return splitted


def xorSingleChar(bytelist,char):

    printable = []

    for byte in bytelist:
        sym=chr(ord(byte)^ord(char))
        if re.match(r"[a-zA-Z]|[ ]", sym):
            printable.append(sym)
    result = str("".join([y for y in printable]))
    return result


def getScore(s):

    freqs = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442,
    'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033,
    'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302,
    'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984,
    'z': 0.0007836, ' ': 0.1918182
    }
    score = 0
    for i in s:
        c = i.lower()
        if c in freqs:
            score += freqs[c]
    return score


def findSingleKey(cipher):
    toute = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:,. !?"
    plain = [getScore(xorSingleChar(cipher,char)) for char in toute]
    key = toute[plain.index(max(plain))]
    return(key,max(plain))


def findKeySizes(cipher):
    tab = []
    for i in range(2,40):
        tab.append((i,getNorm(i,cipher)))
    tab.sort(key=lambda tup: tup[1])
    keyS = tab[0][0]
    return (tab[0][0],tab[1][0],tab[2][0],tab[3][0],tab[4][0])


if __name__ == "__main__":
    
    cipherTxt = base64.b64decode(open('cipherfile2', 'r').read()) 
    
    probableSizes = findKeySizes(cipherTxt)


    for k in probableSizes:
        print('**************************')
        print("Trying size: ", k)
        y = splitCipher(k, cipherTxt)
        splitted = [[chr(j) for j in i] for i in y]
        for l in range(0, k):
            print('probable key char for char', l)
            print(findSingleKey(splitted[l]))

        
