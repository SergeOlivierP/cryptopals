from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from functools import reduce
from util import xor16, padPKCS7, splitTxt


def ecbEncrypt(key, plain):
    plain = padPKCS7(plain,16)
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    cipherTxt = encryptor.update(plain)
    return cipherTxt

def ecbDecrypt(key, ciphertxt):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertxt) + decryptor.finalize()


def cbcEncrypt(key, plain, IV):
    blocks = splitTxt(plain, 16)
    blocks[-1] = padPKCS7(blocks[-1],16)
    x0 =  xor16(blocks[0],IV)
    cipherTxt = [ecbEncrypt(key, x0)[:16]]
    for i in range(1, len(blocks)):
        x = xor16(cipherTxt[i-1], blocks[i])
        localCipher = ecbEncrypt(key, x)[:16]
        cipherTxt.append(localCipher)
    return b''.join(cipherTxt)

def cbcDecrypt(key, ciphertext, IV):
    blocks = splitTxt(ciphertext, 16)
    x0 = ecbDecrypt(key, blocks[0])
    plainList = [xor16(x0,IV)]
    for i in range(1, len(blocks)):
        plainList.append(xor16(blocks[i-1],ecbDecrypt(key, blocks[i])))
    plainList = reduce(lambda x,y: x+y,plainList)
    return "".join([chr(j) for j in plainList])

