import numpy as np
import pandas as pd 
from PIL import Image,ImageFilter

#importing the image
path = "test.jpg"
img = Image.open(path)
#img.show()

#filtering the image and saving it 
img_sharp = img.filter(ImageFilter.SHARPEN)
img_sharp.save('test1.jpg','JPEG')

img_sharp = img.filter(ImageFilter.BLUR)
img_sharp.save('test2.jpg','JPEG')

img_sharp = img.filter(ImageFilter.MinFilter(3))
img_sharp.save('test3.jpg','JPEG')

img_sharp = img.filter(ImageFilter.CONTOUR)
img_sharp.save('test4.jpg','JPEG')

img_sharp = img.filter(ImageFilter.UnsharpMask())
img_sharp.save('test5.jpg','JPEG')
