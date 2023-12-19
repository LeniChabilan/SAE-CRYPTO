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


resultat=analyse_image("rossignol2.bmp")
mes=resultat[:64]
print(mes)

def binaire_to_hexa(binaire):
    decimal=int(binaire,2)
    hexa=hex(decimal)[2:]
    return hexa.upper()
hexa=binaire_to_hexa(mes)
print(hexa)
    