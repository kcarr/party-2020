# this was created and used to pre-process the partygopher gif into individual frames
# Reading an animated GIF file using Python Image Processing Library - Pillow

from PIL import Image
from PIL import GifImagePlugin

imageObject = Image.open("images/partygopher.gif")
 
for frame in range(0,imageObject.n_frames):

    if frame < 10:
        file_name = "0" + str(frame)
    else:
        file_name = str(frame)

    imageObject.seek(frame)
    imageObject.save("images/party_gopher/"+file_name+".png")