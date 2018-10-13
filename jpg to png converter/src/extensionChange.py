from PIL import Image
import os
# img1 = Image.open('image1.jpg')
# img1.show()
# img1.save('image1.png')
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        #print(fext)
        # print (fn)
        i.save('png/{}.png'.format(fn))



