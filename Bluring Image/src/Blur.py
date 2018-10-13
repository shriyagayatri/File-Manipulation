from PIL import Image , ImageFilter
import os
img1 = Image.open('image1.jpg')
img1.filter(ImageFilter.GaussianBlur()).save('image1(default).jpg')
img1.filter(ImageFilter.GaussianBlur(1)).save('image1(1).jpg')
img1.filter(ImageFilter.GaussianBlur(2)).save('image1(2).jpg')
img1.filter(ImageFilter.GaussianBlur(5)).save('image1(5).jpg')
img1.filter(ImageFilter.GaussianBlur(10)).save('image1(10).jpg')
img1.filter(ImageFilter.GaussianBlur(25)).save('image1(25).jpg')