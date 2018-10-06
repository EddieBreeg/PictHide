from PIL import Image
import sys

def imageName(userInput):
	string = list(userInput)
	while 1:
		try:
			string.remove('"')
		except ValueError:
			name = ""
			for c in string:
				name += c
			return name
def output(name):
	i = len(name)-1
	while name[i] != '.':
		i -= 1
	name = name[:i] + "PictHideOutput.png"
	return name

def hide():
	userInput = input("Image a cacher: ")
	name = imageName(userInput)

	image1 = Image.open(name)
	userInput = input("Image support: ")
	name2 = imageName(userInput)
	image2 = Image.open(name2)

	pixels1 = image1.getdata()
	pixels2 = image2.getdata()

	new = []

	for i in range(len(pixels1)-1):
		try:
			r1, g1, b1 = pixels1[i]
		except ValueError:
			r1, g1, b1, a = pixels1[i]
		r1 = r1 >> 5
		g1 = g1 >> 5
		b1 = b1 >> 5
		
		try:
			r2,g2,b2 = pixels2[i]
		except ValueError:
			r2,g2,b2,a = pixels2[i]
		r2 = (r2>>3)*8 + r1
		g2 = (g2>>3)*8 + g1
		b2 = (b2>>3)*8 + b1
		new.append((r2,g2,b2))

	final = Image.new("RGB", (image1.size))
	final.putdata(new)
	name = output(name)
	final.save(name)
	
def reveal():
	userInput = input("Image: ")
	name = imageName(userInput)
	image1 = Image.open(name)

	pixels1 = image1.getdata()
	newPixelList = []

	for p in pixels1:
		r,g,b = p
		r = r%8
		g = g%8
		b = g%8
		
		r = (r<<5) + 16
		g = (g<<5) + 16
		b = (b<<5) + 16
		
		newPixelList.append((r,g,b))
		
	final = Image.new('RGB', image1.size)
	final.putdata(newPixelList)
	name = output(name)
	final.save(name)
	
exec(sys.argv[1])