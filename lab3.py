
# coding: utf-8

# In[81]:

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy import stats
from scipy.stats import iqr
from scipy.stats import skew

image1= plt.imread("teletabi.jpg")
plt.imshow(image1)
plt.show()


# In[38]:

import os
cwd = os.getcwd()
cwd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
def reverse(x):
    return 255-x

image1[:,:,0]=reverse(image1[:,:,0])
image1[:,:,1]=reverse(image1[:,:,1])
image1[:,:,2]=reverse(image1[:,:,2])

#plt.subplot(1,2,1),plt.imshow(image1)
#plt.subplot(1,2,2),plt.imshow(255-image1)
plt.imshow(image1)
plt.show()


# In[90]:

def find_histogram(image):
    h1={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,0] in h1.keys()):
                h1[image[i,j,0]]+=1
            else:
                h1[image[i,j,0]]=1
    h2={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,1] in h2.keys()):
                h2[image[i,j,1]]+=1
            else:
                h2[image[i,j,1]]=1
                
    h3={}
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if(image[i,j,2] in h3.keys()):
                h3[image[i,j,2]]+=1
            else:
                h3[image[i,j,2]]=1
                
    plt.bar(list(h1.keys()), h1.values(),color='r')
    plt.show()
    plt.bar(list(h2.keys()), h2.values(),color='g')
    plt.show()
    plt.bar(list(h3.keys()), h3.values(),color='b')
    plt.show()

find_histogram(image1)


# In[ ]:




# In[86]:

def find(image1):
    print("Dimension:" , image1.ndim)
    print("Shape:" , image1.shape)
    
    print("\n---Min ve Max---\n")
    print("Min kırmızı renk değeri:" , image1[:,:,0].min()) #:,:,0 vs. dediğimizde o layer için ayrıca bakıyoruz. iki nokta'lar bütün satır ve bütün sütunu kapsıyor demek
    print("Max kırmızı renk değeri:" , image1[:,:,0].max())
    
    print("Min yesil renk değeri:" , image1[:,:,1].min())
    print("Max yesil renk değeri:" , image1[:,:,1].max())
    
    print("Min mavi renk değeri:" , image1[:,:,2].min())
    print("Max mavi renk değeri:" , image1[:,:,2].max())
    
    print("\n---Mean, Mode, Median---\n")
    print("Kırmızı için mean:", image1[:,:,0].mean())
    print("Yesil için mean:", image1[:,:,1].mean())
    print("Mavi için mean:", image1[:,:,2].mean())
    print("-----------")
    print("Kırmızı için mode",stats.mode(image1[:,:,0]))
    print("Yesil için mode",stats.mode(image1[:,:,1]))
    print("Mavi için mode",stats.mode(image1[:,:,2]))
    print("------------")
    print("Kırmızı için median",np.median(image1[:,:,0]))
    print("Yesil için median",np.median(image1[:,:,1]))
    print("Mavi için median",np.median(image1[:,:,2]))
    
    print("-----Ceyreklikler ve IQR Değerleri----")
    print("Kırmızı için Q1",np.percentile(image1[:,:,0],25))
    print("Kırmızı için Q2",np.percentile(image1[:,:,0],50))
    print("Kırmızı için Q3",np.percentile(image1[:,:,0],75))
    print("Kırmızı için IQR",iqr(image1[:,:,0]))
    print("Yesil için Q1",np.percentile(image1[:,:,1],25))
    print("Yesil için Q2",np.percentile(image1[:,:,1],50))
    print("Yesil için Q3",np.percentile(image1[:,:,1],75))
    print("Yesil için IQR",iqr(image1[:,:,1]))
    print("Mavi için Q1",np.percentile(image1[:,:,2],25))
    print("Mavi için Q2",np.percentile(image1[:,:,2],50))
    print("Mavi için Q3",np.percentile(image1[:,:,2],75))
    print("Mavi için IQR",iqr(image1[:,:,2]))
    
    print("-------Skewness Degerleri-------")
    print("Kırmızı için skewness",skew(image1[:,:,0]))
    print("Yesil için skewness",skew(image1[:,:,1]))
    print("Mavi için skewness",skew(image1[:,:,2]))
    
find(image1)
        
    


# In[ ]:

def find_outliers(image1):
    
    
    
    
    

