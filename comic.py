import sys
import numpy

import cv2


def comic(image):
    img = cv2.imread(image)
    # do edge detection on a grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    edges = cv2.blur(gray, (3, 3)) # this blur gets rid of some noise
    edges = cv2.Canny(edges, 50, 150, apertureSize=3) # this is the edge detection

    # the edges are a bit thin, this blur and threshold make them a bit fatter
    kernel = numpy.ones((3,3), dtype=numpy.float) / 12.0
    edges = cv2.filter2D(edges, 0, kernel)
    edges = cv2.threshold(edges, 50, 255, 0)[1]

    # and back to colour...
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # this is the expensive operation, it blurs things but keeps track of
    # colour boundaries or something, heck, just play with it
    shifted = cv2.pyrMeanShiftFiltering(img, 10, 20)

    # now compose with the edges, the edges are white so take them away
    # to leave black
    cv2.imwrite('images/tmp/tmp1.jpg',shifted)

if __name__ == '__main__':
    # load
    img = cv2.imread(sys.argv[1])
    comicImage = comic(img)
    cv2.imwrite('stage1.jpg', comicImage)