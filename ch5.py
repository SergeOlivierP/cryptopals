
def xorKey(txt, key):
    buf = b''.join([key for y in range(len(txt))][:len(txt)])
    xored = bytes([txt[i] ^ buf[i] for i in range(len(txt))])
    return xored.hex()


if __name__ == "__main__":
    plain = ("Burning 'em, if you ain't quick and nimble\n"
             "I go crazy when I hear a cymbal")
    key = 'ICE'
    print(xorKey(bytes(plain, 'utf-8'), bytes(key, 'utf-8')))
