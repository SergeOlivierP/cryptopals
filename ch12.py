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
    for s in infinite_A():
        lenght = len(encryptionOracle(s, key))
        if (lenght != L):
            block_size = lenght-L
            break
    return block_size


def decrypt_first_block():
    block_size = get_block_size()
    block = b'a'*(block_size-1)
    pad = block
    for i in range(len(block)):
        if find_byte(block, pad) is not None:
            block = find_byte(block, pad)
            block = block[1:]
            pad = pad[1:]
        else:
            break
    return ''.join([chr(j) for j in block])


def infinite_A():
    for i in count():
        yield b'A'*i


def iterate_bytes(block):
    if block is not None:
        for letter in range(1, 255):
            yield block + bytes([letter])


def find_byte(block, pad, n=16):
    cipher = encryptionOracle(pad, key)
    for tries in iterate_bytes(block):
        candidate = encryptionOracle(tries, key)[:n]
        if candidate == cipher[:n]:
            return tries


def decrypt_shit(max_lenght):
    solution = []
    for k in count():
        if k > max_lenght:
            break
        blocks = b'a'*(k-1)
        pad = blocks
        for i in range(len(blocks)):
            if find_byte(blocks, pad) is not None:
                try:
                    blocks = find_byte(blocks, pad, k)
                    blocks = blocks[1:]
                    solution.append(blocks)
                    pad = pad[1:]
                except:
                    pass
    print(solution)


if __name__ == "__main__":
    L = len('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9'
            'wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ'
            '2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHR'
            'vIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c'
            '3QgZHJvdmUgYnkK')
    key = randBytes(16)
    decrypt_shit(max_lenght=L)
