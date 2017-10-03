# Uses takes a pdf and turns it into a picture, separated by page
from __future__ import print_function
from wand.image import Image
import os

#file source and resolution wanted
#note: 600+ resolution lets OCR work best, longer wait times
with Image(filename='pdfs/lorem.pdf', resolution = 600) as img:
    print('pages = ', len(img.sequence))

    #converts to png type and folder pyout
    with img.convert('png') as converted:
        converted.units='pixelsperinch'
        converted.save(filename='imgout/lorem.png')


#To run tesseract after img creation above for a txt file
#note:need to find way so that variable can be added below instead of directly
#naming the img file. Maybe by splitting string into sections
os.system("tesseract imgout/lorem.png imgout/lorem.txt -l eng --oem 2 --psm 1 -c tessedit_write_images=true")








#Unknownn
# from wand.image import Image
# # Converting first page into JPG
# with Image(filename="pdfs/master.pdf[0]") as img:
#      img.save(filename="temp.jpg")
# Resizing this image
# with Image(filename="temp.jpg") as img:
#      img.resize(200, 150)
#      img.save(filename="thumbnail_resize.jpg")
