import aes
from re import sub
import random


def random_bytes(n):
    return b''.join([bytes([random.randint(0, 255)]) for i in range(n)])


def padPKCS7(text):
    pad = 16 - (len(text) % 16)
    return text + bytes([pad] * pad)


def sandwich(key, IV, text):
    prefix = b"comment1=cooking%20MCs;userdata="
    suffix = b";comment2=%20like%20a%20pound%20of%20bacon"
    text = bytes(sub('[\;\=]', '-LOL-', text), 'utf-8')
    pad = padPKCS7(prefix+text+suffix)
    cipher = aes.cbc(key=key, IV=IV)
    return cipher.encrypt(pad)


def find_admin(key, IV, ciphertext):
    cipher = aes.cbc(key=key, IV=IV)
    plaintext = cipher.decrypt(ciphertext)
    print(plaintext)
    return b'admin=true' in plaintext


if __name__ == '__main__':

    key = random_bytes(16)
    IV = random_bytes(16)
    ciphertext = sandwich(key, IV, 'YELLOW SUBMARINE')
    material = ciphertext[32:48]
    plain = b';comment2=%20lik'
    admin = b'admin=true;aaaaa'
    stuff = [admin[i] ^ plain[i] for i in range(0, 16)]
    stuff2 = [stuff[i] ^ material[i] for i in range(16)]
    ciphertext2 = ciphertext[:32] + bytes(stuff2) + ciphertext[48:]
    print(ciphertext2)

    print(find_admin(key, IV, ciphertext2))
