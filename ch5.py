import string
import binascii


def xorKey(txt, key):
    buf = "".join([key for y in range(len(txt))])[:len(txt)]
    xored = "".join([hex(ord(txt[i]) ^ ord(buf[i]))[2:] for i in range(0, len(txt))])
    return xored

if __name__ == "__main__":
    plain = '''Burning 'em, if you ain't quick and nimble
    I go crazy when I hear a cymbal'''
    key = 'ICE'
    print(xorKey(plain, key))
