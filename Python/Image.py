from PIL import Image

def analyse_image(chemin):
    res=""
    img= Image.open(chemin)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            valeur=img.getpixel((j,i))
            if valeur%2==0:
                res+="0"
            else: 
                res+="1"
    return res


resultat=analyse_image("Image/rossignol2.bmp")
mes=resultat[:64]



from scapy.all import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Fonction pour décrypter un message chiffré AES-256 en mode CBC avec un remplissage PKCS7
def decrypt_aes_cbc(texte_chiffre, cle, vecteur_initialisation):
    chiffrer = Cipher(algorithms.AES(cle), modes.CBC(vecteur_initialisation), backend=default_backend())
    decrypteur = chiffrer.decryptor()
    pad = padding.PKCS7(128).unpadder()

    donnees_dechiffrees = decrypteur.update(texte_chiffre) + decrypteur.finalize()
    pad_data = pad.update(donnees_dechiffrees) + pad.finalize()

    return pad_data

# Charger le fichier de capture réseau
capture = rdpcap('./analyse_trace/trace_sae.cap') 

# Répliquer la clé 4 fois pour obtenir la clé de 256 bits
cle_complete = bytes([int(mes[i:i+8], 2) for i in range(0, len(mes), 8)]) * 4

port = 9999

for paquet in capture:
    if UDP in paquet and paquet[UDP].dport == port:
        # Extraire le vecteur d'initialisation et le message chiffré
        vecteur_initialisation = paquet[Raw].load[:16]
        texte_chiffre = paquet[Raw].load[16:]
        message_dechiffre = decrypt_aes_cbc(texte_chiffre, cle_complete, vecteur_initialisation)
        print(message_dechiffre.decode('utf-8', errors='ignore'))
