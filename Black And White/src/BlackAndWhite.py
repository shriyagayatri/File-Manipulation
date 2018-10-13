from PIL import Image
import os

image1 = Image.open('diana.jpg')
image1.convert(mode = 'L').save('diana3.jpg')
image1.convert(mode = 'RGB').save('diana2.jpg') # Converts Black and White image to colour