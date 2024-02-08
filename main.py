import cv2
import numpy as np
def hist_equalization(im_path):
    im=cv2.imread(im_path,cv2.IMREAD_GRAYSCALE)
    eq=cv2.equalizeHist(im)

    cv2.imshow("original Image",im)
    cv2.imshow("Equalized image",eq)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()
#hist_equalization("Z:\python pycharm projects\Picture1.png")
hist_equalization("Z:\myphoto.png")