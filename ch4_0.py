import string
import re

def xorSingleChar(hexstr,char):

    b1 = bytearray.fromhex(hexstr)
    printable = []
        
    for byte in b1:
        sym=chr(byte^ord(char))
        if re.match(r"[a-zA-Z]|[ ]", sym):
            printable.append(sym)
    result = str("".join([y for y in printable]))
    return([result.split(' '),hexstr])


def tryAllChars(cipher):
    
    toute = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789x"
    Words = loadFile('dict3')

    for char in toute:
        plaintest = xorSingleChar(cipher, char)[0]

        for word in plaintest:
            if word.upper() in Words:
                print("Ciphertext: "+ xorSingleChar(cipher, char)[1]) 
                print(str(" ".join([y for y in plaintest])))
                print("The char is: "+char+"\n")
                return True


def loadFile(name):
    dicto = open(name)
    englishWords = dicto.read().split('\n')
    dicto.close()
    return englishWords


if __name__ == "__main__":
    ciphers = loadFile('cipherfile.txt')
    for line in ciphers:
        tryAllChars(line)
