#! python3
#resizeAndAddLogo.py - resizes all images in current working dir
#to fit into a 300x300 squre, adds catlogo.png to lowerright

## MAKE SURE THIS IS IN THE RIGHT DIRECTORY ALONG IWTH ITS PICTURES ##

import os
from PIL import Image

SQUARE_FIT_SIZE=300
LOGO_FILENAME="smallcat.png" #makesure the logo is small

logoIm=Image.open(LOGO_FILENAME)
logoWidth,logoHeight=logoIm.size
os.makedirs("withLogo",exist_ok=True) #makes a folder for the files

#Loop over all files in the working directory.
for filename in os.listdir("."):
    if not (filename.endswith('.png') or filename.endswith(',jpg')) \
       or filename==LOGO_FILENAME:
        continue #skip nonimage and logo file
    im=Image.open(filename)
    width,height=im.size

    #Check if image needs to be resized.
    if width> SQUARE_FIT_SIZE or height> SQUARE_FIT_SIZE:
        #calculate new size to fit to
        if width>height:
            height=int(height/(width/SQUARE_FIT_SIZE)) #try other way, ie w/SFS
            width=SQUARE_FIT_SIZE
        else:
            width=int(width/(height/SQUARE_FIT_SIZE))
            height=SQUARE_FIT_SIZE
            
       # Resize the image.
        print("resizing %s..." %(filename))
        im=im.resize((width,height))
       #add the logo.
    print("adding logo to %s..." % (filename))
    im.paste(logoIm,(width-logoWidth,height-logoHeight),logoIm)
       #  Save changes.
    im.save(os.path.join("withlogo",filename))







