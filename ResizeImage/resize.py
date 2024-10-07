from PIL import Image

img = Image.open("./src/etex.jpeg")


img.thumbnail((400,800))
img.show()
print(img.size)