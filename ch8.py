import binascii


def decodeLines(lines):
    s = ""
    for line in lines:
        if line[-1] == '\n':
            line = line[:-1]
        s = binascii.unhexlify(line)
        yield s


def isECB(line):
    k = 16
    blocks = [line[i:i+k] for i in range(0, len(line), k)]
    return any(blocks.count(x) > 1 for x in blocks)


if __name__ == "__main__":

    with open('cipherfile4', 'r') as f:
        c = f.readlines()

    cipherTxt = decodeLines(c)
    for i, line in enumerate(cipherTxt):
        if isECB(line):
            print("line: {} : {}".format(i, line))
