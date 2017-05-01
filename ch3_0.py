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
    return(result.split(' '))


def tryAllChars(cipher):
    toute = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    thoseWords = englishDict()
    for char in toute:
        plaintest = xorSingleChar(cipher, char)
        for word in plaintest:
            if word in thoseWords:
                print(str(" ".join([y for y in plaintest])))
                print("The char is: "+char)
                return True


def englishDict():
    dicto = open('dict2')
    englishWords = dicto.read().split('\n')
    dicto.close()

    return englishWords

if __name__ == "__main__":
   
    cipher = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    
    
    #print(xorSingleChar(cipher,'X'))
    #print(englishDict()) 
    tryAllChars(cipher)
