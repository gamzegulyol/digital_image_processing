
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
import os


image_rgb = plt.imread("resim.jpg")
print(image_rgb.shape)
plt.imshow(image_rgb)
plt.show()


# In[2]:

def get_distance(v,weight=[1/3,1/3,1/3]):
    a,b,c = v[0], v[1], v[2]
    w1,w2,w3 = weight[0], weight[1], weight[2]
    return ((a**2)*w1 + (b**2)*w2 + (c**2)*w3)**.5


# In[8]:

def rgb_to_graylevel(image_rgb):
    m,n = (image_rgb.shape[0],image_rgb.shape[1])

    image_graylevel = np.zeros((m,n))
    image_graylevel.setflags(write=1)

    for i in range(m):
        for j in range(n):
            #image_graylevel[i,j] = sqrt((image_rgb[i,j,0]*.3)**2 + (image_rgb[i,j,1]*.3)**2 + (image_rgb[i,j,2]*.4)**2)
            image_graylevel[i,j] = get_distance(image_rgb[i,j,:])

    return image_graylevel
       

#plt.imshow(rgb_to_graylevel(image_rgb))
image_graylevel = rgb_to_graylevel(image_rgb)
plt.imshow(image_graylevel, cmap='gray')
plt.show()



# In[9]:

mask_0 = np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3)
mask_0 = mask_0/9


# In[14]:

mask_1 = np.random.randint(20, size=9).reshape(3,3) #ilk parametre 0 ile kaç arasında random belirleneceğini, 2. parametre dizinin kaç elemanlı olacağını belirtir. reshape ise diziyi yeniden şekillendirir
mask_2 = np.random.randint(5, size=9).reshape(3,3)
print(mask_1)
print("-"*20)
print(mask_2)
print("-"*20)
print(mask_1*mask_2)
print("-"*20)
print(mask_1*mask_0)


# In[15]:

def get_default_mask_for_mean():
    return np.array([1,1,1,1,1,1,1,1,1]).reshape(3,3) / 9
    
def apply_mask(part_of_image, mask = get_default_mask_for_mean()):
    return sum(sum(part_of_image * mask))


# In[ ]:

def get_mean_filter(image): #yollanan image'ın graylevel olması gerek.
    m = image.shape[0]
    n = image.shape[1]

    image_2 = np.zeros((m,n))

    for i in range(1, m-1):
        for j in range(1, n-1):
            poi = image[i-1:i+2, j-1:j+2]
            image_2[i,j] = apply_mask(poi)
            
    return image_2

image_blurred = get_mean_filter(image_graylevel)
        
plt.imshow(image_blurred, cmap='gray')
plt.show()


# In[ ]:

mask_1 = np.random.randint(20, size=9).reshape(3,3)
mask_1


# In[5]:

s_1=image_2[3:6,10:13].reshape(1,9)
print(s_1)
s_1.sort(s_1)
print(s_1)
print(s_1[0,4])


# In[ ]:



