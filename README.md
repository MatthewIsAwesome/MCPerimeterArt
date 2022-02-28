# Minecraft Perimeter Art
A set of python tools for creating pixel art perimeter walls in Minecraft.

## Example

![nomc](https://user-images.githubusercontent.com/30124354/155988121-dfc18899-7071-45ab-a25e-5d954ef3872d.png)

Into Minecraft

![yesmc](https://user-images.githubusercontent.com/30124354/155988113-46ec051e-5016-4c1a-b596-cb613698016c.png)

## How To Use
Use `imageAverage.py` to generate a new dictionary if you're using more than just the gravity blocks. Modify the `block_textures` folder to include your textures and if they use a different texture width, edit the `textureSize` variable in the script.

Edit the `image_to_replicate` variable in `pixelArtConcrete.py` to the name of the image you placed in the `images` folder. Run the script and it will generate the necessary files in that folder

Make sure that for any images you use, the height of the image in pixels is equal to the number of blocks BETWEEN (but not including) the floor and where you place it. You will want some extra blocks at the end to push through anything left behind on the conveyor when the printing is done.
