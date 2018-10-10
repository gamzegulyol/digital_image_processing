
# coding: utf-8

# In[9]:

import numpy as np
import matplotlib.pyplot as plt
image=plt.imread("kedi.jpg")
plt.imshow(image)
plt.show()
image.shape




# In[13]:

def my_function_1(img2):
    print(...)
    print("BOYUTU:",img2.ndim)
    print("Eksen Değerleri:",img2.shape)
    print("R için min değer")
    print(img2[:,:,0].min())
    print("R için max değer")
    print(img2[:,:,0].max())
    print("Boyutu:",img2.size)
my_function_1(image)


# In[17]:

def plti(image, h=8, **kwargs):
    """
    Helper function to plot an image.
    """
    y = image.shape[0]
    x = image.shape[1]
    w = (y/x) * h
    plt.figure(figsize=(w,h))
    plt.imshow(im, interpolation="none", **kwargs)
    plt.axis('off')

plti(image)
def to_grayscale(image, weights = np.c_[0.2989, 0.5870, 0.1140]):
    """
    Transforms a colour image to a greyscale image by
    taking the mean of the RGB values, weighted
    by the matrix weights
    """
    tile = np.tile(weights, reps=(image.shape[0],image.shape[1],1))
    return np.sum(tile * image, axis=2)
    
    


# In[19]:

img = to_grayscale(image)

plti(img, cmap='Greys')


# In[ ]:



