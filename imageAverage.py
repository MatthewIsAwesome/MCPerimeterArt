from PIL import Image
from collections import defaultdict
import os

# get block textures from here or any resource pack: https://texture-packs.com/resourcepack/default-pack/#download
imageFolder = 'block_textures'
textureSize = 16

# find all images in dir
imageLocations = [imageFolder+"/"+f for f in os.listdir(imageFolder)]

for imageLoc in imageLocations:
    im = Image.open(imageLoc)
    byColour = defaultdict(int)
    for pixel in im.getdata():
        byColour[pixel] += 1
    
    avgCol = (.0, .0, .0);

    for colour, quantity in byColour.items():
        avgCol = [avgCol[x]+(colour[x]*quantity/float(textureSize**2)) for x in range(3)]
    
    avgColInt = [int(round(x, 0)) for x in avgCol]

    avgColHex = "#"+"".join(["0"+x if len(x) == 1 else x for x in [hex(x)[2:] for x in avgColInt]])

    print(imageLoc.split("/")[1].split(".")[0], avgColInt, avgColHex)
    