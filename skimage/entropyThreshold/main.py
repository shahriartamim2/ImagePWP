import numpy as np
from matplotlib import pyplot as plt
from skimage import io, restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk 
from skimage.filters import try_all_threshold
from skimage import feature
from skimage.filters import threshold_otsu

img = io.imread("../images/weftD.jpg", as_gray=True)
#entropyImg = entropy(img, disk(3))
#plt.imshow(entropyImg, cmap="gray")
edgeCanny = feature.canny(img, sigma=2)
plt.imshow(edgeCanny, cmap="gray")
#fig, ax = try_all_threshold(edgeCanny, figsize=(10,8), verbose = False)
thresh =threshold_otsu(edgeCanny)

binary = edgeCanny<=thresh
plt.imshow(binary, cmap="gray")