from PIL import Image
from collections import defaultdict
import numpy as np
from math import floor

image_to_replicate = "hexabw.png" # must be png

blocks = {
    "black_concrete": [8, 10, 15, 255], #080a0f
    #"blue_concrete": [45, 47, 143, 255], #2d2f8f
    #"brown_concrete": [96, 60, 32, 255], #603c20
    #"cyan_concrete": [21, 119, 136, 255], #157788
    #"gravel": [132, 127, 127, 255], #847f7f
    #"gray_concrete": [55, 58, 62, 255], #373a3e
    #"green_concrete": [73, 91, 36, 255], #495b24
    #"light_blue_concrete": [36, 137, 199, 255], #2489c7
    #"light_gray_concrete": [125, 125, 115, 255], #7d7d73
    #"lime_concrete": [94, 169, 24, 255], #5ea918
    #"magenta_concrete": [169, 48, 159, 255], #a9309f
    #"orange_concrete": [224, 97, 1, 255], #e06101
    #"pink_concrete": [214, 101, 143, 255], #d6658f
    #"purple_concrete": [100, 32, 156, 255], #64209c
    #"red_concrete": [142, 33, 33, 255], #8e2121
    #"red_sand": [191, 103, 33, 255], #bf6721
    #"sand": [219, 207, 163, 255], #dbcfa3
    "white_concrete": [207, 213, 214, 255], #cfd5d6
    #"yellow_concrete": [241, 175, 21, 255] #f1af15
}


img = Image.open("images/"+image_to_replicate)
imgArr = np.fliplr(np.rot90(np.array(img)))
#print(imgArr.shape)
w, h, _ = imgArr.shape

def findClosest(r, g, b):
    bestBlock = ""
    bestDistance = 9999999999999999.0

    for block, colour in blocks.items():
        distance = (r-colour[0])**2+(g-colour[1])**2+(b-colour[2])**2

        if distance < bestDistance:
            bestBlock = block
            bestDistance = distance

    return blocks[bestBlock], bestBlock

outputImage = np.zeros(shape = (w, h, 4))
#outputBlocks = []#np.empty((w, h), dtype=str)
RLE = [] # run length encoding
totals = {}
cBlock = ""

for x in range(w):
    for y in range(h):
        outputImage[x, y], block = findClosest(*imgArr[x, y])
        if block not in totals:
            totals[block] = 0
        totals[block] += 1
        if cBlock != block or RLE[-1][1] == 64:
            cBlock = block
            RLE.append([block, 0])
        RLE[-1][1] += 1

#RLE = RLE + ["sand", 64]*floor(w/64)


#print(RLE)

print("\nTOTALS")
print(totals)

print("\nSIZE")
print(w, ":", h)

htmlPage = "<html><head><link rel=\"stylesheet\" href=\"tables.css\"><link rel=\"stylesheet\" href=\"base.css\"><title>Resouces</title></head><body><table class=\"pure-table pure-table-horizontal pure-table-bordered\">"
i = 0
for block, amount in RLE:
    i += 1
    blockyblock = block.split("_")
    
    col = " ".join(blockyblock[:-1]) if len(blockyblock) > 1 else blockyblock[0]
    if block == "red_sand":
        col = "red sand"
    colhtml = col

    if colhtml == "light blue":
        colhtml = "aqua"
    elif colhtml == "light green":
        colhtml = "limegreen"
    elif colhtml == "light gray":
        colhtml = "gainsboro"
    elif colhtml == "sand":
        colhtml = "moccasin"
    elif colhtml == "gravel":
        colhtml = "silver"
    elif colhtml == "red sand":
        colhtml = "peru"
    elif colhtml == "brown":
        colhtml = "saddlebrown"

    textCol = "black"
    #print(col, sum(blocks[block]))
    if sum(blocks[block]) < 500:
        textCol = "white"
    htmlPage += f"<tr style=\"background-color:{colhtml};color:{textCol}\"><th><b>{i}</b></th><th><img src=\"block_textures/{block}.png\"></th><th>{col}</th><th>{amount}</th><th><input type=\"checkbox\"></th></tr>"

htmlPage += "</table></body></html>"

i = 0
giveCommands = []
#"/give @p chest{BlockEntityTag:{Items:[{Slot:0,id:acacia_door,Count:1}]}} 1"
items = []
for block, amount in RLE:
    if i % 27 == 0 and i != 0:
        i = 0
        joined = ",".join(items)
        giveCommands.append(f"/give @p chest{{BlockEntityTag:{{Items:[{joined}]}}}}")
        items = []
        #print("nextt", len(RLE))
    
    blockPowder = block
    if blockPowder.split('_')[-1] == "concrete":
        blockPowder += "_powder"
    items.append(f"{{Slot:{i},id:{blockPowder},Count:{amount}}}")

    i += 1

joined = ",".join(items)
giveCommands.append(f"/give @p chest{{BlockEntityTag:{{Items:[{joined}]}}}}")
        


givers = "\n\n\n".join(giveCommands)
#print(giveCommands)
with open("images/"+image_to_replicate[:-4]+'-commands.txt', 'w') as f:
    f.write(givers)


with open("images/"+image_to_replicate[:-4]+"-resources.html", 'w') as f:
    f.write(htmlPage)

outputImage = outputImage.astype("uint8")
#print(outputImage)

outputImage = np.fliplr(np.rot90(outputImage))
invimg = Image.fromarray(outputImage)
#invimg.show()
invimg.save("images/"+image_to_replicate[:-4]+'-minecrafted.png')