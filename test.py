import sys
import os
from matplotlib import pyplot as plt
from scipy.misc import imread,imsave

from stylize import render

if __name__ == "__main__":
	try:
		path = sys.argv[1]
	except:
		path = '1000stage2.jpg'

	# Load an image into a numpy format and see it
	img = imread(path)

	less_detail = render(img,ratio=0.001,verbose=True)
	abstract = render(less_detail, depth=4, verbose=True)

	print ("Saved results are in the examples directory!")
	imsave('images/'+sys.argv[1][:sys.argv[1].index('stage')]+'stage3.jpg',less_detail)
	imsave('images/'+sys.argv[1][:sys.argv[1].index('stage')]+'stage4.jpg',abstract)