import aes
import base64
import random
from itertools import count


def encryption_oracle(key, rand, text, postfix):

    cipher = aes.ecb(key=key)
    postfix = base64.b64decode(postfix)
    cipherText = cipher.encrypt(rand + text + postfix)
    return cipherText


def random_bytes(n):
    return b''.join([bytes([random.randint(0, 255)]) for i in range(n)])


def overflow(i, postfix):
    return encryption_oracle(key, rand, b'a'*i, postfix)


def extract_suffix(blocks):
    for i, block in enumerate(blocks):
        if block == blocks[i-1]:
            return blocks[i+1:]


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


key = random_bytes(16)
n = random.randint(1, 70)
rand = random_bytes(n)

if __name__ == '__main__':
    postfix = ('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9'
               'wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ'
               '2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHR'
               'vIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c'
               '3QgZHJvdmUgYnkK')
    for i in count():
        buffered = overflow(i, postfix)
        blocks = [buffered[j: j+16] for j in range(0, len(buffered), 16)]
        if extract_suffix(blocks) is not None:
            cipher = b''.join(extract_suffix(blocks))
            break
