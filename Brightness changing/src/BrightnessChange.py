from PIL import Image

image = Image.open("colourful.jpg")

# image.point creates a new copy of the original image

image.point(lambda x: x*0).save("dark.jpg")
image.point(lambda x: x*0.1).save("darkest.jpg")
image.point(lambda x: x*0.5).save("darker.jpg")
image.point(lambda x: x*1.5).save("bright.jpg")
image.point(lambda x: x*5.5).save("brighter.jpg")
image.point(lambda x: x*105.5).save("brightest.jpg")
