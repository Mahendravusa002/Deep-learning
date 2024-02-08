import cv2
import numpy as np
def edge_detection(im_path):
    img=cv2.imread(im_path,cv2.IMREAD_GRAYSCALE)
    edges=cv2.Canny(img,100,200)
    cv2.imshow('Original Image',img)
    cv2.imshow('Edges',edges)
    cv2.waitKey()
    cv2.destroyAllWindows()
#edge_detection("Z:\python pycharm projects\Picture1.png")
edge_detection("Z:\myphoto.png")