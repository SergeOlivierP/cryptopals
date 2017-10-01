import base64
from Crypto.Cipher import AES
import util


class cbc:
    def __init__(self, key, IV):
        self._ECB = AES.new(key, AES.MODE_ECB)
        self._IV = IV
        self._blksize = 16

    def _getBlocks(self, s):
        return [s[i:i+self._blksize] for i in range(0, len(s), self._blksize)]

    def encrypt(self, plaintext):
        plainblocks = self._getBlocks(plaintext)
        plainblocks[-1] = util.padPKCS7(plainblocks[-1])
        ciphertext = b''
        prev = self._IV
        for i in range(len(plainblocks)):
            plainblock = plainblocks[i]
            cipherblock = self._ECB.encrypt(util.xor16(plainblock, prev))
            ciphertext += cipherblock
            prev = cipherblock
        return ciphertext

    def decrypt(self, ciphertext):
        cipherblocks = self._getBlocks(ciphertext)
        plaintext = b''
        prev = self._IV
        for i in range(len(cipherblocks)):
            cipherblock = cipherblocks[i]
            plainblock = util.xor16(self._ECB.decrypt(cipherblock), prev)
            plaintext += plainblock
            prev = cipherblock
        return plaintext


class ecb:
    def __init__(self, key):
        self._cipher = AES.new(key, AES.MODE_ECB)
        self._key = key

    def encrypt(self, text):
        paddedtext = util.padPKCS7(text)
        return self._cipher.encrypt(paddedtext)

    def decrypt(self, ciphertext):
        return self._cipher.decrypt(ciphertext)


if __name__ == '__main__':
    x = base64.b64decode(open('cipherfile5', 'r').read())

    key = b'YELLOW SUBMARINE'
    cipher = cbc(key, bytes([0] * 16))
    y = cipher.decrypt(x)
    print(y.decode('utf-8'))
    z = cipher.encrypt(y)
    print(z)
