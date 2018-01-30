#!/usr/bin/python

from PIL import Image
import sys

def load_bmp (filename):
	bmp = Image.open ("3.bmp")
	print "Bitmap width: ", bmp.width
	print "Bitmap height: ", bmp.height, "\n"

	for y in range (bmp.height):
		for x in range (bmp.width):
			if bmp.getpixel ((x, y)) == 0:
				print "*",
			else:
				print " ",
		print ""


if len (sys.argv) == 2:
	print "First param is", sys.argv[1]
	if ".bmp" in sys.argv[1]:
		load_bmp (sys.argv[1])
	else:
		print "Filename is not .bmp"
else :
	print "Specify the filename"


