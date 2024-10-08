from skimage import io
from matplotlib import pyplot as plt 
from skimage import filters

# Load the image in grayscale
img = io.imread("./etex.jpeg", as_gray=True)

# Apply different filters
robertImg = filters.roberts(img)
sobelImg = filters.sobel(img)
prewittImg = filters.prewitt(img)
scharrImg = filters.scharr(img)

# Create a figure with 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot each filtered image in the subplots
axes[0, 0].imshow(robertImg, cmap='gray')
axes[0, 0].set_title('Robert Filter')
axes[0, 0].axis('off')  # Hide the axes

axes[0, 1].imshow(sobelImg, cmap='gray')
axes[0, 1].set_title('Sobel Filter')
axes[0, 1].axis('off')

axes[1, 0].imshow(prewittImg, cmap='gray')
axes[1, 0].set_title('Prewitt Filter')
axes[1, 0].axis('off')

axes[1, 1].imshow(scharrImg, cmap='gray')
axes[1, 1].set_title('Scharr Filter')
axes[1, 1].axis('off')

# Adjust layout
plt.tight_layout()
plt.show()
