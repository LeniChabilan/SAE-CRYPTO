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



from scapy.all import UDP  # Ajoutez cette ligne pour importer explicitement UDP

from scapy.all import *
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Function to decrypt AES-256 CBC encrypted message with PKCS7 padding
def decrypt_aes_cbc(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    return unpadded_data

# Load the network capture file
capture = rdpcap('./analyse_trace/trace_sae.cap') 
# Replicate the key 4 times to obtain the 256-bit key
full_key = bytes([int(mes[i:i+8], 2) for i in range(0, len(mes), 8)]) * 4

# Define the protocol and port
protocol = 'plutotBonneConfidentialite'
port = 9999

# Iterate through the packets
for packet in capture:
    if UDP in packet and packet[UDP].dport == port:
        # Extract IV and encrypted message
        iv = packet[Raw].load[:16]
        ciphertext = packet[Raw].load[16:]

        # Decrypt the message
        decrypted_message = decrypt_aes_cbc(ciphertext, full_key, iv)

        # Print or process the decrypted message
        print(decrypted_message.decode('utf-8', errors='ignore'))
