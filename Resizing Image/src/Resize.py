from PIL import Image
import os


size_300 = (300,300)
'''size_100 = (100,100)
size_700 = (700,700)
size_1000 = (1000,1000)'''

for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn , fext = os.path.splitext(f)

        '''i.thumbnail(size_100)
        i.save('100/{}_100{}'.format(fn, fext))'''

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn , fext))

        '''i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn, fext))

        i.thumbnail(size_1000)
        i.save('1000/{}_1000{}'.format(fn, fext))'''