import os
import urllib.request
from PIL import Image


root_dir = os.path.dirname(os.path.curdir)
data_dir = os.path.join(root_dir, 'data')
struct_dir = os.path.join(data_dir,'structures')
proc_struct_dir = os.path.join(data_dir, 'structures_processed')

images = os.listdir(struct_dir)

for i in images[0:100]:
    image = Image.open(os.path.join(struct_dir, i))
    print(image.size)
    width, height = image.size
    if width != height:
        square_size = min(width, height)
        left = (width - square_size) / 2
        top = (height - square_size) / 2
        right = (width + square_size) / 2
        bottom = (height + square_size) / 2
        image = image.crop((left, top, right, bottom))
    print(image.size)
    image_sm = image.resize((256,256))
    print(image_sm.size)
    image_sm.save(os.path.join(proc_struct_dir, i))