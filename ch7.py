import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


backend = default_backend()
key = b'YELLOW SUBMARINE'
# x = base64.b64decode(open('cipherfile3', 'r').read())

plain = b'a secret message'

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)

decryptor = cipher.decryptor()
encryptor = cipher.encryptor()


cipherText = encryptor.update(plain) + encryptor.finalize()

plain = decryptor.update(x) + decryptor.finalize()

print(base64.b64encore(cipherText))
