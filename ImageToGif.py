#-*- coding:utf-8 -*-
from PIL import Image,ImageSequence
import sys,os

#逆向提取GIF的帧
'''def processImage(infile):
	try:
		im = Image.open(infile)
	except IOError:
		print("Can't load",infile)
		sys.exit(1)
	i = 0
	mypalette = im.getpalette()

	try:
		while 1:
			im.putpalette(mypalette)
			new_im = Image.new("RGBA",im.size)
			new_im.paste(im)
			new_im.save("image\\fengche\\"+str(i)+'.png')

			i+=1
			im.seek(im.tell() + 1)
	except EOFError:
		pass

if __name__ == '__main__':
	processImage('fengche.gif')
	sys.exit()'''

#生成GIF图
def getGIF():
	image = []
	imN = 1
	filenames = os.listdir('F:\\pic\\aaa\\')
	filenames.sort(key = lambda x:int(x[:-4]))
	#print(filenames)
	for filename in filenames:
		if imN == 1:
			im = Image.open('F:\\pic\\aaa\\' + filename)
			imN = 2

		image.append(Image.open('F:\\pic\\aaa\\' + filename))

	im.save("image\\LF.gif",save_all = True, append_images = image, loop=100, duration = 500,
		comment = b"this is my fengche.gif")

if __name__ == '__main__':
	getGIF()
	sys.exit()
