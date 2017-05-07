import aes
from util import splitTxt, randBytes
import random


def encryptionOracle(text):
    prefixL = random.randint(5,10)
    prefix = randBytes(prefixL)
    postfixL = random.randint(5,10)
    postfix = randBytes(postfixL)
    mode = random.randint(0,1)
    toEncrypt = prefix + text + postfix

    if mode == 0:
        print("The oracle chose: CBC")
        ecbCipher = aes.cbc(randBytes(16), randBytes(16))
        return ecbCipher.encrypt(toEncrypt)
    else:
        print("The oracle chose: ECB")
        ecbCipher = aes.ecb(randBytes(16))
        return ecbCipher.encrypt(toEncrypt)
    


def ecbORcbc(cipher):
    blocks = splitTxt(cipher, 16)
    
    if any(blocks.count(x) > 1 for x in blocks):
        return "Detected: ECB"
    else:
        return "Detected: CBC"
    

if __name__ == "__main__":

    for i in range(10):
        plain = bytes(64)
        #plain = bytes(open('plain.txt', 'r').read(), 'utf-8')
        print(ecbORcbc(encryptionOracle(plain)), "\n")
