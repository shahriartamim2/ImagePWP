import numpy as np
from matplotlib import pyplot as plt
from skimage import io, restoration
from skimage.filters.rank import entropy
from skimage.morphology import disk 
from skimage.filters import try_all_threshold

img = io.imread("../images/defect.jpeg", as_gray=True)
entropyImg = entropy(img, disk(3))
#plt.imshow(entropyImg, cmap="gray")
fig, ax = try_all_threshold(entropyImg, figsize=(10,8), verbose = False)
plt.show()