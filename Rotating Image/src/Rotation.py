from PIL import Image
import os

img1 = Image.open('image1.jpg')
img1.rotate(30).save('image1(30).jpg')
img1.rotate(45).save('image1(45).jpg')
img1.rotate(90).save('image1(90).jpg')
img1.rotate(120).save('image1(120).jpg')
img1.rotate(270).save('image1(270).jpg')
img1.rotate(360).save('image1(360).jpg')