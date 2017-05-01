import string
import binascii

def xorKey(plaintext,key):
    printable = []
    bufferKey = str("".join([key for y in range(len(plaintext))]))[:len(plaintext)]
    i=0
    for char in plaintext:
        sym=ord(char)^ord(bufferKey[i])
        i += 1
        printable.append(sym)
    result = "".join([hex(y)[2:] for y in printable])
    return(result)

if __name__ == "__main__":
    plain1 = "Burning 'em, if you ain't quick and nimble"
    plain2 = "I go crazy when I hear a cymbal"
    key = "ICE"
    print(xorKey(plain1,key)+'\n')
    print(xorKey(plain2,key)+'\n')

