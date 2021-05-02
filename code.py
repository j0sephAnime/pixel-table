import os, glob
from PIL import Image

def checkFiles():
	for fileName in os.listdir():
		if fileName != "pixelWhite.png":
			image = Image.new("RGBA", (24, 24), color = (255, 255, 255))
			image.save("pixelWhite.png")
			if fileName != "pixelBlack.png":
				image = Image.new("RGBA", (24, 24), color = (0, 0, 0))
				image.save("pixelBlack.png")
				if fileName != "background.png":
					image = Image.new("RGBA", (1920, 1080), color = (0, 0, 0))
					image.save("background.png")

def getNumber():
	files = glob.glob("result/*.png")
	number = 0
	for i in files:
		number = number + 1
	return number

checkFiles()
while True:
	x = int(input("x: "))
	y = int(input("y: "))
	if x <= 1920 / 24:
		if y <= 1080 / 24:
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