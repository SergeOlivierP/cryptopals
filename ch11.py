import aes
from util import splitTxt
import random

def randBytes(n):
    return  b''.join([bytes([random.randint(0, 255)]) for i in range(n)])

def encryptionOracle(text):
    prefixL = random.randint(5,10)
    prefix = randBytes(prefixL)
    postfixL = random.randint(5,10)
    postfix = randBytes(postfixL)
    mode = random.randint(0,1)
    toEncrypt = prefix + text + postfix

    if mode == 0:
        print("The oracle chose: CBC")
        return aes.cbcEncrypt(randBytes(16), toEncrypt, randBytes(16))
    else:
        print("The oracle chose: ECB")
        return aes.ecbEncrypt(randBytes(16), toEncrypt)
    


def ecbORcbc(cipher):
    blocks = splitTxt(cipher, 16)
    
    if any(blocks.count(x) > 1 for x in blocks):
        return "ECB detected"
    else:
        return "CBC detected or plaintext without pattern"
    

if __name__ == "__main__":

    for i in range(10):
        plain = bytes(64)
        print(ecbORcbc(encryptionOracle(plain)), "\n")
