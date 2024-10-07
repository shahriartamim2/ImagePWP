from PIL import Image

img = Image.open("./src/etex.jpeg")


new = img.resize((900,900))
new.save("./src/newtex.jpeg", "JPEG")
new.show()
print(new.size)