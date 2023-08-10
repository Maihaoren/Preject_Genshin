import cv2
import numpy as np
from genshin2_2 import draw

a=cv2.imread('pictures\\'+input(),1)
print(a.shape)
res=draw(a)   
print(res)
