import numpy as np
from PIL import Image
import sys

list_im = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]]
imgs = [Image.open(i) for i in list_im]
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

imgs_comb = np.vstack(np.asarray(i.resize(min_shape)) for i in imgs)
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save(sys.argv[1][:sys.argv[1].index('.')]+' Stack.jpg')