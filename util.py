

def xorStrings(bytestr1, bytestr2):
    return [ bytestr1(i)^bytestr2(i) for i in range(len(bytestr1)) ]

if __name__ == "__main__":
    
