
def padding_validation(string):
    pad = string[-1]
    test = string[-pad:]
    return all(i == pad for i in test)


if __name__ == '__main__':
    string1 = b"ICE ICE BABY\x04\x04\x04\x04"
    string2 = b"ICE ICE BABY\x01\x02\x03\x04"

    print(padding_validation(string1))
    print(padding_validation(string2))
