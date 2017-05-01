import string
import re

def xorSingleChar(hexstr,char):

    b1 = bytearray.fromhex(hexstr)
    printable = []
        
    for byte in b1:
        sym=chr(byte^ord(char))
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

def findKey(cipher,symbols):
    plain = [getScore(xorSingleChar(cipher,char)) for char in toute]
    key = toute[plain.index(max(plain))]
    return((plain,key))

if __name__ == "__main__":
    
    cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    toute = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" 
    solution = findKey(cipher, toute)
    print("Key is: "+ solution[1])
    print()
    print(solution[0])

