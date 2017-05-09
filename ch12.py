import aes
from util import splitTxt, randBytes
import random
import base64

 

 
def encryptionOracle(text, key):
    cipher = aes.ecb(key)    
    postfix = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    cipherText = cipher.encrypt(text + postfix)
    return cipherText


def ecbORcbc(cipher):
    blocks = splitTxt(cipher, 16) 
    
    if any(blocks.count(x) > 1 for x in blocks):
        return "Detected: ECB"
    else:
        return "Detected: CBC"

def getBlockSize(text):
    return size

if __name__ == "__main__":
    key =  randBytes(16)
    mystring = b'AAAAA'
    print('number of bytes of ciphertext: ', len(encryptionOracle(mystring, key)))
    print('number of blokcs of ciphertext: ', len(encryptionOracle(mystring, key))/16)
    print(ecbORcbc(encryptionOracle(mystring, key)))
