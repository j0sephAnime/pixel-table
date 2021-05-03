import os.path, glob
from PIL import Image

if os.path.exists("background.png") == False:
	image = Image.new("RGBA", (1920, 1080), color = (0, 0, 0))
	image.save("background.png")
	if os.path.exists("pixelWhite.png") == False:
		image = Image.new("RGBA", (24, 24), color = (255, 255, 255))
		image.save("pixelWhite.png")
		if os.path.exists("pixelBlack.png") == False:
			image = Image.new("RGBA", (24, 24), color = (0, 0, 0))
			image.save("pixelBlack.png")

def getNumber():
	files = glob.glob("result/*.png")
	number = 0
	for i in files:
		number = number + 1
	return number

def pixelTable(x, y):
	image = Image.open("background.png")
	if image.getpixel((x * 24 - 24, y * 24 - 24)) == (0, 0, 0, 255):
		pixel = Image.open("pixelWhite.png")
		image.paste(pixel, (x * 24 - 24, y * 24 - 24),  pixel)
		image.save("background.png")
		image.save("result/background_" + str(getNumber()) + ".png")
	else:
		pixel = Image.open("pixelBlack.png")
		image.paste(pixel, (x * 24 - 24, y * 24 - 24),  pixel)
		image.save("background.png")
		image.save("result/background_" + str(getNumber()) + ".png")