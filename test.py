from DES import *
    
def chifrementSDES(text,cle1,cle2):
    cryp1=[]
    cryp2=[]
    motD=""
    for n in text:
        cryp1.append(encrypt(cle1,ord(n)))
    for n in cryp1:
        cryp2.append(encrypt(cle2,n))
    print(cryp1)
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

# res=chifrementSDES("hello",0000000000,1010101110)
# print(res)
# print(dechifrementSDES(res,0000000000,1010101110))


def casse_brutal(message_clair, message_chiffre):
    for key in range(1024):
        key_binary = format(key, '010b')
        for key2 in range(1024):
            key_binary2 = format(key2, '010b')
            essai_dechiffre = dechifrementSDES(message_chiffre, int(key_binary2),int(key_binary))
            if essai_dechiffre == message_clair:
                return key_binary2 , key_binary
    print("Clé inconnue")

message_clair = "hello"
cle1 = 0000000000
cle2 = 111

message_chiffre = chifrementSDES(message_clair, cle1, cle2)
print(message_chiffre)

cle_trouvee2 , cle_trouve = casse_brutal(message_clair, message_chiffre)

print("Clé trouvée :", cle_trouvee2 , cle_trouve)
