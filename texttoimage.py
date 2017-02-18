from PIL import Image, ImageDraw, ImageFont
from iv import getSize
from memeifywords import getVerbose
import numpy as np
import sys

# create new image
imgx = getSize()[0] # image width in pixels
imgy = getSize()[1] # image height in pixels
i = 1
words = getVerbose(sys.argv[2])

phrases = [next(words),
            next(words),
            next(words),
            next(words)]
for phrase in phrases:
    image = Image.new("RGB", (imgx, imgy),'white')
    font = ImageFont.truetype('.gitignore/comicsans.ttf',28) # load default bitmap font
    draw = ImageDraw.Draw(image)
    words = phrase.split()
    lines = len(words)//5
    for j in range(0,lines+1):
        draw.text((10,imgy//3+imgy//10*j),' '.join(words[0+j*4:4+j*4]),font = font,fill='black')
        print(' '.join(words[0+j*4:4+j*4]))
        print(phrase)
    draw.text((10,imgy//3+imgy//10*(lines+1)),' '.join(words[4+lines*4:]),font = font,fill='black')
    image.save("images/tmp/tmpt" + str(i) + ".png", "PNG")
    i += 1

list_im = ['images/tmp/tmpt1.png', 'images/tmp/tmpt2.png', 'images/tmp/tmpt3.png', 'images/tmp/tmpt4.png']
imgs = [Image.open(i) for i in list_im]
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

imgs_comb = np.vstack(np.asarray(i.resize(min_shape)) for i in imgs)
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save('images/tmp/HStack.png')

list_im = ['images/tmp/VStack.jpg','images/tmp/HStack.png']
imgs = [Image.open(i) for i in list_im]
min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]

imgs_comb = np.hstack(np.asarray(i.resize(min_shape)) for i in imgs)
imgs_comb = Image.fromarray(imgs_comb)
imgs_comb.save(sys.argv[1][:sys.argv[1].index('.')]+' IV.png')