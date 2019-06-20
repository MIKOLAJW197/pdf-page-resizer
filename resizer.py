from PyPDF2 import PdfFileReader, PdfFileWriter

def main():
	fileName = raw_input("Type your file name: ")

	pdfFile = PdfFileReader(open(fileName, 'rb'))
	# Getting only first page!
	newPage = pdfFile.getPage(0)

	newHeight = float(raw_input("Type your newHeight in mm"))
	newWidth = float(raw_input("Type your newWidth in mm"))

	# Conversion to points
	newHeight = newHeight * 2.83464567
	newWidth = newWidth * 2.83464567

	newPage.scaleTo(newWidth, newHeight)

	writer = PdfFileWriter()
	writer.addPage(newPage)

	with file('resize_' + fileName, "wb") as outfp:
		writer.write(outfp)

if __name__ == "__main__":
    main()
