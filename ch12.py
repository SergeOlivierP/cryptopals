import aes
from util import splitTxt, randBytes
from itertools import count
import base64


def encryptionOracle(text, key):
    cipher = aes.ecb(key=key)
    postfix = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9'
                               'wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ'
                               '2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHR'
                               'vIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c'
                               '3QgZHJvdmUgYnkK')
    cipherText = cipher.encrypt(text + postfix)
    return cipherText


def ecbORcbc(cipher, block_size):
    blocks = splitTxt(cipher, block_size)
    if any(blocks.count(x) > 1 for x in blocks):
        return "Detected: ECB"
    else:
        return "Detected: CBC"


def get_block_size():
    L = len(encryptionOracle(b"a", key))
    for s in my_string():
        lenght = len(encryptionOracle(s, key))
        if (lenght != L):
            block_size = lenght-L
            break
    return block_size


def my_string():
    for i in count():
        yield b'A'*i


def iterate(block):
    alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 '
    for letter in alpha:
        yield block + bytes(letter, 'utf-8')


def find_byte(block):
    cipher = encryptionOracle(block, key)
    for tries in iterate(block):
        if (encryptionOracle(tries, key)[:16] == cipher[:16]):
            return bytes([tries[-1]])


if __name__ == "__main__":
    key = randBytes(16)
    block_size = get_block_size()
    block = b'a'*(block_size-1)
    found = find_byte(block)
    print(found)
