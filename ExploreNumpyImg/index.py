import numpy as np
import imageio

image = imageio.imread('./src/eid.jpg')

new_img = image * np.array([1,1,0])

imageio.imsave("./src/newImg3.jpg", new_img.astype(np.uint8))

print(new_img)

print(image)