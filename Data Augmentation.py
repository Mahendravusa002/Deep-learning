import cv2
import numpy as np

def data_augmentation(im_path):
    img=cv2.imread(im_path)
    flipp=cv2.flip(img,1)
    cv2.imshow('Original Image',img)
    cv2.imshow('Flipped image',flipp)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#edge_detection("Z:\python pycharm projects\Picture1.png")
data_augmentation("Z:\myphoto.png")