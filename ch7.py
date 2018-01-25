import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


key = b'YELLOW SUBMARINE'
ciphertext = base64.b64decode(open('cipherfile3', 'r').read())

cipher = algorithms.AES(key)
mode = modes.ECB()

decryptor = Cipher(cipher, mode, backend=default_backend()).decryptor()
plaintext = decryptor.update(ciphertext)

print(plaintext)
