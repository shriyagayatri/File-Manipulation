from PIL import Image
import os

#image1 = Image.open('google.png')
image2 = Image.open('google1.jpg')
if image2.mode == "RGBA":
    image2 = image2.convert("RGB")

new_filename = "google1.pdf"
if not os.path.exists(new_filename):
    image2.save(new_filename , "PDF" , resolution = 200)