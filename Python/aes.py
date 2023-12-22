from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def cryptageAES(data, clé):
    cryptage = AES.new(clé, AES.MODE_EAX)
    data =  data.encode("utf-8")
    text_crypté = cryptage.encrypt(data)
    return text_crypté, cryptage.nonce

def decryptageAES(text_crypté, clé,nonce):
    decipher = AES.new(clé, AES.MODE_EAX, nonce=nonce)
    text_decrypté = decipher.decrypt(text_crypté)
    return text_decrypté.decode("utf-8")

# Example usage
data = 'Hello world!'
clé = get_random_bytes(32)

# Encryption
text_crypté,nonce = cryptageAES(data, clé)
print("Text crypté:", text_crypté)

# Decryption
text_decrypté = decryptageAES(text_crypté, clé,nonce)
print("Text Décrypté:", text_decrypté)



