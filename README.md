# Minecraft Perimeter Art
A set of python tools for creating pixel art perimeter walls in Minecraft.

## Example

![nomc](https://user-images.githubusercontent.com/30124354/155988528-c4aa6dca-117a-4eeb-85c7-85ccf9215609.png)

Into Minecraft

![yesmc](https://user-images.githubusercontent.com/30124354/155988524-0b772223-948a-4233-8304-f1241c9e89ec.png)

## How To Use
Use `imageAverage.py` to generate a new dictionary if you're using more than just the gravity blocks. Modify the `block_textures` folder to include your textures and if they use a different texture width, edit the `textureSize` variable in the script.

Edit the `image_to_replicate` variable in `pixelArtConcrete.py` to the name of the image you placed in the `images` folder. Run the script and it will generate the necessary files in that folder

Make sure that for any images you use, the height of the image in pixels is equal to the number of blocks BETWEEN (but not including) the floor and where you place it. You will want some extra blocks at the end to push through anything left behind on the conveyor when the printing is done.
