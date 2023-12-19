from DES import *

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import time
from PIL import Image
from binascii import unhexlify
from scapy.all import *

def chiffrage(message, cle):
    message_chiffre = ""
    for lettre in message:
        message_chiffre += chr(encrypt(cle, ord(lettre)))
    return message_chiffre

def dechiffrage(message_chiffre, cle):
    message_clair = ""
    for lettre in message_chiffre:
        message_clair += chr(decrypt(cle, ord(lettre)))
    return message_clair

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
    cpt=0
    for key in range(1024):
        key_binary = format(key, '010b')
        for key2 in range(1024):
            cpt+=1
            key_binary2 = format(key2, '010b')
            essai_dechiffre = dechifrementSDES(message_chiffre, int(key_binary2),int(key_binary))
            if essai_dechiffre == message_clair:
                print(cpt)
                return key_binary2 , key_binary
    print("Clé inconnue")

message_clair = "hello"
cle1 = 0000000000
cle2 = 1111

# message_chiffre = chifrementSDES(message_clair, cle1, cle2)
# print(message_chiffre)
# time1=time.time()
# cle_trouvee2 , cle_trouve = casse_brutal(message_clair, message_chiffre)
# time2=time.time()
# print(time2-time1)  
# print("Clé trouvée :", cle_trouvee2 , cle_trouve)


def cassage_astucieux(message_clair, message_chiffre):
    liste = {}
    cpt=0
    for key in range(1024):
        cpt+=1
        key_binary = format(key, '010b')
        liste[chiffrage(message_clair, int(key_binary))] = key_binary
    for key2 in range(1024):
        cpt+=1
        key_binary2 = format(key2, '010b')
        if dechiffrage(message_chiffre, int(key_binary2)) in liste:
            print(cpt)
            return liste[dechiffrage(message_chiffre, int(key_binary2))],key_binary2
        
    print("Clé inconnue")

# time1=time.time()
# cle_trouvee4 , cle_trouve3 = cassage_astucieux(message_clair, message_chiffre)
# time2=time.time()
# print(time2-time1)
# print("Clé trouvée :", cle_trouvee4 , cle_trouve3)



def chiffrement_aes(key, texte_clair):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    chiffreur = cipher.encryptor()
    # Ajout de remplissage (padding) pour garantir que la longueur est un multiple de la taille du bloc
    padder = padding.PKCS7(128).padder()
    texte_clair_padded = padder.update(texte_clair) + padder.finalize()
    texte_chiffre = chiffreur.update(texte_clair_padded) + chiffreur.finalize()
    return texte_chiffre

def dechiffrement_aes(key, texte_chiffre):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    dechiffreur = cipher.decryptor()
    texte_dechiffre = dechiffreur.update(texte_chiffre) + dechiffreur.finalize()
    # Retirer le remplissage (padding)
    unpadder = padding.PKCS7(128).unpadder()
    texte_clair = unpadder.update(texte_dechiffre) + unpadder.finalize()
    return texte_clair

texte_clair_connu = b'bonjour a tous'  
cle_aes = os.urandom(32)
texte_chiffre = chiffrement_aes(cle_aes, texte_clair_connu)
cle_devinee = dechiffrement_aes(cle_aes,texte_chiffre)
# print(texte_chiffre)
# print(cle_devinee)
