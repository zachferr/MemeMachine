import sys
import cv2
import numpy as np
from scipy.misc import imread,imsave
from PIL import Image
from comic import comic
from compression import compress
from stylize import render

img = sys.argv[1]
img1 = comic(img)
img2 = compress('images/tmp/tmp1.jpg')
img3 = render(imread('images/tmp/tmp2.jpg'),ratio=0.001,verbose=True)
img3 = imsave('images/tmp/tmp3.jpg',img3)
img4 = render(imread('images/tmp/tmp3.jpg'), depth=4, verbose=True)
img4 = imsave('images/tmp/tmp4.jpg',img4)

list_im = [sys.argv[1], 'images/tmp/tmp2.jpg', 'images/tmp/tmp3.jpg', 'images/tmp/tmp4.jpg']
imgs = [Image.open(i) for i in list_im]
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

imgs_comb = np.vstack(np.asarray(i.resize(min_shape)) for i in imgs)
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('images/tmp/VStack.jpg')

def getSize():
    return min_shape