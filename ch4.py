from util import getScore, xorSingleChar


def loadFile(name):
    with open(name, 'r') as f:
        dicto = f.read()
    return dicto.split('\n')


if __name__ == "__main__":

    with open('cipherfile1', 'r') as f:
        ciphers = f.read().split('\n')

    toute = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    for line in ciphers:

        x = [getScore(xorSingleChar(line, char)) for char in toute]
        key = toute[x.index(min(x))]

        if min(x) < 15:
            print("For key: " + key)
            print("Entropy is: ", min(x))
            print("Cipher is: " + line)
            print("Plaintext is: ", xorSingleChar(line, key), '\n')
