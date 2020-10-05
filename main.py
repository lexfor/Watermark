from PIL import Image
import os

IMAGE_DIR = os.path.join(os.getcwd(), "images")
WAT_DIR = os.path.join(os.getcwd(), "watermark")
REZ_DIR = os.path.join(os.getcwd(), "rezults")
for filename in os.listdir(IMAGE_DIR):
    im = Image.open(os.path.join(IMAGE_DIR, filename))
    centerX = int(im.width / 2)
    centerY = int(im.height / 2)
    for name in os.listdir(WAT_DIR):
        transparent = Image.new('RGBA', (im.width, im.height), (0, 0, 0, 0))
        transparent.paste(im, (0, 0))
        water = Image.open(os.path.join(WAT_DIR, name))
        watCenterX = int(water.width / 2)
        watCenterY = int(water.height / 2)
        position = (centerX - watCenterX,
                    centerY - watCenterY)
        transparent.paste(water, position, mask=water)
        filename = filename[:-4]
        filename += '.png'
        conv = os.path.join(REZ_DIR, filename)
        transparent.save(conv)