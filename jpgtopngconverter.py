import sys
import os
from PIL import Image

try:
	a = sys.argv
	# print(a)

	jpgDir = a[1]
	pngDir = a[2]
	
	print(os.path.isdir(a[2]))
	print('here')

	if not os.path.isdir(a[2]):
		os.mkdir(a[2])

	files = os.listdir(a[1])
	print(files)
	for i in files:
		if not os.path.isfile(str(pngDir + i)): 
			a = Image.open(str(jpgDir + i))
			filesplit = i.split('.')
			print(str(pngDir + filesplit[0]+ '.png'))
			a.save(str(pngDir + filesplit[0]+ '.png'),'png')
			a = ''

except:
	print('something fishy')