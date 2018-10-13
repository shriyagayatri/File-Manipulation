from PIL import Image

name ="python.jpg"
image1 = Image.open(name);
size = width , height = image1.size;
coordinate = x , y = 69 , 47
print(image1.getpixel(coordinate));
