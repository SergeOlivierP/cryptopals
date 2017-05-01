from ch1_3_2 import getScore, xorSingleChar


def loadFile(name):
    dicto = open(name)
    englishWords = dicto.read().split('\n')
    dicto.close()
    return englishWords

if __name__ == "__main__":
    
    ciphers = loadFile('cipherfile1')
    toute = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    for line in ciphers:
        x = [getScore(xorSingleChar(line,char)) for char in toute]
        key = toute[x.index(max(x))]
        if max(x) > 2:
            print("Key is: "+ key)
            print("Cipher is: "+ line )
            print(xorSingleChar(line,key)) 

