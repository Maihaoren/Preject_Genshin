import cv2
import numpy as np

def draw(pic):
    print(pic.max())
    print(pic)
    print(pic.max())
    lists=['#','M','@','=','-','O','D','-']
    print('')
    ans=''
    for i in pic:
        for o in i:
            num=o.sum()
            num=int(num/128)
            ans+=lists[num-1]
            ans+=' '
        ans+='\n'        
    return ans


