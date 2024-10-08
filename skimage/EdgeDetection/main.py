from skimage import io, img_as_ubyte
from matplotlib import pyplot as plt 
from skimage import filters
from skimage import feature


# Load the image in grayscale
img = io.imread("./etex.jpeg", as_gray=True)

for i in range(10):
    edgeCanny = feature.canny(img, sigma=i)
    
    # Convert the floating-point image to 8-bit unsigned integers
    edgeCanny_uint8 = img_as_ubyte(edgeCanny)
    
    # Save as PNG
    io.imsave(f'canny_{i}.png', edgeCanny_uint8)

