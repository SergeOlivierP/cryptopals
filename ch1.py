import base64


a = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e'\
    + '6f7573206d757368726f6f6d'
b = bytes.fromhex(a)
c = base64.b64encode(b)
print(b)
print(c)
print(help(bytes()))
