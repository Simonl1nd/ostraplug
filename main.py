from PIL import Image, ImageDraw

# RGB-värden för blå och gul
RED = (200, 16, 46)
WHITE = (255, 255, 255)

# Skapa en ny bild
im = Image.new("RGB", (185, 140), RED)

# Skapa ett ImageDraw-objekt för att kunna rita grafik
imd = ImageDraw.Draw(im)

# Rita två rektanglar
imd.rectangle([(60, 0), (80, 140)], WHITE)
imd.rectangle([(0, 60), (185, 80)], WHITE)

im.save("flag.png")