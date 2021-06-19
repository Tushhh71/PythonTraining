
import PyPDF2

with open("C:/Users/Tushhh/OneDrive/Desktop/pythonPDF/dummy.pdf", mode = 'rb') as file:

	pdfobj = PyPDF2.PdfFileReader(file)
	print(pdfobj.getNumPages())
	pageobj =  pdfobj.getPage(0)
	pageobj.rotateCounterClockwise(180) #pageobj contains rotated file content

	with open("C:/Users/Tushhh/OneDrive/Desktop/pythonPDF/Rotatedummy.pdf", mode = 'wb') as file2:
		writeobj = PyPDF2.PdfFileWriter()
		writeobj.addPage(pageobj)
		writeobj.write(file2)


