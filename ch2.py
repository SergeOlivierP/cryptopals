b1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
b2 = bytes.fromhex("686974207468652062756c6c277320657965")
b3 = [b1[b] ^ b2[b] for b in range(len(b1))]
print("".join([(("{:x}".format(x))) for x in b3]))
