import PyPDF2


def mergeit(filename, wpage):

	with open(filename,'rb') as file:
		readobj = PyPDF2.PdfFileReader(file)
		no = readobj.getNumPages()
		with open('C:/Users/Tushhh/OneDrive/Desktop/PythonTraining/pythonPDF/superwater.pdf','wb') as file2:
			wobj = PyPDF2.PdfFileWriter()
			for i in range(no):
				singlePage = readobj.getPage(int(i))
				singlePage.mergePage(wpage)
				wobj.addPage(singlePage)
			wobj.write(file2)


watermark = open('C:/Users/Tushhh/OneDrive/Desktop/PythonTraining/pythonPDF/wtr.pdf', mode='rb')
waterobj = PyPDF2.PdfFileReader(watermark)
wpage = waterobj.getPage(0)
print(type(wpage))
filename = 'C:/Users/Tushhh/OneDrive/Desktop/PythonTraining/pythonPDF/super.pdf'
mergeit(filename, wpage)
watermark.close()