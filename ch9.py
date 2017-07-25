def padPKCS7(text, keyL):
    pad = keyL - (len(text) % keyL)
    return text + bytes([pad] * pad)

if __name__ == "__main__":
    text = b'all i want'
    print(padPKCS7(text, 16))
