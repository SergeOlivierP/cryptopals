from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from functools import reduce
import base64


def xor(bytestr1, bytestr2):
    return [bytestr1[i] ^ bytestr2[i] for i in range(len(bytestr1))]


def padPKCS7(text, keyL):
    pad = keyL - (len(text) % keyL)
    return text + bytes([pad] * pad)


def splitTXT(text, keySize):
    k = keySize
    return [text[i:i+k] for i in range(0, len(text), k)]


def aesECBEncrypt(key, plain):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    return encryptor.update(plain) + encryptor.finalize()


def aesECBDecrypt(key, ciphertxt):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertxt) + decryptor.finalize()


def aesCBCEncrypt(key, plain, IV):
    blocks = splitTXT(plain, 16)
    blocks[-1] = padPKCS7(blocks[-1], 16)
    x0 = xor(blocks[0], IV)
    cipherTxt = [aesECBEncrypt(key, x0)]
    for i in range(1, len(blocks)):
        x = xor(cipherTxt[i-1], blocks[i])
        cipherTxt.append(aesECBEncrypt(key, x))
    return b''.join(cipherTxt)


def aesCBCDecrypt(key, ciphertext, IV):
    blocks = splitTXT(ciphertext, 16)
    x0 = aesECBDecrypt(key, blocks[0])
    plainList = [xor(x0, IV)]
    for i in range(1, len(blocks)):
        plainList.append(xor(blocks[i-1], aesECBDecrypt(key, blocks[i])))
    plainList = reduce(lambda x, y: x+y, plainList)
    return "".join([chr(j) for j in plainList])


if __name__ == "__main__":

    key = b'YELLOW SUBMARINE'
    plain = b'1 secret message2 secret message'
    IV = bytes(16)

    with open('cipherfile5', 'r') as f:
        c = f.read()
    x = base64.b64decode(c)

    print(aesCBCDecrypt(key, x, IV))
