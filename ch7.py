import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = b'YELLOW SUBMARINE'
x = base64.b64decode(open('cipherfile3', 'r').read())

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
decryptor = cipher.decryptor()
dec = decryptor.update(x) + decryptor.finalize()
print(dec.decode("utf-8"))
