import cv2
import numpy as np
def thresholding(im_path,threshold_val=128):
    img=cv2.imread(im_path,cv2.IMREAD_GRAYSCALE)
    _, thresholed=cv2.threshold(img,threshold_val,225,cv2.THRESH_BINARY)

    cv2.imshow("Original Image",img)
    cv2.imshow('Thresh holded image',thresholed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

thresholding("Z:\python pycharm projects\Picture1.png",threshold_val=128)
thresholding("Z:\python pycharm projects\Picture1.png",threshold_val=128)