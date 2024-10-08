
from skimage import io
from matplotlib import pyplot as plt

img = io.imread("./images/etex.jpeg", as_gray=True)
plt.imshow(img, cmap='gray')
plt.show()

