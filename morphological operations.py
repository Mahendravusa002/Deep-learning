import cv2
import numpy as np
def morphologicaal_operations(im_path):
    img=cv2.imread(im_path,cv2.IMREAD_GRAYSCALE)
    kernal=np.ones((5,5),np.int8)
    erosion=cv2.erode(img,kernal,iterations=1)
    cv2.imshow('original image',img)
    cv2.imshow('Erosion:',erosion)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#morphologicaal_operations('Z:\python pycharm projects\Picture1.png')
morphologicaal_operations('Z:\myphoto.png')