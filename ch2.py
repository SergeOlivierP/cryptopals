b1=bytearray.fromhex("1c0111001f010100061a024b53535009181cff")
b2=bytearray.fromhex("686974207468652062756c6c277320657965")
b3=[None]*min(len(b1),len(b2))


for b in range(min(len(b1),len(b2))):
    b3=[None]*min(len(b1),len(b2))
    b3[b] = b1[b]^b2[b]
    #print b3[b]

print("".join([(("{:x}".format(x))) for x in b3]))

