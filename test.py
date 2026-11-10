from PIL import Image, ImageEnhance, ImageOps

peterigloo = Image.open("peterigloo.jpg")

bw_peterigloo = peterigloo.convert("RGB")
hc_peterigloo = ImageEnhance.Contrast(bw_peterigloo).enhance(5)
emo_peterigloo = ImageEnhance.Brightness(hc_peterigloo).enhance(0.6)


# Inverterar alla pixlar över ett visst gränsvärde
emo_peterigloo = ImageOps.solarize(emo_peterigloo, 60)

# Lägger till en ram runt bilder
emo_peterigloo = ImageOps.expand(emo_peterigloo, 10, (255, 255, 255))

# Reducerar bitdjupet (antal färger)
emo_peterigloo = ImageOps.posterize(emo_peterigloo, 2)

# Skalar om en bild
emo_peterigloo = ImageOps.scale(emo_peterigloo, 0.2)

# Vänder en bild upp- och ned
emo_peterigloo = ImageOps.flip(emo_peterigloo)

# Spegelvänder en bild
emo_peterigloo = ImageOps.mirror(emo_peterigloo)


emo_peterigloo.save("new.jpg")