


from PIL import Image,ImageFilter 
import PIL

photo = Image.open('C:/Users/Tushhh/OneDrive/Desktop/tushar.png')

photo.thumbnail((400,200))
photo.save('C:/Users/Tushhh/OneDrive/Desktop/dp.png','png')


# print(photo)

# print(photo.format)
# print(photo.size)
# print(photo.mode)

# print(dir(photo))

# filterImage = photo.filter(ImageFilter.BLUR)

# filterImage.save('C:/Users/Tushhh/OneDrive/Desktop/tusharFiltered.png','png')
# print(dir(Image))
# print(dir(ImageFilter))

# filterImage = photo.filter(ImageFilter.SMOOTH)
# print(type(filterImage))

# help(PIL.Image.Image)
# filterImage.save('C:/Users/Tushhh/OneDrive/Desktop/tusharFiltered3.png','png')

# # photo.show()
# photo.save('C:/Users/Tushhh/OneDrive/Desktop/tushar.png','png')
# filterImage = photo.convert('L').save('C:/Users/Tushhh/OneDrive/Desktop/tusharFiltered4.png','png')
# filterImage = photo.convert('L')
# filterImage.save('C:/Users/Tushhh/OneDrive/Desktop/tusharFiltered4.png','png')

# filterImage.show()


# photo.rotate(180).show()
# print(photo.size)

# photo.resize((500,100)).show()

# box = (50,100,2500,1500)
# cropped = photo.crop(box)
# cropped.show()

# photo.resize((1000,1000)).show()


# photo = Image.open('C:/Users/Tushhh/OneDrive/Desktop/resizedwall.png')

# a = photo.size
# print(a)

# photo.resize((1366,768)).save('C:/Users/Tushhh/OneDrive/Desktop/resizedwall.png','png')
