from operator import itemgetter
import binascii


def decodeLines(filename):

    with open(filename, 'r') as f:
        c = f.read()

    for line in c:
        if line[-1] == '\n':
            line = line[:-1]
        s = binascii.unhexlify(line)
        yield s


def splitAES(cipher):
    k = 16
    return [cipher[i:i+k] for i in range(0, len(cipher), k)]


def isECB(line):
    blocks = splitAES(line)
    return any(blocks.count(x) > 1 for x in blocks)


if __name__ == "__main__":

    cipherTxt = decodeLines('cipherfile4')
    index = 0
    for line in cipherTxt:
        index += 1
        if isECB(line):
            print('Line:', index)
