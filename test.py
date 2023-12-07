from DES import *
    
def chifrementSDES(text,cle1,cle2):
    cryp1=[]
    cryp2=[]
    motD=""
    for n in text:
        cryp1.append(encrypt(cle1,ord(n)))
    for n in cryp1:
        cryp2.append(encrypt(cle2,n))
    print(cryp2)
    for n in cryp2:
        motD+=chr(n)
    return motD

def dechifrementSDES(text,cle1,cle2):
    decrypt1=[]
    decrypt2=[]
    for n in text:
        decrypt1.append(decrypt(cle2,ord(n)))
    for n in decrypt1:
        decrypt2.append(decrypt(cle1,n))
    motD=""
    for n in decrypt2:
        motD+=chr(n)
    return motD

res=chifrementSDES("hello      ",0000000000,111111)
print(res)
print("\n")
print(dechifrementSDES(res,0000000000,111111))


