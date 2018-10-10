
# coding: utf-8

# In[2]:

import numpy as np
import matplotlib.pyplot as plt
image=plt.imread("kedi.jpg")
plt.imshow(image)
plt.show()
image.shape
type(image)
image


# In[4]:

def my_function_1(img2):
    print(...)
    print(img2.ndim)
    print(img2.shape)
    print("R için min değer")
    print(img2[:,:,0].min())
    print("R için max değer")
    print(img2[:,:,0].max())
my_function_1(image)


# In[ ]:



